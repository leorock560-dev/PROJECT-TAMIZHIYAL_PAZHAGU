import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

data=pd.read_csv("gender_dataset.csv")

X=data["name"]
X=X.str.lower()
y=data["gender"]

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

vectorizer=TfidfVectorizer(analyzer='char', ngram_range=(2,3))
X_train_vec=vectorizer.fit_transform(X_train)
X_test_vec=vectorizer.transform(X_test)

model=LogisticRegression()
model.fit(X_train_vec,y_train)

prediction=model.predict(X_test_vec)
def gen_id(name):
    name=name.lower()
    name_vec=vectorizer.transform([name])
    pred=model.predict(name_vec)
    return pred[0]
