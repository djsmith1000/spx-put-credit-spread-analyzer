# Wheel Strategy Portfolio Summary & Analysis
**Updated:** 2026-06-18 (IBKR live data) | **Account NAV ~$177k long** | **Target: ~50% allocated to wheel positions** (currently under-allocated)

## Core Philosophy (per user prefs)
- **Long-term holds / Accumulation**: ABAT (battery recycling bullish), TTI (magnesium thixomolding + EV + Magrathea partnership bullish). These get preferential treatment for rolling/assignment avoidance to maintain exposure.
- **Opportunistic**: F, SOFI (and future adds). No emotional attachment — prioritize capital preservation, quick rolls/closes, or reassignment decisions based on data. Willing to exit entirely if thesis breaks or losses mount.
- **Advanced Wheel Mgmt**: Multi-leg (CSP + CC where applicable), rolling based on delta/IV/profit targets (e.g. 50% profit take or roll at 21-30 DTE), factor in vol (IV rank/percentile), news catalysts, technical support levels, portfolio correlation/heat, earnings calendar. Consider opportunistic vs core holds for strike selection and size.
- **Risk/Allocation**: Aim for ~half IBKR capital in wheels (diverse underlyings, position sizing by IV & conviction). Use defined-risk where possible or size CSPs conservatively. Monitor overall Greeks exposure, assignment risk, and margin.
- **Scanning for New**: High liquidity options, IV rank >30-50% preferred for premium, price $5-150, no major earnings in next 2-4 wks or plan around, good volume/OI, diverse sectors from current (avoid over-concentration in materials/EV/auto/fintech). Balance high-IV opportunistic with lower-IV core like SPY/QQQ for stability.

## Current Wheel Positions (from IBKR get_account_positions + snapshots)

### 1. ABAT (Long-term Accumulation / Thematic Bullish)
- **Stock**: Long 2,600 shares @ avg $3.095 | Current $3.05 (-1.61% today, YTD -8.7%) | Unrealized P/L: -$117 | HV ~130% ann. (elevated), IV percentile low-moderate (20-61% windows)
- **Short Calls (Covered partial)**: Short 6x Jul17'26 $3 CALL @AMEX (collected ~$0.443/contract) | Current premium $0.40 | P/L on premium: +$26 | IV ~110% ann. | Stock slightly ITM (delta high ~0.55+ est.), 29 DTE. Covers 600 shares.
- **Capital/Status**: ~$7.9k stock value tied. Short calls OTM time value still decent but ITM risk. Partial wheel (long shares + CC).
- **Analysis & Recs**:
  - Thematic hold: Battery recycling story intact; small position, accumulation mode ok.
  - Short $3c ITM slightly: High assignment risk on 600 shares if holds/rallies into Jul. Since **long-term bullish**, do **not** want full assignment — roll the short calls.
  - **Recommended Action**: Roll Jul $3c to Aug (or later) higher strike e.g. $3.5-$4 if premium attractive, or out in time for more credit. Or close calls if want free up (but prefer keep covered income). Monitor for 50% profit or delta >0.40-0.45.
  - Multi-level: Can add more shares on dips or more OTM CCs on additional lots for income while holding core.
  - Watch: News on US battery policy, recycling mandates, lithium/metal prices. High vol good for premium but assignment risk.

### 2. TTI (Long-term Accumulation / Thematic Bullish)
- **Stock**: Long 600 shares @ avg $9.567 | Current $10.15 (+0.2% today, YTD +8.3%) | Unrealized P/L: +$353 | HV ~59% ann., **very low IV percentile** (3-6% — cheap premium environment, good for sellers but lower yields)
- **Short Puts (CSP phase)**: Short 2x Jul17'26 $10 PUT @AMEX (collected ~$0.693) | Current $0.70 | P/L ~+$15-16 | IV ~61% | Stock OTM (10.15 >10), ~29 DTE. Buying power ~$2k.
- **Short Calls (Covered partial)**: Short 4x Sep18'26 $11 CALL @AMEX (collected ~$1.039) | Current ~$1.08 | P/L ~+$7 | IV ~63-65% | Stock OTM (10.15 <11), longer 92 DTE. Covers 400 shares.
- **Capital/Status**: ~$6.1k stock. Multi-leg advanced wheel active (CSP + CC on long shares). Good income layer.
- **Analysis & Recs**:
  - Strong thematic: Magnesium for EV/thixomolding + partnership belief holds. Profitable shares + premium collection ideal.
  - Jul $10p OTM: Comfortable, can let expire worthless or roll to Aug if want continue CSP income (low IV = modest premium).
  - Sep $11c OTM: Excellent for long-term hold — collect premium, allows upside to 11. Manage by rolling up/out if stock approaches 10.5-10.8 (e.g. to $12+ later exp).
  - **Recommended**: Let Jul put expire or close for small profit. For CC, standard roll rules: at 21 DTE or 50% profit, roll to further OTM/higher strike or later month. Size more lots if adding shares on dips.
  - Watch: EV/magnesium demand news, commodity prices, any Magrathea updates. Low IV good entry for new legs.

### 3. F (Opportunistic — NO attachment)
- **No long shares currently**
- **Short Puts (CSP)**: Short 2x Jul10'26 $16.5 PUT @AMEX (collected low ~$0.557 avg!!) | Current premium $2.56 | **Unrealized P/L: -$386** (big loss) | IV ~43% | **Deep ITM** (stock $14.03, intrinsic ~$2.47), only ~22 DTE (expires soon Jul10).
- **Capital/Status**: High risk — likely assignment soon buying 200 shares @ effective ~$15.94 (strike - premium). Current price implies ~$1.91/share underwater if assigned (~$382 loss). Position is distressed.
- **Analysis & Recs**:
  - **Critical**: This is the problem child. Premium collected was too low relative to move; stock dropped hard or rolled poorly into ITM. Not attached — prioritize stopping the bleeding.
  - **Strongly Recommended Action**: **Close immediately** (buy to close the 2 puts at ~$2.56, accept ~$400 loss total). Frees capital/margin, avoids forced long 200 F shares at bad basis in opportunistic name. 
  - Alternative (if mildly bullish short-term): Let assign, then immediately sell OTM CCs on the new long shares to wheel out (recover via premium), but since "not attached at all", closing is cleaner and aligns with opportunistic mindset. Avoid rolling deep ITM (adds risk/capital).
  - Lesson for future: Better strike selection (delta 0.2-0.3 CSPs), avoid low premium collection on volatile names, or use defined risk if unsure.
  - Watch: Auto sales/EV transition news, but exit first.

### 4. SOFI (Opportunistic — NO attachment)
- **No long shares currently**
- **Short Puts (CSP)**: Short 2x Jul17'26 $17 PUT @AMEX (collected ~$0.863) | Current $0.74 | P/L +$23 | IV ~57% | Stock $17.77 slightly OTM, ~29 DTE. Buying power ~$3.4k. High OI/volume good liquidity.
- **Capital/Status**: Clean CSP, profitable so far. Good premium collection.
- **Analysis & Recs**:
  - Recent news: Strong Q1'26 results ($1.1B rev, $167M net income), launched SoFiUSD stablecoin (bullish for fintech moat/OCC charter), but mixed (charge-off concerns, tech platform client loss, short-seller?, unchanged guidance). Stock YTD -32% but rebounding (up 2% today, had pullbacks).
  - OTM put in decent IV environment: Solid. Can let to expiration (high prob OTM) or roll if dips toward $17 support.
  - **Recommended**: Monitor closely around any earnings or regulatory news. If 50% profit or 21 DTE, roll out/down or take profit. If assigned (possible if drops), since opportunistic: decide quickly — sell CC immediately or close shares if no thesis. No attachment = flexible exit.
  - Opportunity: If stock weakens more on news, can roll or add another leg at lower strike for income (opportunistic scaling).
  - Watch: Fintech regulation, member growth, charge-offs, crypto/stablecoin adoption news. YTD weakness may offer better entries for new CSPs.

## Other Notable Positions (Non-Wheel or Related)
- **SPX Jun24'26 Put Spread** (long 6x 7255p / short 6x 7320p): Defined risk, near expiration (6 DTE), volatile daily P/L (big swings). Manage/roll/close per your SPX analyzer tool. Not core wheel.
- **LEU Oct16'26 160 PUT** short 1x: Longer dated, perhaps thematic (uranium/nuclear — aligns with your AI power interest?). Check if wheel candidate or hedge.
- **ONDS Jul17'26 11 PUT** short 4x: Speculative/small, high risk name? Review thesis or close.
- **Long Stocks**: TSLA (34 sh), TSLR (3023 sh — ? leveraged/related), LLY (1), SGOV (~75k cash equiv for margin/liquidity), LMG (AU small).
- **Cash/Margin**: Limited cash ~$2.8k + SGOV; wheels use margin/buying power. Target scaling wheels to use ~half total buying power.

## Overall Recommendations & Action Plan
1. **Immediate (High Priority)**: Close or aggressively manage the **F Jul $16.5p** — accept loss to protect capital. This is dragging performance and ties up resources in non-core name.
2. **ABAT**: Roll short $3c calls to preserve long-term exposure. Add to position on dips if conviction high.
3. **TTI**: Strongest current wheel — let Jul put expire/take profit, actively roll/manage Sep CCs. Consider adding shares + more legs given thematic + profitable base.
4. **SOFI**: Ride or roll the CSP. Good liquidity; scale opportunistically on weakness but size small.
5. **Scaling to 50% Allocation**: Current wheel capital at risk modest (~$10-15k effective + margin). With ~$177k NAV, target $80-90k in wheels. Add 2-4 new underlyings with $10-20k each (e.g. 5-10 contracts depending price). Use your SPX analyzer style Monte Carlo for sizing/rolling sims.
6. **Risk Mgmt**: Track portfolio delta/theta exposure. Avoid correlated adds (e.g. more EV/materials). Set alerts for IV spikes, news, technical breaks. Use 30-delta or lower for CSPs on new names. Earnings avoidance or straddle hedge.
7. **New Opportunistic/Diverse Wheel Candidates** (scanned via market data + public 2026 wheel lists):
   - **AMD or NVDA** (High IV ~40%+ rank, AI/semicon cycle strong, liquid weeklies, user familiarity from prior wheels. Opportunistic high-premium; size carefully for vol. ~$150 range good capital efficiency).
   - **PLTR** (AI/data analytics, high interest/IV, liquid, growth story. Popular in 2026 wheel picks. Opportunistic.)
   - **SPY or QQQ** (Core/safe wheel for base income + accumulation. Low single-name risk, extremely liquid, "wheel for life" candidate per analysts. Lower IV but consistent premium + dividends. Ideal for larger allocation to hit 50% target stably.)
   - **XOM or CVX** (Energy, stagflation hedge, high yield + premium, diverse from current holdings. Good for multi-leg wheel.)
   - Others to scan: HOOD (fintech diversify from SOFI), MARA (crypto high IV but volatile), AAPL (blue chip stability).
   - **Process for scanning**: Filter liquid options (high OI/volume), IV percentile >30, price/support levels for strikes, upcoming events calendar (earnings.finance.yahoo or IBKR), sector diversification score. Use code/MonteCarlo for expected yield vs risk. I can help analyze specific tickers on request or build scanner tool.

## Next Steps & Tools Built
- **This doc maintained** as single source of truth for wheel positions (local + github sync).
- **GitHub Integration**: Added to your trading tools repo (djsmith1000/spx-put-credit-spread-analyzer) as reusable reference and starting point for wheel-specific modules. Can extend with Python wheel_analyzer.py (position tracker, roll simulator, IBKR data pull stubs via ib_insync or TWS API, new candidate screener). Mirrors structure of SPX analyzer (Monte Carlo projections, rolling logic, allocation vs reserves like SGOV).
- **Future Tools**:
  - Wheel position dashboard (Lovable.dev or Streamlit) pulling live IBKR data for P/L, approx Greeks, automated roll suggestions based on rules (delta, DTE, profit %, hold/opportunistic flag).
  - Automated market scanner: high IV rank + liquidity + earnings filter + thematic/opportunistic fit scoring.
  - Advanced rolling engine: inputs current pos details → suggested actions (expire/roll up-out-down/close/add pyramid).
- Update this file (local or GitHub) after any trades/rolls or weekly review. Share specific underlyings, roll candidates, or new ideas for deeper IBKR chain analysis or custom recs.

**Disclaimer**: Not financial advice. Options trading involves substantial risk of loss and is not suitable for all investors. Past performance no guarantee. Data snapshot ~Jun 18 2026; verify all live prices, IV, chains, and news in IBKR TWS before acting. Tax implications (Koinly for crypto/options), margin requirements, and personal risk tolerance apply. This is analysis aid only.

*Version controlled on GitHub for history, backup, and potential collaboration/extension.*