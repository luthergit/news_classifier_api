import joblib
import pandas as pd
import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# load english language model and create nlp object from it
nlp = spacy.load("en_core_web_sm")


def preprocess(text):
    doc = nlp(text)

    filtered_tokens = []

    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)

    return " ".join(filtered_tokens)


def news_classifier():
    df = pd.read_json("news_dataset.json")

    test_model = joblib.load("model_joblib")
    df["predictions"] = test_model.predict(df["text"])
    # df.to_csv('test.csv')
    return df.to_dict()
    # return {'text':10}


def classifier(data: dict[str, str]):
    df = pd.DataFrame.from_dict(data)

    test_model = joblib.load("model_joblib")
    df["predictions"] = test_model.predict(df["text"])
    # df.to_csv('test.csv')
    return df.to_dict()
    # return {'text':10}
