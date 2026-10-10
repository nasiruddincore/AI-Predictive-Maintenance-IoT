import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

print("🧠 Training Predictive Maintenance ML Model...")
df = pd.read_csv('data/sensor_telemetry.csv')

X = df[['temperature', 'vibration', 'current']]
y = df['failure']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("\n📊 Model Evaluation Metrics:")
print(classification_report(y_test, model.predict(X_test)))

os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/predictive_model.pkl')
print("✅ Success: Model saved as models/predictive_model.pkl")