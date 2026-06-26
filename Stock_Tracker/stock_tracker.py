"""
Stock Portfolio Tracker - CodeAlpha Python Internship Task 2
Author: Qasir Nawaz
Pakistani Mobile Market Prices (PKR)
"""

import csv
import os
from datetime import datetime

# Mobile prices in PKR (Pakistani Rupees) - Popular phones in Pakistan
STOCK_PRICES = {
    "APPLE":    125000,   # Apple iPhone 15 Pro
    "SAMSUNG":   40000,   # Samsung Galaxy A35
    "XIAOMI":    28000,   # Xiaomi Redmi 13C
    "OPPO":      35000,   # Oppo A38
    "VIVO":      30000,   # Vivo Y18
    "NOKIA":     15000,   # Nokia C32
    "SONY":      50000,   # Sony Xperia 10 VI
    "TECHNO":    18000,   # Techno Spark 20C
    "INFINIX":   22000,   # Infinix Hot 40i
    "REALME":    25000,   # Realme C55
}

COMPANIES = {
    "APPLE":   "Apple iPhone 15 Pro",
    "SAMSUNG": "Samsung Galaxy A35",
    "XIAOMI":  "Xiaomi Redmi 13C",
    "OPPO":    "Oppo A38",
    "VIVO":    "Vivo Y18",
    "NOKIA":   "Nokia C32",
    "SONY":    "Sony Xperia 10 VI",
    "TECHNO":  "Techno Spark 20C",
    "INFINIX": "Infinix Hot 40i",
    "REALME":  "Realme C55",
}


def show_available_stocks():
    print("\n📱 Pakistani Mobile Market Prices (PKR):")
    print("-" * 50)
    print(f"{'Symbol':<10} {'Model':<25} {'Price (PKR)':>12}")
    print("-" * 50)
    for symbol, price in STOCK_PRICES.items():
        model = COMPANIES.get(symbol, "")
        print(f"{symbol:<10} {model:<25} Rs.{price:>9,}")
    print("-" * 50)


def get_portfolio():
    portfolio = {}
    print("\nApne phones enter karo. 'done' type karo jab khatam ho.")

    while True:
        symbol = input("\nPhone symbol (e.g. SAMSUNG): ").upper().strip()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print(f"⚠  '{symbol}' nahi mila. Available: {', '.join(STOCK_PRICES.keys())}")
            continue

        try:
            qty = int(input(f"Quantity of {symbol}: "))
            if qty <= 0:
                print("⚠  Quantity positive honi chahiye.")
                continue
        except ValueError:
            print("⚠  Sirf number daalo.")
            continue

        if symbol in portfolio:
            portfolio[symbol] += qty
        else:
            portfolio[symbol] = qty

    return portfolio


def display_portfolio(portfolio):
    if not portfolio:
        print("\n⚠  Portfolio khali hai.")
        return 0

    total = 0
    W = 72
    print("\n" + "=" * W)
    print("           📊 AAPKA MOBILE PORTFOLIO SUMMARY (PKR)")
    print("=" * W)
    print(f"  {'#':<4} {'Symbol':<10} {'Model':<24} {'Qty':^6} {'Price (PKR)':>12} {'Value (PKR)':>12}")
    print("-" * W)

    for i, (symbol, qty) in enumerate(portfolio.items(), 1):
        price = STOCK_PRICES[symbol]
        model = COMPANIES.get(symbol, "")
        value = price * qty
        total += value
        print(f"  {i:<4} {symbol:<10} {model:<24} {qty:^6} {price:>12,} {value:>12,}")

    print("-" * W)
    print(f"  {'TOTAL INVESTMENT':<56} {total:>12,}")
    print("=" * W)
    return total


def save_to_csv(portfolio, total):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Symbol", "Model", "Quantity", "Price (PKR)", "Total Value (PKR)"])
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            model = COMPANIES.get(symbol, "")
            value = price * qty
            writer.writerow([symbol, model, qty, price, value])
        writer.writerow([])
        writer.writerow(["", "", "", "TOTAL", total])
    print(f"\n✅ Portfolio save ho gaya: '{filename}'")


def save_to_txt(portfolio, total):
    filename = f"portfolio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        f.write("MOBILE PORTFOLIO REPORT (PKR)\n")
        f.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 50 + "\n")
        for symbol, qty in portfolio.items():
            price = STOCK_PRICES[symbol]
            model = COMPANIES.get(symbol, "")
            value = price * qty
            f.write(f"{symbol} ({model}): {qty} x Rs.{price:,} = Rs.{value:,}\n")
        f.write("=" * 50 + "\n")
        f.write(f"TOTAL: Rs.{total:,}\n")
    print(f"✅ Portfolio save ho gaya: '{filename}'")


def main():
    print("=" * 55)
    print("   📱 MOBILE PORTFOLIO TRACKER (PKR) - CodeAlpha")
    print("=" * 55)

    show_available_stocks()
    portfolio = get_portfolio()
    total = display_portfolio(portfolio)

    if portfolio:
        save = input("\nPortfolio save karo? (csv / txt / no): ").lower().strip()
        if save == "csv":
            save_to_csv(portfolio, total)
        elif save == "txt":
            save_to_txt(portfolio, total)
        else:
            print("Portfolio save nahi hua.")

    print("\nShukriya! Mobile Portfolio Tracker use karne ka! 📱")


if __name__ == "__main__":
    main()