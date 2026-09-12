# House Price Prediction — Machine Learning

## Project 2

Regression project based on the assigned Kaggle dataset:

https://www.kaggle.com/datasets/bhanupratapbiswas/house-price-prediction

### Goal
Build a regression model to predict house prices, with emphasis on:
- EDA
- missing-value handling
- feature engineering
- log transformations where appropriate
- categorical encoding
- numerical scaling
- model selection
- residual analysis

### Models
1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

### Evaluation
- RMSE
- MAE
- R²
- residual analysis

## Project structure

```text
house-price-prediction-machine-learning/
├── data/
│   ├── house_prices.csv          # Put the downloaded Kaggle CSV here
│   └── README.txt
├── models/
│   └── house_price_best_model.joblib   # Created after running the notebook
├── house_price_prediction.ipynb
├── inference.py
├── requirements.txt
└── README.md
```

## Setup

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
```

Open the notebook in VS Code with the Jupyter extension or run:

```bash
jupyter notebook house_price_prediction.ipynb
```

## Dataset setup

Download the dataset from the assigned Kaggle page and place the CSV at:

`data/house_prices.csv`

The notebook includes automatic target-column detection for common names. If it cannot detect the target, set `TARGET_COLUMN` manually near the beginning of the notebook.

## Model output

After the notebook runs, the best preprocessing + model pipeline is saved to:

`models/house_price_best_model.joblib`

## Prediction example

The notebook contains a prediction cell. `inference.py` demonstrates how to load the saved pipeline and predict a new house price.

> Important: The exact Kaggle CSV must be supplied before model metrics and the trained model can be generated. No substitute dataset is silently used.
