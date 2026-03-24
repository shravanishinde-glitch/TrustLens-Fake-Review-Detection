import joblib

model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Test reviews
test_reviews = [
    "This product is amazing, I love it!",
    "Terrible product, complete waste of money",
    "Great quality and fast shipping",
    "Fake review, don't buy this junk"
]

for review in test_reviews:
    review_vec = vectorizer.transform([review])
    prediction = model.predict(review_vec)
    print(f"Review: '{review}'")
    print(f"Prediction: {prediction[0]}")
    print("---")
