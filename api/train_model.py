import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# load dataset
df = pd.read_csv("FuelConsumption.csv")

# input/output
X = df[["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_COMB"]]
y = df["CO2EMISSIONS"]

# train model
model = LinearRegression()
model.fit(X, y)


# save model
with open("fuel_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully!")