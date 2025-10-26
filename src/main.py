from utils import ensure_dirs, load_data
from analysis import basic_analysis, descriptive_stats
from clustering import clustering_analysis
from market_basket import market_basket_analysis
from regression import regression_analysis
from forecasting import forecasting

def main():
    ensure_dirs()
    df = load_data()
    basic_analysis(df)
    descriptive_stats(df)
    clustering_analysis(df)
    market_basket_analysis(df)
    regression_analysis(df)
    forecasting(df)

if __name__ == "__main__":
    main()