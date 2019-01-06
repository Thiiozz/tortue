# coding: utf-8

import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import SGDClassifier

import pickle

df = pd.read_csv('dataset.csv', sep=';')

# Logistic regression

reg_text_clf = Pipeline([
    ('vect', CountVectorizer(lowercase=False)),
    ('tfidf', TfidfTransformer()),
    ('reg', SGDClassifier())
])

reg_text_clf.fit(df.text, df.subject)

pickle.dump(reg_text_clf, open('model.sav', 'wb'))
