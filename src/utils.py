import os
import pandas as pd

def ensure_dirs():
    os.makedirs("outputs", exist_ok=True)
    os.makedirs("outputs/figures", exist_ok=True)

def load_data(path=r"D:\sales data mining\data\Sales Overview Data.xlsx", sheet_name="Sales Data"):
    df = pd.read_excel(path, sheet_name=sheet_name, engine="openpyxl")
    for col in ["Order Date", "Ship Date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

def save_df(df, name):
    df.to_csv(name, index=False)