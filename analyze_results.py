import os
import csv
import sys

def main():
    filepath = os.path.join(os.path.dirname(__file__), "backtest", "results", "backtest_summary.csv")
    if not os.path.exists(filepath):
        print("Summary not found.")
        return

    print("| Symbol | Trades | Win% | Max DD% | Liq. Risk | Profit Factor | x20 PnL ($) | Proj. Monthly ($) |")
    print("|--------|--------|------|---------|-----------|---------------|-------------|-------------------|")
    
    total_trades = 0
    total_pnl = 0
    
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["symbol"].startswith("TOTAL") or not row["total_trades"]:
                continue
                
            trades = int(row["total_trades"])
            if trades == 0:
                continue
                
            win_rate = float(row["win_rate"])
            pnl = float(row["total_pnl"])
            dd = float(row["max_drawdown"])
            pf = float(row["profit_factor"])
            
            monthly = pnl / 12.0
            
            # Liquidation Risk heuristic based on max drawdown
            if dd > 5.0:
                liq_risk = "High"
            elif dd > 2.5:
                liq_risk = "Medium"
            else:
                liq_risk = "Low"
            
            print(f"| {row['symbol']:<6} | {trades:<6} | {win_rate:>4.1f}% | {dd:>6.2f}% | {liq_risk:<9} | {pf:>13.2f} | {pnl:>11.2f} | {monthly:>17.2f} |")
            
            total_trades += trades
            total_pnl += pnl

    total_monthly = total_pnl / 12.0
    print(f"| **TOTAL**| **{total_trades}** | **-** | **-** | **-** | **-** | **${total_pnl:.2f}** | **${total_monthly:.2f}** |")

if __name__ == "__main__":
    main()
