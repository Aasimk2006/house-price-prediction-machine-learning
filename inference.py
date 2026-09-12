"""Inference example for the trained house-price pipeline."""
import joblib
import pandas as pd

MODEL_PATH = "models/house_price_best_model.joblib"
model = joblib.load(MODEL_PATH)

# Replace this example with the exact feature columns from your dataset.
# The notebook demonstrates inference using a real test row.
new_house = pd.DataFrame([{
    # "feature_1": value,
    # "feature_2": value,
}])

prediction = model.predict(new_house)
print("Predicted house price:", prediction[0])
