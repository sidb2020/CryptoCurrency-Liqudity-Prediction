# CryptoCurrency Liquidity Prediction

This project predicts the **liquidity level** of cryptocurrencies using market data from CoinGecko. It helps identify coins with high or low liquidity for better investment and risk decisions.

---

## Project Objective

To build a machine learning model that classifies cryptocurrencies into **High**, **Medium**, or **Low Liquidity** based on features like:

- Total Volume  
- Market Cap  
- Price Volatility  
- Price Change %

---

## Folder Structure

```

cryptocurrency\_liquidity\_project/
├── app\_ml\_project\_sid.py                      # Streamlit web app for predictions
├── data\_preparation\_ml\_project\_sid.py        # Merges & cleans input data
├── feature\_engineering\_ml\_project\_sid.py     # Creates liquidity-related features
├── model\_training\_ml\_project\_sid.py          # Trains ML model
├── models/
│   ├── trained\_model.pkl      # Saved model
│   └── scaler.pkl             # Scaler for input normalization
├── data/
│   ├── coin\_gecko\_2022-03-16.csv
│   ├── coin\_gecko\_2022-03-17.csv
│   ├── merged\_cleaned\_crypto\_data.csv
│   └── engineered\_crypto\_data.csv
├── reports/
│   ├── EDA\_Report.pdf
│   ├── HLD.pdf
│   ├── LLD.pdf
│   ├── Final_Report.pdf
│   ├── pipeline_architecture.png
│   └── pipeline_architecture_doc.txt
├── requirements.txt
└── README.md

````

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/sidb2020/cryptocurrency-liquidity-prediction.git
cd cryptocurrency-liquidity-prediction
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

```bash
streamlit run app_ml_project_sid.py
```

---

## Features Used

* `liquidity_ratio = total_volume / market_cap`
* `price_change_ratio = price_change_percentage_24h / current_price`
* `cap_per_supply = market_cap / circulating_supply`
* `volatility_range = high_24h - low_24h` (if available)

---

## Model Used

* **Random Forest Classifier**
* Accuracy: \~87%
* F1-Score: \~0.85

---

## Dependencies

Listed in `requirements.txt`:

* pandas
* numpy
* scikit-learn
* joblib
* streamlit
* matplotlib
* seaborn
* xgboost

---

## Reports

All documentation is inside `/reports/`:

* EDA Report
* High-Level Design (HLD)
* Low-Level Design (LLD)
* Final Report
* Pipeline Architecture

---

## Credits

Data source: [CoinGecko](https://www.coingecko.com/)
Project by **\[Siddharth Banerjee]** as part of the ML assignment.
