
'''
This code is only to generate the embeddings.

'''
import pickle
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns


from nltk.corpus import stopwords as sw
from nltk.corpus import wordnet as wn
from nltk import wordpunct_tokenize
from nltk import WordNetLemmatizer
from nltk import sent_tokenize
from nltk import pos_tag


sns.set()
sns.set_context("poster")
from operator import itemgetter
class NLTKPreprocessor(BaseEstimator, TransformerMixin):

    def __init__(self, stopwords=None, punct=None,
                 lower=True, strip=True):
        self.lower      = lower
        self.strip      = strip
        self.stopwords  = stopwords or set(sw.words('english'))
        self.punct      = punct or set(string.punctuation)
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


raw_corpus = u"".join(video_games['reviewText']+" . " + video_games['summary'])

import nltk

# Load the punkt tokenizer
tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
print("The punkt tokenizer is loaded")
# we tokenize the raw string into raw sentences
raw_sentences = tokenizer.tokenize(raw_corpus)
print("We have {0:,} raw sentences".format(len(raw_sentences)))

import re
from tqdm import tqdm
# Clean and split sentence into words
def clean_and_split_str(string):
    return NLTKPreprocessor().transform([string])[0]
     
# clean each raw sentences and build the list of sentences
sentences = []
i = 0
for raw_sent in tqdm(raw_sentences):
        sentences.append(clean_and_split_str(raw_sent))
print("We have {0:,} clean sentences".format(len(sentences)))

with open('pickle/sentences.pkl', "wb") as f:
    pickle.dump(sentences, f)
'''
Now, these sentences are processed with the Star space repo code to generate embeddings

$wget https://dl.bintray.com/boostorg/release/1.63.0/source/boost_1_63_0.zip
$unzip boost_1_63_0.zip
$sudo mv boost_1_63_0 /usr/local/bin

git clone https://github.com/facebookresearch/Starspace.git
cd Starspace
make

./starspace train -trainFile data.txt 

'''
