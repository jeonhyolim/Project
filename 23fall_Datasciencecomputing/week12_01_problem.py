# Packages for preprocessing
#! pip install ntlk
#! python -m nltk.downloader all
#! pip install contractions

import re # replace
import contractions # he's -> he is
from nltk.stem import WordNetLemmatizer # had -> have
from collections import Counter
import numpy as np
from nltk.corpus import stopwords # the, a, an etc
from itertools import chain 
from tensorflow import keras # for deep learning model


"""
Refer to https://www.nltk.org/
"""

def letters_only(word):
    return word.isalpha() # T, F를 반환

# lemmaization
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    #### Your Code Here ####
    # from each document, remove all unnecessary characters/punctuation/phrase etc
    # return the document
    text = contractions.fix(text)  # expand contractions
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # remove non-alphabetic characters
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra whitespaces
    cleaned_doc = []
    for word in text.split(' '): # split doc. by blank (' ')
        word = word.lower() # ABD -> abd
        if letters_only(word) and len(word) > 2: # remove number and punc. and name entity
            cleaned_doc.append(lemmatizer.lemmatize(word))
            
    return ' '.join(cleaned_doc) 


    ##############################

def pp_text(docs):
    #### Your Code Here ####
    # for each document, use clean_text to remove unnecessary parts
    # from each cleaned document, remoce unnecessary vocab ex) a, the, etc
    # return list of documents
    cleaned_docs = [clean_text(doc) for doc in docs]
    stop_words = set(stopwords.words('english'))
    tokenized_docs = [doc.split() for doc in cleaned_docs]
    tokenized_docs = [[word.lower() for word in doc if word.lower() not in stop_words] for doc in tokenized_docs]
    return [' '.join(doc) for doc in tokenized_docs]

    ##############################


#### Do not edit here ####

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

categories = [
              'alt.atheism', 'talk.politics.misc', 'comp.graphics',
              'sci.med', 'rec.sport.baseball'
              ]
data_train = fetch_20newsgroups(subset='train', categories=categories, random_state=2023)
data_test = fetch_20newsgroups(subset='test', categories=categories, random_state=2023)

print(data_train.data)


#############################



"""
Refer to https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
"""



#### Your Code Here ####
# Preprocess the documents
# Using TfidfVectorizer, vectorize the documents with max_feature = 1000
# Split train data into train dataset and validation dataset (ratio 8:2)

X_train_cleaned = pp_text(data_train.data)
X_test_cleaned = pp_text(data_test.data)

vectorizer = TfidfVectorizer(max_features=1000)
X_train_tfidf = vectorizer.fit_transform(X_train_cleaned).toarray()
X_test = vectorizer.transform(X_test_cleaned).toarray()

from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X_train_tfidf, data_train.target, test_size=0.2, random_state=2023)
y_test = data_test.target




############################


#### Do not edit here ####


model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=[1000]))
model.add(keras.layers.Dense(256, activation="elu"))
model.add(keras.layers.Dense(128, activation="elu"))
model.add(keras.layers.Dense(64, activation="elu"))
model.add(keras.layers.Dense(5, activation="softmax"))

model.summary()

model.compile(loss="sparse_categorical_crossentropy",
              optimizer="adam",
              metrics=["accuracy"])

history = model.fit(X_train, y_train, epochs=20,
                    validation_data=(X_valid, y_valid))

loss, acc = model.evaluate(X_test, y_test)

print(f'The loss for test data is {loss:.2f}, and the accuracy is {acc:.2f}')

##########################