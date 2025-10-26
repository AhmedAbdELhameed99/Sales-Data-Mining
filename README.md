# 📊 Sales Data Mining & Forecasting Project

### 🔍 Project Overview
This project performs **end-to-end sales analytics and data mining** to uncover **patterns, drivers, and predictive insights** from transaction data.

It covers:
- 📈 Exploratory Data Analysis (EDA)
- 👥 Customer Segmentation (KMeans)
- 🧮 Profit Regression (OLS)
- 🧺 Market Basket Analysis (Apriori)
- 🔮 Sales Forecasting (Prophet)

The goal is to help business teams understand **what drives profit**, **which products are related**, **how to segment customers**, and **how sales will evolve over time**.

---

## 🧱 Project Structure

```
sales-data-mining/
│
├── data/
│   └── Sales Overview Data.xlsx                # Original dataset
│
├── outputs/
│   ├── figures/                               # Plots and visual outputs
│   ├── forecast.csv                           # Prophet forecast data
│   ├── regression_summary.txt                 # Regression results
│   ├── association_rules.csv                  # Market basket rules
│   ├── customer_clusters.csv                  # KMeans clustering output
│   ├── cluster_profile.csv                    # Cluster profiling summary
│   ├── monthly_sales.csv                      # Time-series aggregation
│   └── numeric_description.csv                # Descriptive statistics
│
├── src/
│   ├── utils.py                               # Helper functions (load/save/dirs)
│   ├── analysis.py                            # EDA & summary statistics
│   ├── clustering.py                          # Customer segmentation (KMeans)
│   ├── regression.py                          # Profit regression (OLS)
│   ├── market_basket.py                       # Association rule mining (Apriori)
│   └── forecasting.py                         # Prophet sales forecasting
```

---

## ⚙️ Step-by-Step Workflow

### 1️⃣ Data Preparation (`utils.py`)
- Loads Excel dataset  
- Converts date columns to datetime  
- Creates output directories (`outputs/`, `outputs/figures/`)  
- Saves processed data consistently across scripts  

➡️ **Output:** Clean, ready-to-analyze dataset

---

### 2️⃣ Exploratory Data Analysis (`analysis.py`)
Performs initial exploration and visualization:
- Summary statistics (`describe()`)
- Missing values check  
- Correlation heatmap  
- Monthly sales trend visualization  

🗂️ **Outputs:**  
- `numeric_description.csv`  
- `correlation.png`  
- `monthly_sales.png`

📊 **Key Findings:**
- Average Sale ≈ 229  
- Profit highly correlated with Sales  
- “West” region & “Office Supplies” dominate  
- No major missing data

---

### 3️⃣ Customer Segmentation (`clustering.py`)
Applies **KMeans** clustering on aggregated customer metrics.

| Feature | Description |
|----------|-------------|
| Sales | Total spend per customer |
| Profit | Total profit generated |
| Quantity | Number of units bought |

**Results:**
| Cluster | Avg Sales | Avg Profit | Avg Quantity | Customers |
|----------|------------|-------------|---------------|------------|
| 0 | 3655.6 | 507.6 | 67.6 | 278 |
| 1 | 1426.9 | 144.3 | 30.8 | 446 |
| 2 | 9328.6 | 2373.6 | 76.5 | 53 |
| 3 | 6600.5 | -1942.2 | 61.0 | 23 |

📈 **Insights:**
- Cluster 2 → **High-value customers**
- Cluster 3 → **Unprofitable segment**
- Cluster 1 → **Low spenders**

---

### 4️⃣ Profit Regression (`regression.py`)
Builds a linear regression model:
\[
Profit = β_0 + β_1(Sales) + β_2(Discount) + β_3(Quantity)
\]

**Key Results:**
| Variable | Coefficient | Impact |
|-----------|--------------|---------|
| Sales | +0.18 | Profit increases with sales |
| Discount | -232.7 | High discount = major loss |
| Quantity | -2.93 | Minor negative effect |
| R² | 0.273 | Model explains 27% of variation |

📘 **Interpretation:**
Discount is the strongest negative driver of profit → pricing strategy optimization needed.

---

### 5️⃣ Market Basket Analysis (`market_basket.py`)
Uses **Apriori algorithm** to identify frequently co-purchased items.

| Antecedent | Consequent | Confidence | Lift |
|-------------|-------------|-------------|------|
| Binders + Paper | Storage | 19.3% | 1.25 |
| Fasteners | Paper | 27% | 1.15 |
| Appliances | Binders | 28.8% | 1.09 |

📈 **Insights:**
- Office supplies tend to be bought together  
- Suggest bundling “Binders + Paper + Storage”  
- Lift > 1 confirms true behavioral relationships

---

### 6️⃣ Sales Forecasting (`forecasting.py`)
Forecasts next **90 days** of daily sales using **Prophet**.

| Month | Trend |
|--------|--------|
| January 2025 | Stable (1k–2.3k) |
| February 2025 | Slight decline (~1.2k) |
| March 2025 | Upward trend (~3k–3.2k) |

📊 **Outputs:**
- `forecast.csv`
- `forecast_plot.png`
- `forecast_components.png`

💡 **Interpretation:**  
Steady recovery and sales growth expected through March 2025.

---

## 🧮 Technical Stack

| Category | Tools |
|-----------|--------|
| Language | Python 3.11 |
| Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| ML Models | Scikit-learn, Prophet, mlxtend |
| Statistical Modeling | Statsmodels |
| Data Source | Excel (.xlsx) |

---

## 🚀 How to Run

```bash
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/sales-data-mining.git
cd sales-data-mining

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run individual scripts
python src/analysis.py
python src/clustering.py
python src/regression.py
python src/market_basket.py
python src/forecasting.py
```
