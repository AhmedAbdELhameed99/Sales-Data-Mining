"""
Regression analysis: model Profit as function of Sales, Discount, Quantity
- uses statsmodels OLS
- saves summary text
"""
import pandas as pd
import statsmodels.api as sm
from utils import ensure_dirs, load_data

def main():
    ensure_dirs()
    df = load_data()

    # Ensure required columns
    req = ["Profit", "Sales", "Discount", "Quantity"]
    for c in req:
        if c not in df.columns:
            raise SystemExit(f"Required column missing: {c}")

    df_model = df[req].dropna()
    # Filter extreme outliers if needed (optional)
    # df_model = df_model[(df_model['Sales'] < df_model['Sales'].quantile(0.99))]

    X = df_model[["Sales", "Discount", "Quantity"]]
    y = df_model["Profit"]

    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    summary_text = model.summary().as_text()
    with open("outputs/regression_summary.txt", "w", encoding="utf-8") as f:
        f.write(summary_text)
    print("Saved outputs/regression_summary.txt")
    print(model.summary())

if __name__ == "__main__":
    main()