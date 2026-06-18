# Wheel Strategy Portfolio Summary & Analysis
**Updated:** 2026-06-18 (IBKR live data, with LEU/ONDS correction) | **Account NAV ~$177k long** | **Target: ~50% allocated to wheel positions** (currently under-allocated)

## Core Philosophy (per user prefs + correction)
- **Long-term holds / Accumulation** (strong bias to maintain exposure): ABAT (battery recycling bullish), TTI (magnesium thixomolding + EV + Magrathea partnership bullish).
- **Moderate Hold Interest** (willing to accept assignment and wheel/hold shares moderately; prefer rolls that preserve some exposure over panic closes): LEU (uranium/nuclear thematic, aligns with AI power interest), ONDS (speculative high-vol small-cap).
- **Opportunistic** (no attachment — prioritize capital preservation, quick closes or flexible exits): F, SOFI (and future adds). Willing to exit entirely if thesis breaks or losses mount.
- **Advanced Wheel Mgmt**: Multi-leg (CSP + CC where applicable), rolling based on delta/IV/profit targets (e.g. 50% profit take or roll at 21-30 DTE), factor in vol (IV rank/percentile), news catalysts, technical support levels, portfolio correlation/heat, earnings calendar. Differentiate by hold type for strike selection, size, and assignment tolerance.
- **Risk/Allocation**: Aim for ~half IBKR capital in wheels (diverse underlyings, position sizing by IV & conviction). Use defined-risk where possible or size CSPs conservatively. Monitor overall Greeks exposure, assignment risk, and margin.
- **Scanning for New**: High liquidity options, IV rank >30-50% preferred for premium, price $5-150, no major earnings in next 2-4 wks or plan around, good volume/OI, diverse sectors from current. Balance high-IV opportunistic/moderate with lower-IV core like SPY/QQQ for stability.

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

### 5. LEU (Moderate Hold Interest — Uranium/Nuclear thematic)
- **No long shares currently**
- **Short Puts (CSP)**: Short 1x Oct16'26 $160 PUT @AMEX (collected ~$25.75) | Current ~$26.15 | Slight unrealized loss | IV ~88% ann. | Stock ~$189.20 (strong +11% today, YTD -22%), OTM put (good ~$29 buffer), long ~120 DTE. HV ~78% ann., low-moderate IV percentile.
- **Capital/Status**: Longer-dated CSP on volatile name. Buying power ~$16k. Clean OTM position with solid time value. High liquidity potential.
- **Analysis & Recs**:
  - Strong thematic fit (Centrus Energy — uranium enrichment for nuclear/AI data center power; aligns with your AI power/nuclear interest). Moderate hold interest means **prefer to maintain some exposure** if assigned (e.g., sell CCs on shares rather than immediate exit).
  - OTM with long DTE and high IV: Excellent wheel candidate. Premium collection potential strong over months.
  - **Recommended Action**: Let ride or roll closer to expiry (or on dips) if premium attractive — roll out/up or adjust to maintain desired delta/exposure. If assigned on a dip, **wheel it**: sell OTM CCs on the long shares to generate income while holding moderately per your interest level. Size (1 contract) fits moderate conviction well.
  - Watch: Nuclear policy, uranium prices, AI power demand news (significant tailwind potential). High vol supports premium selling; long DTE gives flexibility.
  - Multi-level potential: Good candidate for adding more puts on weakness or layering CCs post-assignment.

### 6. ONDS (Moderate Hold Interest — Speculative high-vol small-cap)
- **No long shares currently**
- **Short Puts (CSP)**: Short 4x Jul17'26 $11 PUT @AMEX (collected ~$0.977 avg) | Current ~$2.22 | **Unrealized loss ~-$499** | IV ~87-92% ann. | Stock ~$9.04 (slightly down today, YTD -7.4%), ITM put (intrinsic ~$1.96), ~29 DTE. Very high HV ~111% ann., low IV percentile. High OI/volume.
- **Capital/Status**: Short-term CSP now ITM with loss (distress similar to F, but moderate hold changes management). Buying power ~$4.4k.
- **Analysis & Recs**:
  - High-vol speculative name (Ondas Holdings — rail/drone/automation tech?). Moderate hold interest: **willing to accept assignment and hold/wheel shares moderately** rather than close at full loss like pure opportunistic.
  - Currently ITM with premium pressure: Risk of assignment in ~29 days (or sooner if drops more). Loss position but high IV environment offers recovery via premium.
  - **Recommended Action**: **Prefer roll** (to later expiration/lower strike for net credit or better risk management) **or let assign and immediately wheel** (sell CCs on new long 400 shares to recover via premium and hold per moderate interest). Avoid outright close at large loss unless thesis is fully broken — moderate interest supports giving it a chance through assignment + covered call income. If rolling, target manageable delta/OTM where possible.
  - Watch: Company-specific news, rail/tech/automation sector catalysts, small-cap/high-vol sentiment. Note: 4-contract size was aggressive for this volatility — consider scaling down on future rolls or adds.
  - Lesson for moderate-hold names: ITM situations favor assignment + wheel (or patient roll) over panic close, to align with willingness to hold somewhat.

## Other Notable Positions (Non-Wheel or Related)
- **SPX Jun24'26 Put Spread** (long 6x 7255p / short 6x 7320p): Defined risk, near expiration (6 DTE), volatile daily P/L (big swings). Manage/roll/close per your SPX analyzer tool. Not core wheel.
- **Long Stocks**: TSLA (34 sh), TSLR (3023 sh — ? leveraged/related), LLY (1), SGOV (~75k cash equiv for margin/liquidity), LMG (AU small).
- **Cash/Margin**: Limited cash ~$2.8k + SGOV; all wheels use margin/buying power. Target scaling total wheels to use ~half overall buying power while respecting hold-type differences.

## Overall Recommendations & Action Plan (Updated with LEU/ONDS)
1. **Immediate (High Priority)**: Close or aggressively manage the **F Jul $16.5p** — accept loss to protect capital (pure opportunistic). For **ONDS** (moderate hold), prioritize roll or assign+wheel instead of close.
2. **ABAT/TTI (Long-term)**: Roll short calls (ABAT) or manage CCs (TTI) to preserve exposure. Strongest current setups.
3. **LEU (Moderate)**: Excellent longer-term wheel — ride/roll OTM CSP. Plan for post-assignment CC wheel if triggered. Thematic alignment strong.
4. **ONDS (Moderate)**: Manage ITM situation via roll or assign+immediate CC wheel to recover and hold moderately. Avoid F-style close.
5. **SOFI (Opportunistic)**: Ride or roll CSP flexibly.
6. **Scaling to 50% Allocation**: Current wheel capital modest. With ~$177k NAV, target $80-90k across all wheel types (differentiated sizing: larger/more patient for long-term & moderate like LEU; smaller/flexible for opportunistic). Add 2-4 new underlyings. Use SPX analyzer-style Monte Carlo for sizing/rolling sims per hold type.
7. **Risk Mgmt**: Track portfolio delta/theta, correlated moves (e.g., materials for ABAT/TTI; high-vol for ONDS). Set alerts for IV spikes, news, technical breaks. Use hold-type-specific rules (longterm/moderate = bias to rolls/assignment+wheel; opportunistic = faster exits). Earnings avoidance or hedges.
8. **New Opportunistic/Diverse Wheel Candidates** (scanned via market data + public 2026 wheel lists; consider moderate-hold potential too):
   - **AMD or NVDA** (High IV AI/semicon, liquid, prior familiarity — opportunistic or moderate).
   - **PLTR** (AI growth, high interest/IV — opportunistic/moderate).
   - **SPY or QQQ** (Core stable wheel for base income + accumulation — long-term style ballast to hit 50% target).
   - **XOM or CVX** (Energy diversification, premium + dividend — moderate or opportunistic).
   - Others: HOOD (fintech), MARA (crypto high IV), or nuclear-adjacent names to complement LEU.
   - **Process**: Filter liquid options (high OI/volume), IV percentile >30, price/support for strikes, events calendar, sector diversity, and thematic fit (e.g., nuclear/AI power for moderate holds). I can analyze specific tickers or build enhanced scanner.

## Next Steps & Tools Built
- **This doc maintained** as single source of truth (local + GitHub sync). Updated with LEU/ONDS as moderate-hold wheels, detailed analysis, recs, and integration into overall plan.
- **GitHub Integration**: Updated `WHEEL_POSITIONS_ANALYSIS.md` and `wheel_analyzer.py` in djsmith1000/spx-put-credit-spread-analyzer with the correction, new sections for LEU/ONDS, hold-type differentiated logic in the rule engine, and example data including them. The Python scaffold now handles long-term / moderate / opportunistic distinctions in recommendations.
- **Future Tools**: Extend wheel_analyzer.py with full IBKR integration, BS greeks/delta for precise rolling, Monte Carlo per hold type, earnings/news filters, and dashboard export. Add LEU/ONDS-specific modules (e.g., nuclear catalyst scanner). I can iterate on code or add features on request.

**Disclaimer**: Not financial advice. Options involve substantial risk of loss. Data as of ~Jun 18 2026; verify live in TWS/IBKR before acting. Tax (Koinly), margin, and personal risk tolerance apply. This is analysis and tooling support only.

*Version controlled on GitHub for history and extension. LEU/ONDS now properly classified per your correction — moderate hold changes management (rolls/assignment+wheel preferred over closes where possible).*