import re
import argparse
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.base import BaseEstimator, TransformerMixin


URL_RE = re.compile(r"https?://\S+|www\.\S+", re.IGNORECASE)

def extract_features(text):
    text = str(text)
    urls = URL_RE.findall(text)
    words = re.findall(r"\b\w+\b", text.lower())
    suspicious_words = [
        "urgent", "verify", "password", "otp", "suspended", "claim",
        "prize", "winner", "bank details", "gift card", "immediately",
        "refund", "click", "account"
    ]
    lower = text.lower()
    return {
        "url_count": len(urls),
        "has_ip_url": int(bool(re.search(r"https?://(?:\d{1,3}\.){3}\d{1,3}", text))),
        "has_https": int("https://" in lower),
        "has_http": int("http://" in lower),
        "exclamation_count": text.count("!"),
        "uppercase_ratio": sum(c.isupper() for c in text) / max(len(text), 1),
        "message_length": len(text),
        "word_count": len(words),
        "suspicious_word_count": sum(lower.count(w) for w in suspicious_words),
    }

class FeatureExtractor(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return pd.DataFrame([extract_features(x) for x in X])


def select_text(X):
    return X["email_text"].astype(str).tolist()

def select_numeric(X):
    return pd.DataFrame([extract_features(x) for x in X["email_text"]])

def build_model():
    text_pipeline = Pipeline([
        ("select", FunctionTransformer(select_text, validate=False)),
        ("tfidf", TfidfVectorizer(ngram_range=(1, 2), stop_words="english"))
    ])
    numeric_pipeline = Pipeline([
        ("extract", FunctionTransformer(select_numeric, validate=False)),
        ("scale", StandardScaler())
    ])
    combined = FeatureUnion([
        ("text", text_pipeline),
        ("numeric", numeric_pipeline)
    ])
    return Pipeline([
        ("features", combined),
        ("classifier", RandomForestClassifier(
            n_estimators=250, random_state=42, class_weight="balanced"
        ))
    ])

def main():
    parser = argparse.ArgumentParser(description="Phishing email detection demo")
    parser.add_argument("--data", default="data/emails.csv", help="CSV with email_text,label columns")
    parser.add_argument("--message", help="Classify one email message")
    args = parser.parse_args()

    data = pd.read_csv(args.data)
    required = {"email_text", "label"}
    if not required.issubset(data.columns):
        raise ValueError("CSV must contain email_text and label columns.")
    data = data.dropna(subset=["email_text", "label"])
    data["label"] = data["label"].astype(str).str.lower().str.strip()
    if not set(data["label"]).issubset({"safe", "phishing"}):
        raise ValueError("Labels must be 'safe' or 'phishing'.")
    if data["label"].nunique() != 2:
        raise ValueError("Dataset must contain both safe and phishing examples.")

    X = pd.DataFrame({"email_text": data["email_text"].astype(str)})
    y = data["label"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    model = build_model()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print(f"\nTest accuracy: {accuracy_score(y_test, predictions):.2%}")
    print("\nClassification report:")
    print(classification_report(y_test, predictions, zero_division=0))

    ConfusionMatrixDisplay.from_predictions(
        y_test, predictions, labels=["safe", "phishing"],
        display_labels=["Safe", "Phishing"], cmap="Blues"
    )
    plt.title("Phishing Email Detection - Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png", dpi=150)
    print("Confusion matrix saved as confusion_matrix.png")

    if args.message:
        result = model.predict(pd.DataFrame({"email_text": [args.message]}))[0]
        print(f"\nPrediction: {result.upper()}")

if __name__ == "__main__":
    main()
