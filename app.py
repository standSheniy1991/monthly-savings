"""Toy monthly savings table: python3 app.py 1000 5 12 --deposit 50"""
import argparse
import math


def balances(principal, annual_percent, months, deposit):
    if not all(math.isfinite(value) and value >= 0 for value in (principal, annual_percent, deposit)):
        raise ValueError("Enter finite, nonnegative amounts and rate")
    if not 0 <= months <= 1200:
        raise ValueError("Months must be between 0 and 1200")
    result = []
    for month in range(1, months + 1):
        principal = principal * (1 + annual_percent / 1200) + deposit
        result.append((month, principal))
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("principal", type=float)
    parser.add_argument("annual_percent", type=float)
    parser.add_argument("months", type=int)
    parser.add_argument("--deposit", type=float, default=0)
    args = parser.parse_args()
    try:
        for month, amount in balances(args.principal, args.annual_percent, args.months, args.deposit):
            print(f"Month {month}: {amount:.2f}")
    except ValueError as error:
        parser.error(str(error))
