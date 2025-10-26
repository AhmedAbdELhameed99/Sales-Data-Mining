"""
Forecasting sales using Prophet
- aggregates sales by date (daily) then fits Prophet
- outputs forecast CSV and plot
"""
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
from utils import ensure_dirs, load_data

def main(periods=90, freq='D'):
    ensure_dirs()
    df = load_data()
    if "Order Date" not in df.columns or "Sales" not in df.columns:
        raise SystemExit("Required columns 'Order Date' or 'Sales' not found.")

    # Aggregate to daily sales (or monthly if you prefer)
    sales = df.groupby("Order Date")["Sales"].sum().reset_index()
    sales = sales.rename(columns={"Order Date":"ds", "Sales":"y"})
    sales = sales.dropna()

    # Minimal requirement: at least a few periods
    if sales.shape[0] < 30:
        print("Warning: too few time points for reliable forecasting")

    m = Prophet(daily_seasonality=True)
    m.fit(sales)

    future = m.make_future_dataframe(periods=periods, freq=freq)
    forecast = m.predict(future)
    forecast[["ds","yhat","yhat_lower","yhat_upper"]].to_csv("outputs/forecast.csv", index=False)
    print("Saved outputs/forecast.csv")

    # Plot
    fig = m.plot(forecast)
    fig.savefig("outputs/figures/forecast_plot.png")
    plt.close(fig)
    # Components (trend/seasonality)
    fig2 = m.plot_components(forecast)
    fig2.savefig("outputs/figures/forecast_components.png")
    plt.close(fig2)
    print("Saved outputs/figures/forecast_plot.png and forecast_components.png")

if __name__ == "__main__":
    main()