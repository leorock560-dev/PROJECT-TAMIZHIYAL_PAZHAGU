import pandas as pd
import joblib

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

df = pd.read_csv("grammar_corrector.csv")

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            analyzer="char",
            ngram_range=(2,5)
        )
    ),
    (
        "clf",
        LinearSVC()
    )
])

model.fit(df["incorrect_sentence"], df["error_type"])
classify=model.predict
print(classify(["நான் பேசினாள்"]))

joblib.dump(model, "classifier.pkl")
