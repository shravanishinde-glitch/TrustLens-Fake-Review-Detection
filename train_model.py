import pandas as pd
import nltk
import string
import joblib
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Try to download stopwords, but continue if it fails (e.g., no internet)
try:
    nltk.download('stopwords', quiet=True)
    stop_words = set(stopwords.words('english'))
except:
    # Fallback: use a basic set of common stopwords
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'be', 'been',
        'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
        'should', 'could', 'may', 'might', 'must', 'can', 'this', 'that',
        'these', 'those', 'i', 'you', 'he', 'she', 'it', 'we', 'they'
    }
    print("⚠️  Using fallback stopwords (no internet connection)")

# Load dataset
df = pd.read_csv("dataset/reviews.csv")
print(f"✅ Loaded {len(df)} reviews from dataset")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

# Apply cleaning
df["cleaned_review"] = df["review"].apply(clean_text)

# Features & labels
X = df["cleaned_review"]
y = df["label"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Train SVM model
model = LinearSVC(max_iter=2000, random_state=42)
model.fit(X_train_vec, y_train)

# Evaluate
predictions = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, predictions)
print(f"\n{'='*50}")
print(f"Model Accuracy: {accuracy:.2%}")
print(f"{'='*50}")
print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model & vectorizer
joblib.dump(model, "svm_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print(f"\n✅ Model and vectorizer saved successfully")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
