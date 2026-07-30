import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/phishing_dataset.csv")

# Input and Output
X = data["URL"]
y = data["Label"]

# Convert URLs into numbers
vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

# Train AI model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_vector, y)

# Save the model
joblib.dump(model, "model/phishing_model.pkl")

# Save the vectorizer
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ AI Model Trained Successfully!")
print("Files Created:")
print(" - phishing_model.pkl")
print(" - vectorizer.pkl")