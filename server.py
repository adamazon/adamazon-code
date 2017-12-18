import pickle

import numpy as np
import pandas as pd
import seaborn as sns
import web

sns.set()
sns.set_context("poster")

from sklearn.preprocessing import LabelEncoder

from sklearn.model_selection import train_test_split

import string

from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
from nltk import wordpunct_tokenize
from nltk import WordNetLemmatizer
from nltk import sent_tokenize
from nltk import pos_tag

from sklearn.base import BaseEstimator, TransformerMixin


def get_X_Y_from_df(helpful_video_games, test_size=0.2):
    X = helpful_video_games.summary.values
    X = X.reshape(len(X), 1)
    X = np.append(X, np.array(helpful_video_games.reviewText.values).reshape(len(X), 1), 1)
    X = np.append(X, np.array(helpful_video_games.reviewLength.values).reshape(len(X), 1), 1)
    X = np.append(X, np.array(helpful_video_games.overall.values).reshape(len(X), 1), 1)

    X = np.append(X, np.array(helpful_video_games.exclamationCount.values).reshape(len(X), 1), 1)
    X = np.append(X, np.array(helpful_video_games.questionCount.values).reshape(len(X), 1), 1)
    X = np.append(X, np.array(helpful_video_games.threeDotsCount.values).reshape(len(X), 1), 1)
    X = np.append(X, np.array(helpful_video_games.uppercaseCount.values).reshape(len(X), 1), 1)
    X = np.append(X, np.array(helpful_video_games.summaryLength.values).reshape(len(X), 1), 1)
    X = np.append(X, np.array(helpful_video_games.price.values).reshape(len(X), 1), 1)

    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(helpful_video_games.wasHelpful.values)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test


class NLTKPreprocessor(BaseEstimator, TransformerMixin):
    def __init__(self, stopwords=None, punct=None,
                 lower=True, strip=True):
        self.lower = lower
        self.strip = strip
        self.stopwords = stopwords or set(sw.words('english'))
        self.punct = punct or set(string.punctuation)
        self.lemmatizer = WordNetLemmatizer()

    def fit(self, X, y=None):
        return self

    def inverse_transform(self, X):
        return [" ".join(doc) for doc in X]

    def transform(self, X):
        return [
            list(self.tokenize(doc)) for doc in X
        ]

    def tokenize(self, document):
        # Break the document into sentences
        for sent in sent_tokenize(document):
            # Break the sentence into part of speech tagged tokens
            for token, tag in pos_tag(wordpunct_tokenize(sent)):
                # Apply preprocessing to the token
                token = token.lower() if self.lower else token
                token = token.strip() if self.strip else token
                token = token.strip('_') if self.strip else token
                token = token.strip('*') if self.strip else token

                # If stopword, ignore token and continue
                if token in self.stopwords:
                    continue

                # If punctuation, ignore token and continue
                if all(char in self.punct for char in token):
                    continue

                # Lemmatize the token and yield
                lemma = self.lemmatize(token, tag)
                yield lemma

    def lemmatize(self, token, tag):
        tag = {
            'N': wn.NOUN,
            'V': wn.VERB,
            'R': wn.ADV,
            'J': wn.ADJ
        }.get(tag[0], wn.NOUN)

        return self.lemmatizer.lemmatize(token, tag)


class MeanEmbeddingVectorizer(BaseEstimator, TransformerMixin):
    def __init__(self, word2vec):
        self.word2vec = word2vec
        self.dim = len(next(iter(word2vec.values())))

    def fit(self, X, y):
        return self

    def transform(self, X):
        return np.array([
            np.mean([self.word2vec[w] for w in words if w in self.word2vec]
                    or [np.zeros(self.dim)], axis=0)
            for words in X
        ])


class MultipleItemSelector(BaseEstimator, TransformerMixin):
    def __init__(self, keys):
        self.keys = keys

    def fit(self, x, y=None):
        return self

    def transform(self, data_dict):
        if not isinstance(data_dict[:, self.keys][0], str):
            return np.array(list(data_dict[:, self.keys])).reshape(len(data_dict), 1)
        return data_dict[:, self.keys]


with open('pickle/trained_model.pkl', 'rb') as output:
    model = pickle.load(output)
with open('pickle/label_encoder.pkl', 'rb') as output:
    label_encoder = pickle.load(output)

web.config.debug = False

urls = ('/.*', 'Hooks')

app = web.application(urls, globals())


class Hooks:
    def POST(self):
        data = web.input()

        try:
            summary = data.summary
            price = int(data.price)
            review_text = data.reviewText
            overall = int(data.overall)
        except:
            return 'Parameters missing'

        dictionary = dict()
        dictionary['summary'] = summary
        dictionary['price'] = price
        dictionary['reviewText'] = review_text
        dictionary['overall'] = overall

        df = pd.DataFrame.from_dict([dictionary])
        df['exclamationCount'] = df['reviewText'].str.count('!') + df['summary'].str.count('!')
        df['questionCount'] = df['reviewText'].str.count('\?') + df['summary'].str.count('\?')
        df['threeDotsCount'] = df['reviewText'].str.count('\.\.\.') + df['summary'].str.count('\.\.\.')
        df['uppercaseCount'] = df['reviewText'].str.count('[A-Z]') + df['summary'].str.count('[A-Z]')
        df['reviewLength'] = df['reviewText'].str.len()
        df['summaryLength'] = df['summary'].str.len()
        df['wasHelpful'] = 'helpful'

        X_train, X_test, y_train, y_test = get_X_Y_from_df(df)
        prediction = label_encoder.inverse_transform(model.predict(X_test))

        return prediction[0]


if __name__ == '__main__':
    app.run()
