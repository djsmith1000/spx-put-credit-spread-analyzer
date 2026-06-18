#!/usr/bin/env python3
"""
Wheel Strategy Analyzer & Manager

Starter script for advanced wheel position tracking, rolling recommendations,
new candidate scanning, and integration with IBKR (via ib_insync or TWS API).

Extends the SPX put credit spread analyzer patterns (Monte Carlo, rolling logic,
allocation vs SGOV/cash reserves, position sizing).

Features to implement:
- Parse IBKR positions for wheel underlyings only.
- Compute status: DTE, ITM/OTM, intrinsic/time value, est. delta.
- Rolling rules engine differentiated by hold_type: 'longterm' | 'moderate' | 'opportunistic'
  (longterm/moderate bias to rolls/assignment+wheel to preserve exposure; opportunistic = faster profit/exit).
- Portfolio heat: correlation between holdings (e.g. materials ABAT/TTI, high-vol ONDS, nuclear LEU).
- Allocation target: ~50% NAV in wheels; suggest contract sizes by hold_type, IV, conviction.
- Scanner: filter by liquidity, IV_percentile, no earnings soon, sector diversity, thematic fit (nuclear/AI power for moderate holds).
- Monte Carlo roll simulator (adapt from SPX analyzer).
- Dashboard export or Lovable.dev friendly JSON.

Dependencies (user to pip): ib_insync, pandas, numpy, scipy (BS), yfinance/polygon.

Usage:
  python wheel_analyzer.py --positions
  python wheel_analyzer.py --scan --min_iv_rank 0.30 --max_price 150

Author: Grok xAI for djsmith1000 | 2026-06-18 (updated with LEU/ONDS moderate hold)
"""

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Literal

HoldType = Literal['longterm', 'moderate', 'opportunistic']

@dataclass
class WheelPosition:
    underlying: str
    hold_type: HoldType
    shares: int = 0
    short_puts: Dict = None
    short_calls: Dict = None
    avg_cost: float = 0.0
    current_price: float = 0.0
    unrealized_pnl: float = 0.0
    iv_rank: float = 0.0
    dte: int = 0

    def status(self) -> str:
        parts = [f"{self.underlying} ({self.hold_type}): "]
        if self.shares > 0:
            parts.append(f"Long {self.shares} sh @${self.avg_cost:.2f} (now ${self.current_price:.2f})")
        if self.short_puts:
            parts.append(f"Short {self.short_puts.get('contracts',0)}x ${self.short_puts.get('strike')}p {self.short_puts.get('exp')}")
        if self.short_calls:
            parts.append(f"Short {self.short_calls.get('contracts',0)}x ${self.short_calls.get('strike')}c {self.short_calls.get('exp')}")
        return " | ".join(parts)

    def roll_recommendation(self) -> str:
        """Differentiated rule engine by hold_type. Expand with real delta/IV/profit/BS calc."""
        pnl = self.unrealized_pnl
        dte = self.dte
        itm = False
        if self.short_puts and self.current_price < self.short_puts.get('strike', 999):
            itm = True
        if self.short_calls and self.current_price > self.short_calls.get('strike', 0):
            itm = True

        if self.hold_type == 'longterm':
            if self.short_calls and itm:
                return "ROLL CC up/out to preserve shares (longterm priority)"
            if self.short_puts and dte < 7:
                return "Let put expire or roll for income (preserve exposure)"
            return "HOLD / manage premium, add on dips, bias to maintain position"
        elif self.hold_type == 'moderate':
            if pnl < -300 and itm:  # e.g. ONDS distress but moderate
                return "PREFER ROLL or ASSIGN+ immediate CC wheel (moderate hold: recover via premium, maintain some exposure)"
            if itm:
                return "ROLL or let assign + wheel CCs (moderate interest supports holding/wheeling shares)"
            if dte < 14 and pnl > 0:
                return "Take profit or roll; flexible but bias to continue wheel"
            return "Ride/roll OTM CSP or plan post-assignment CC (thematic like LEU nuclear/AI power)"
        else:  # opportunistic
            if pnl < -200:
                return "CLOSE immediately - no attachment, limit loss (e.g. F)"
            if dte < 14 and pnl > 0:
                return "Take profit or roll to next cycle; flexible exit"
            return "Monitor news/IV; scale or exit on weakness (no attachment)"


def load_current_positions() -> List[WheelPosition]:
    """Stub - replace with real IBKR query or positions export parse. Includes LEU/ONDS per correction."""
    return [
        WheelPosition(
            underlying='ABAT', hold_type='longterm', shares=2600,
            short_calls={'strike': 3, 'exp': '2026-07-17', 'contracts': 6, 'premium_collected': 0.443},
            avg_cost=3.095, current_price=3.05, unrealized_pnl=-117, iv_rank=0.35, dte=29
        ),
        WheelPosition(
            underlying='TTI', hold_type='longterm', shares=600,
            short_puts={'strike': 10, 'exp': '2026-07-17', 'contracts': 2, 'premium_collected': 0.693},
            short_calls={'strike': 11, 'exp': '2026-09-18', 'contracts': 4, 'premium_collected': 1.039},
            avg_cost=9.567, current_price=10.15, unrealized_pnl=353, iv_rank=0.05, dte=29
        ),
        WheelPosition(
            underlying='F', hold_type='opportunistic',
            short_puts={'strike': 16.5, 'exp': '2026-07-10', 'contracts': 2, 'premium_collected': 0.557},
            current_price=14.03, unrealized_pnl=-386, iv_rank=0.65, dte=22
        ),
        WheelPosition(
            underlying='SOFI', hold_type='opportunistic',
            short_puts={'strike': 17, 'exp': '2026-07-17', 'contracts': 2, 'premium_collected': 0.863},
            current_price=17.77, unrealized_pnl=23, iv_rank=0.40, dte=29
        ),
        WheelPosition(  # LEU moderate hold - nuclear/AI power thematic
            underlying='LEU', hold_type='moderate',
            short_puts={'strike': 160, 'exp': '2026-10-16', 'contracts': 1, 'premium_collected': 25.75},
            current_price=189.20, unrealized_pnl=-40, iv_rank=0.15, dte=120
        ),
        WheelPosition(  # ONDS moderate hold - high vol speculative
            underlying='ONDS', hold_type='moderate',
            short_puts={'strike': 11, 'exp': '2026-07-17', 'contracts': 4, 'premium_collected': 0.977},
            current_price=9.04, unrealized_pnl=-499, iv_rank=0.05, dte=29
        ),
    ]


def analyze_and_recommend(positions: List[WheelPosition]) -> Dict:
    results = {
        'timestamp': datetime.now().isoformat(),
        'total_unrealized': sum(p.unrealized_pnl for p in positions),
        'recommendations': []
    }
    for p in positions:
        rec = {
            'underlying': p.underlying,
            'hold_type': p.hold_type,
            'status': p.status(),
            'action': p.roll_recommendation(),
        }
        results['recommendations'].append(rec)
    return results


def scan_new_candidates(min_iv_rank: float = 0.30, max_price: float = 150.0) -> List[Dict]:
    """Stub scanner. Enhance with earnings calendar, thematic scoring (nuclear/AI for moderate), sector diversity."""
    candidates = [
        {'symbol': 'AMD', 'why': 'High IV AI/semicon, liquid weeklies, prior wheel familiarity (opportunistic or moderate)', 'iv_rank_est': 0.45, 'price': 152},
        {'symbol': 'NVDA', 'why': 'Top tier IV, AI cycle (opportunistic/moderate, capital intensive)', 'iv_rank_est': 0.55, 'price': 140},
        {'symbol': 'PLTR', 'why': 'AI growth, high interest/IV (opportunistic/moderate)', 'iv_rank_est': 0.40, 'price': 45},
        {'symbol': 'SPY', 'why': 'Core stable wheel for base income + accumulation (longterm ballast for 50% target)', 'iv_rank_est': 0.25, 'price': 600},
        {'symbol': 'XOM', 'why': 'Energy diversification, premium + dividend (moderate or opportunistic)', 'iv_rank_est': 0.35, 'price': 110},
        {'symbol': 'LEU', 'why': 'Nuclear/AI power thematic complement to existing LEU wheel (moderate hold)', 'iv_rank_est': 0.20, 'price': 189},
    ]
    return [c for c in candidates if c['iv_rank_est'] >= min_iv_rank and c['price'] <= max_price]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wheel Analyzer (supports longterm/moderate/opportunistic)')
    parser.add_argument('--positions', action='store_true', help='Analyze current wheel positions (incl. LEU/ONDS)')
    parser.add_argument('--scan', action='store_true', help='Scan for new wheel candidates')
    parser.add_argument('--min-iv-rank', type=float, default=0.30)
    parser.add_argument('--max-price', type=float, default=150.0)
    args = parser.parse_args()

    if args.positions:
        pos = load_current_positions()
        analysis = analyze_and_recommend(pos)
        print(json.dumps(analysis, indent=2))
    elif args.scan:
        cands = scan_new_candidates(args.min_iv_rank, args.max_price)
        print('New Wheel Candidates (consider moderate-hold potential e.g. nuclear/AI power):')
        for c in cands:
            print(f"  {c['symbol']}: {c['why']} (est IV rank {c['iv_rank_est']}, ~${c['price']})")
    else:
        print('Wheel Analyzer scaffold ready. Use --positions or --scan. Extended for hold_type differentiation (longterm/moderate/opportunistic) and LEU/ONDS examples. Ready for IBKR feed, full greeks, Monte Carlo per type.')

# TODOs:
# - IBKR connect (ib_insync) for live positions, chains, greeks, delta
# - Full BS model or IBKR greeks for precise roll triggers (delta, theta, IV rank)
# - Earnings/news filter + thematic scorer (nuclear/AI power boosts moderate-hold score)
# - Monte Carlo simulator per hold_type (adapt SPX analyzer)
# - Position sizing: risk % of wheel bucket, adjusted by hold_type conviction & IV
# - Export JSON/CSV for dashboard or GitHub sync
# - Alerts on ITM moves or catalysts
"""