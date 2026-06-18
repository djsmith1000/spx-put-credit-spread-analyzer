#!/usr/bin/env python3
"""
Wheel Strategy Analyzer & Manager

Starter script for advanced wheel position tracking, rolling recommendations,
new candidate scanning, and integration with IBKR (via ib_insync or TWS API).

Extends the SPX put credit spread analyzer patterns (Monte Carlo, rolling logic,
allocation vs SGOV/cash reserves, position sizing).

Features to implement:
- Parse IBKR positions (get_account_positions style) for wheel underlyings only.
- Compute status: DTE, ITM/OTM, intrinsic/time value, est. delta (BS approx or IBKR greeks if avail).
- Rolling rules engine: inputs (hold_type='longterm'|'opportunistic', current_premium, profit_pct, delta, DTE, IV_rank) -> action: 'let_expire' | 'roll_out_up' | 'roll_down' | 'close' | 'add_leg' | 'pyramid'
- Portfolio heat: correlation between ABAT/TTI (materials), SOFI/F (fin/auto), new adds.
- Allocation target: ~50% NAV in wheels; suggest contract sizes based on buying_power, IV, conviction.
- Scanner: filter tickers by liquidity (OI/volume), IV_percentile > X, no earnings in 14d, support levels, sector diversity.
- Monte Carlo roll simulator (like SPX): project P/L distributions for different roll strategies.
- Dashboard export or Lovable.dev friendly JSON output.

Dependencies (user to pip install): ib_insync, pandas, numpy, scipy (for BS), yfinance/polygon for scanner fallback.

Usage:
  python wheel_analyzer.py --positions  # or live IBKR connect
  python wheel_analyzer.py --scan --min_iv_rank 35 --max_price 150

Author: Grok xAI for djsmith1000 | 2026-06-18 initial scaffold
"""

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from typing import List, Dict, Optional, Literal

# Placeholder for IBKR integration - replace with real calls or ib_insync
# from ib_insync import IB, Stock, Option, util

HoldType = Literal['longterm', 'opportunistic']

@dataclass
class WheelPosition:
    underlying: str
    hold_type: HoldType
    shares: int = 0
    short_puts: Dict = None  # e.g. {'strike': 10, 'exp': '2026-07-17', 'contracts': 2, 'premium_collected': 0.693}
    short_calls: Dict = None
    avg_cost: float = 0.0
    current_price: float = 0.0
    unrealized_pnl: float = 0.0
    iv_rank: float = 0.0  # percentile
    dte: int = 0

    def status(self) -> str:
        """Quick status string for dashboard."""
        parts = [f"{self.underlying}: "]
        if self.shares > 0:
            parts.append(f"Long {self.shares} sh @${self.avg_cost:.2f} (now ${self.current_price:.2f})")
        if self.short_puts:
            parts.append(f"Short {self.short_puts['contracts']}x ${self.short_puts['strike']}p {self.short_puts['exp']}")
        if self.short_calls:
            parts.append(f"Short {self.short_calls['contracts']}x ${self.short_calls['strike']}c {self.short_calls['exp']}")
        return " | ".join(parts)

    def roll_recommendation(self) -> str:
        """Basic rule engine stub. Expand with real delta/IV/profit calc."""
        if self.hold_type == 'longterm':
            if self.short_calls and self.current_price > self.short_calls.get('strike', 999) * 0.95:
                return "ROLL CC up/out to preserve shares (longterm priority)"
            if self.short_puts and self.dte < 7:
                return "Let put expire or roll for income (low IV ok for TTI)"
            return "HOLD / manage premium, add on dips"
        else:  # opportunistic
            if self.unrealized_pnl < -200:  # e.g. F case
                return "CLOSE immediately - no attachment, limit loss"
            if self.dte < 14 and self.unrealized_pnl > 0:
                return "Take profit or roll to next cycle"
            return "Monitor news/IV; flexible exit or scale on weakness"


def load_current_positions() -> List[WheelPosition]:
    """Stub - in prod: query IBKR or parse JSON from positions export."""
    # Example from 2026-06-18 snapshot
    return [
        WheelPosition(
            underlying='ABAT',
            hold_type='longterm',
            shares=2600,
            short_calls={'strike': 3, 'exp': '2026-07-17', 'contracts': 6, 'premium_collected': 0.443},
            avg_cost=3.095,
            current_price=3.05,
            unrealized_pnl=-117,
            iv_rank=0.35,
            dte=29
        ),
        WheelPosition(
            underlying='TTI',
            hold_type='longterm',
            shares=600,
            short_puts={'strike': 10, 'exp': '2026-07-17', 'contracts': 2, 'premium_collected': 0.693},
            short_calls={'strike': 11, 'exp': '2026-09-18', 'contracts': 4, 'premium_collected': 1.039},
            avg_cost=9.567,
            current_price=10.15,
            unrealized_pnl=353,
            iv_rank=0.05,
            dte=29
        ),
        WheelPosition(
            underlying='F',
            hold_type='opportunistic',
            short_puts={'strike': 16.5, 'exp': '2026-07-10', 'contracts': 2, 'premium_collected': 0.557},
            current_price=14.03,
            unrealized_pnl=-386,
            iv_rank=0.65,
            dte=22
        ),
        WheelPosition(
            underlying='SOFI',
            hold_type='opportunistic',
            short_puts={'strike': 17, 'exp': '2026-07-17', 'contracts': 2, 'premium_collected': 0.863},
            current_price=17.77,
            unrealized_pnl=23,
            iv_rank=0.40,
            dte=29
        ),
    ]


def analyze_and_recommend(positions: List[WheelPosition]) -> Dict:
    """Main analysis pass."""
    results = {
        'timestamp': datetime.now().isoformat(),
        'total_unrealized': sum(p.unrealized_pnl for p in positions),
        'recommendations': []
    }
    for p in positions:
        rec = {
            'underlying': p.underlying,
            'status': p.status(),
            'action': p.roll_recommendation(),
            'hold_type': p.hold_type
        }
        results['recommendations'].append(rec)
    return results


def scan_new_candidates(min_iv_rank: float = 0.30, max_price: float = 150.0) -> List[Dict]:
    """Stub scanner. In prod: use yfinance.Ticker.info or IBKR search + fundamentals,
    or paid API (polygon). Filter liquid, no earnings soon, sector diversity."""
    candidates = [
        {'symbol': 'AMD', 'why': 'High IV AI/semicon, liquid weeklies, prior wheel familiarity', 'iv_rank_est': 0.45, 'price': 152},
        {'symbol': 'NVDA', 'why': 'Top tier IV, AI cycle, but capital intensive per lot', 'iv_rank_est': 0.55, 'price': 140},
        {'symbol': 'PLTR', 'why': 'AI growth, high retail/IV interest, good liquidity', 'iv_rank_est': 0.40, 'price': 45},
        {'symbol': 'SPY', 'why': 'Core stable wheel, "for life" accumulation, ultra liquid, low risk', 'iv_rank_est': 0.25, 'price': 600},
        {'symbol': 'XOM', 'why': 'Energy diversification, premium + dividend, stagflation hedge', 'iv_rank_est': 0.35, 'price': 110},
    ]
    return [c for c in candidates if c['iv_rank_est'] >= min_iv_rank and c['price'] <= max_price]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Wheel Analyzer')
    parser.add_argument('--positions', action='store_true', help='Analyze current wheel positions')
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
        print('New Wheel Candidates:')
        for c in cands:
            print(f"  {c['symbol']}: {c['why']} (est IV rank {c['iv_rank_est']}, ~${c['price']})")
    else:
        print('Wheel Analyzer scaffold ready. Use --positions or --scan. Extend with real IBKR data feed and full BS greeks/roll engine.')

# TODOs for full tool:
# - Connect to IBKR (ib_insync.IB().connect('127.0.0.1', 7497, clientId=1))
# - Fetch live option chains via reqMktData or snapshot for IV/delta
# - Earnings calendar filter (use yfinance or IBKR fundamental data)
# - MonteCarlo roll simulator (reuse/adapt from spx analyzer)
# - Export to JSON/CSV for Lovable.dev dashboard or GitHub sync
# - Position sizing: risk % of wheel bucket (target 50% NAV), adjust for IV & conviction
# - Alerts: email/slack on ITM moves, news via RSS or API
"""