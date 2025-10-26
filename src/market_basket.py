"""
Market Basket Analysis (Apriori)
- builds transaction matrix from Order ID x Sub-Category
- runs apriori and association rules (lift)
"""
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from utils import ensure_dirs, load_data, save_df

def main(min_support=0.01, min_threshold=1):
    ensure_dirs()
    df = load_data()

    if not {"Order ID", "Sub-Category"}.issubset(df.columns):
        raise SystemExit("Columns 'Order ID' and/or 'Sub-Category' not found.")

    # Build basket: one-hot encoded transactions
    basket = (df.groupby(["Order ID", "Sub-Category"])["Quantity"]
              .sum().unstack().fillna(0))

    # Convert to 0/1
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)

    # Frequent itemsets
    frequent = apriori(basket, min_support=min_support, use_colnames=True)
    frequent.to_csv("outputs/frequent_itemsets.csv", index=False)
    print(f"Found {len(frequent)} frequent itemsets (support>={min_support})")

    # Rules
    rules = association_rules(frequent, metric="lift", min_threshold=min_threshold)
    rules = rules.sort_values(["lift","confidence"], ascending=False)
    rules.to_csv("outputs/association_rules.csv", index=False)
    print("Saved outputs/association_rules.csv")

if __name__ == "__main__":
    main()