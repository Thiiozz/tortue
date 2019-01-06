# coding: utf-8

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier

import pickle

def predict():
    model = pickle.load(open('model.sav', 'rb'))

    to_predict = ["rock des année 70", "homme politique francais de droite", "mamifére marin d'asie"]
    predictions = model.predict(to_predict)

    i = 0

    for predict in predictions:
        print(to_predict[i] + " : " + predict + " -> " + "https://fr.wikipedia.org/wiki/" + predict.replace(' ', '_'))
        i += 1

predict()
