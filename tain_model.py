import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score,classification_report
import joblib

# Load data
X_train = pd.read_csv('data/X_train.csv')
X_test = pd.read_csv('data/X_test.csv')
y_train = pd.read_csv('data/y_train.csv').values.ravel()
y_test = pd.read_csv('data/y_test.csv').values.ravel()

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Make prediction
y_pred = model.predict(X_test)

# Evaluate model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save model and features
joblib.dump(model, 'model/churn_model.pkl')
joblib.dump(X_train.columns.tolist(), 'model/features.pkl')

print("Model saved successfully")

      