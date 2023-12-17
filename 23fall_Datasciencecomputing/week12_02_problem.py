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

#### Your Code Here ####
# Read csv file
# Preprocess reviews
# Get vocabs of positive reviews
# Get vocabs of negative reviews
# Count each vocabs and get the frequency
# Remove overlapping vocabs in positive & negative vocabs

import pandas as pd
from google.colab import drive
drive.mount('/content/drive')

import os

os.chdir('/content/drive/MyDrive/대학원_석사과정/수업/23-2/W12') 
data = pd.read_csv('imdb_dataset-1.csv')
data_cleaned = pp_text(data['review']) # 전처

df = data
df['review'] = data_cleaned 

pos = ''
for i in range(len(df[df['sentiment']=='positive']['review'])):
  pos += df[df['sentiment']=='positive']['review'][i]

neg_df = df[df['sentiment']=='negative']['review'].reset_index(drop=True)
neg = ''
for i in range(len(df[df['sentiment']=='negative']['review'])):
  neg += neg_df[i]

positive_word_counts = Counter(pos.split())
negative_word_counts = Counter(neg.split())
both= set(positive_word_counts.keys()) & set(negative_word_counts.keys())

#########################

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

"""
Refer to https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html
"""

#### Your Code Here ####
# Using WordCloud, show frequently used vocabs for each sentiment
# Save the WordCloud in jpg format
positive_word_counts= {word: count for word, count in positive_word_counts.items() if word not in both}
#len(positive_word_counts)
negative_word_counts = {word: count for word, count in negative_word_counts.items() if word not in both}
#print(len(positive_word_counts), len(negative_word_counts))

#positive_word_counts = Counter(pos.split())
wc_pos = WordCloud(width=600, height=600, random_state=2023, max_font_size=110, background_color='white').generate(pos)
wc_pos.generate_from_frequencies(positive_word_counts)

#negative_word_counts = Counter(neg.split())
wc_neg = WordCloud(width=600, height=600, random_state=2023, max_font_size=110, background_color='white').generate(neg)
wc_neg.generate_from_frequencies(negative_word_counts)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(wc_pos, interpolation='bilinear')
plt.title(f'<Positive Words>\n(n_keywords={len(positive_word_counts)})')
plt.axis('off') 

plt.subplot(1, 2, 2)
plt.imshow(wc_neg, interpolation='bilinear')
plt.title(f'<Negative Words>\n(n_keywords={len(negative_word_counts)})')
plt.axis('off') 
plt.tight_layout()
plt.show()
plt.savefig('wordclud.jpg')
#########################

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

"""
Refer to https://www.nltk.org/_modules/nltk/sentiment/vader.html
"""

def vader_polarity(text):
    #### Your Code Here ####
    # Using SentimentIntensityAnalyzer, get the score of each sentiment for the input text
    # return 1 postivie score > negative score,  else 0
    sid = SentimentIntensityAnalyzer()
    scores = sid.polarity_scores(text)
    return 1 if scores['pos'] > scores['neg'] else 0 
    ###########################

#### Your Code Here ####
# Print true sentiment
# Print predicted sentiment score of each document
# Print predicted label

text_list = [
    'despite original began life play central europe weathered several incarnation followed mgm remake period song good old summertime broadway show love even excellent theatre revival paris couple year ago remains definitive version one beat several previous commenters identified contributing factor make successful memorable least prevailing fashion hollywood lavishing attention detail ensemble playing rather two lead often happens today try example removing ugarte ferrari renault etc casablanca yes would still rick ilsa viktor lazslo would frosting without rich cake mixture jimmy stewart maggie sullavan ideal irreplaceable lead much brighter shine performance reflected frank morgan felix bressart joseph schildkraut andy hardy sara haden factor lubitsch touch okay maybe tad naive innocent even jurassic age many genuine film lover sated scatology screwing face sex turn back day story style slickness skill wallow great movie like one far best thing technological age csi dvd one time make classic available nostalgics show matrix freak big boy used Sentiment: positive',
    'bring box kleenex funny engaging moving weeper two leading actor give tour force performance considerable debate afterward whether really disabled appreciated filmmaker dared politically incorrect depicting people severe physical disability fully developed people character flaw result believability engages make grow like care conflict story structure formulaic many secondary character merely type two central character riveting matter interesting original title inside dancing reflects viewpoint character michael new title usa release suggests rory central figure',
    'set world depression era prague story ambitious store clerk falling love mystery woman exchanged romantic letter discover mystery woman none sale girl shop seems constantly bickering colleague add little twist owner convinced favorite employee stewart affair owner wife leaving stewart briefly fired along admission sale girl liked stewart along happy ending inevitable although dated reference poverty wife two kid consider used along indication many small object pleasure like musical cigar box reach common people enjoyment film much effective credible make got mail make starring tom hank meg ryan actual odds chain event unbelievable viewer intelligence grossly offended shop around corner innocent stroll memory lane le complicated le hectic romantic time place known novelist utopia lover classic romantic comedy enjoy picture',
    'absolutely love movie would really like someday fascinating legend eagle wear turquoise necklace loved would like see remember much native american boy life nice village family remember happens supposed wilderness alone sister pack food go indian boy come running put feather turn eagle legend say ever see eagle wearing turquoise necklace boy always fascinated legend particularly native american legend would love see released someday dvd please release whoever concerned'
]
sid = SentimentIntensityAnalyzer()
predicted_sentiments = [vader_polarity(text) for text in text_list]
predicted_sentiments_polarity = [sid.polarity_scores(text) for text in text_list]
senti = ['positive', 'positive', 'positive', 'positive']

for i, text in enumerate(text_list):
    print(f"Text {i} : {text}")
    print(f"Sentiment: {senti[i]}")
    print(f"Predicted Sentiment polarity: {predicted_sentiments_polarity[i]}")
    print(f"Predicted Sentiment polarity Class: {predicted_sentiments[i]}")
    print("-" * 60)
########################