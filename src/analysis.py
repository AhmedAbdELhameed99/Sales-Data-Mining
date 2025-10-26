import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from utils import ensure_dirs, load_data, save_df

def main():
    ensure_dirs()
    df = load_data()

    # Basic numeric summary
    numeric_cols = ["Sales", "Profit", "Quantity", "Discount"]
    present_numeric = [c for c in numeric_cols if c in df.columns]
    print("Descriptive statistics for:", present_numeric)
    desc = df[present_numeric].describe()
    print(desc)
    save_df(desc.reset_index(), "outputs/numeric_description.csv")

    # Missing values
    miss = df.isna().sum().sort_values(ascending=False)
    print("\nMissing values:\n", miss.head(20))

    # Categorical summaries (top values)
    cat_cols = [c for c in ["Region","Category","Sub-Category","Ship Mode","City","State/Province","Country/Region","Segment"] if c in df.columns]
    cat_summary = {}
    for c in cat_cols:
        cat_summary[c] = df[c].value_counts().head(20)
        print(f"\nTop values for {c}:\n", cat_summary[c].head())
        cat_summary[c].to_csv(f"outputs/top_{c.replace('/','_')}.csv")

    # Correlation heatmap
    if len(present_numeric) >= 2:
        corr = df[present_numeric].corr()
        corr.to_csv("outputs/correlation.csv")
        plt.figure(figsize=(6,5))
        sns.heatmap(corr, annot=True, fmt=".2f")
        plt.title("Correlation matrix")
        plt.tight_layout()
        plt.savefig("outputs/figures/correlation.png")
        plt.close()
        print("Saved outputs/figures/correlation.png")

    # Time series: monthly sales
    if "Order Date" in df.columns and "Sales" in df.columns:
        ts = df.set_index("Order Date")["Sales"].resample("M").sum()
        ts.to_csv("outputs/monthly_sales.csv")
        plt.figure(figsize=(10,4))
        ts.plot()
        plt.title("Monthly Sales")
        plt.ylabel("Sales")
        plt.tight_layout()
        plt.savefig("outputs/figures/monthly_sales.png")
        plt.close()
        print("Saved outputs/monthly_sales.csv and outputs/figures/monthly_sales.png")

if __name__ == "__main__":
    main()