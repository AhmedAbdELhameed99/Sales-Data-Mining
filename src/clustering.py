"""
Customer Segmentation using KMeans
- aggregates by Customer ID
- scales features
- fits KMeans and saves labels + model
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from joblib import dump
from utils import ensure_dirs, load_data, save_df

def main(n_clusters=4, random_state=42):
    ensure_dirs()
    df = load_data()

    # Required columns
    group_cols = ["Customer ID"]
    if "Customer ID" not in df.columns:
        raise SystemExit("Column 'Customer ID' not found in data.")

    # Aggregate features per customer
    agg = df.groupby("Customer ID").agg({
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    }).fillna(0)

    # If data sparse, drop zero-sum customers
    agg = agg.loc[~((agg["Sales"]==0) & (agg["Profit"]==0) & (agg["Quantity"]==0))]

    # Scale
    scaler = StandardScaler()
    X = scaler.fit_transform(agg)

    # Fit KMeans
    km = KMeans(n_clusters=n_clusters, random_state=random_state, n_init=10)
    labels = km.fit_predict(X)
    agg["cluster"] = labels

    # Save outputs
    agg.to_csv("outputs/customer_clusters.csv")
    dump(km, "outputs/kmeans_model.joblib")
    dump(scaler, "outputs/scaler.joblib")
    print("Saved outputs/customer_clusters.csv, kmeans_model.joblib, scaler.joblib")

    # Basic cluster profiling
    profile = agg.groupby("cluster").agg({
        "Sales":"mean","Profit":"mean","Quantity":"mean","cluster":"size"
    }).rename(columns={"cluster":"count"})
    profile.to_csv("outputs/cluster_profile.csv")
    print("Saved outputs/cluster_profile.csv")
    print(profile)

if __name__ == "__main__":
    main()