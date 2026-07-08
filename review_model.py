cat <<EOF > review_model.py
import pandas as pd
import string
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = "".join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return " ".join(words)

def train_model():
    df = pd.read_csv("reviews.csv")
    df['review'] = df['review'].apply(preprocess)
    df['label'] = df['label'].map({'genuine': 0, 'fake': 1})
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(df['review'])
    y = df['label']
    model = LogisticRegression()
    model.fit(X, y)
    return model, vectorizer

model, vectorizer = train_model()

def predict_review(review):
    review = preprocess(review)
    vector = vectorizer.transform([review])
    prediction = model.predict(vector)
    return "Fake" if prediction[0] == 1 else "Genuine"

print("Model trained successfully!")
EOF
