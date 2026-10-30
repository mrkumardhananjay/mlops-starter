"Train the delivery model and save it to model.joblib."
import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

FEATURES = ["distance_km", "prep_time_min", "traffic_level", "rain"]

orders = pd.read_csv("data.csv")
X_train, X_test, y_train, y_test = train_test_split(
    orders[FEATURES], orders["delivery_min"], test_size=0.2, random_state=42)

model = LinearRegression().fit(X_train, y_train)
mae = mean_absolute_error(y_test, model.predict(X_test))
print("trained on", len(X_train), "orders, tested on", len(X_test))
print("minutes per unit:", {f: round(float(c), 2) for f, c in zip(FEATURES, model.coef_)})
print(f"MAE on unseen orders: {mae:.2f} minutes")

joblib.dump(model, "model.joblib")
print("saved model.joblib")
