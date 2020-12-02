import nltk
import re

from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer as Vader
from nltk.stem import WordNetLemmatizer

def part_of_speech(word):
    tag = nltk.pos_tag([word])[0][1][0]
    nltk_tag_to_wordnet_tag = {
        'J': wordnet.ADJ, 
        'V': wordnet.VERB, 
        'N': wordnet.NOUN,
        'R': wordnet.ADV
    }
    try:
        return nltk_tag_to_wordnet_tag[tag]
    except KeyError: 
        return ''

def lemmatization(word):
    lemmatizer = WordNetLemmatizer()
    pos = part_of_speech(word)

    if pos in ['a', 'v', 'n', 'r']:
        return lemmatizer.lemmatize(word, pos=pos)
    
    return lemmatizer.lemmatize(word)

def clean_tweet(tweet):
    # case folding and URL removal
    url_removed = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', tweet.lower())
    
    # punctuation removal
    text = re.sub(r'[^\w\s]', ' ', url_removed)

    stopword_list = stopwords.words('english') + ['a', 'amp', 'an', 'and', 'at', 'be', 'in', 'of', 'u', 'the']
    tokenized_texts = word_tokenize(text)

    clean_text = []
    for tokenized_text in tokenized_texts:
        lemmatized_text = lemmatization(tokenized_text) # lemmatization
        if lemmatized_text not in stopword_list and lemmatized_text != '': # stopwords removal
            clean_text.append(lemmatized_text)

    return ' '.join(clean_text)

def vader_analyzer(tweet):
    vader_scoring = Vader()
    polarity = vader_scoring.polarity_scores(tweet)
    sentiment = 1 if polarity['compound'] >= 0.05 else (-1 if polarity['compound'] <= -0.05 else 0)

    return (polarity, sentiment)