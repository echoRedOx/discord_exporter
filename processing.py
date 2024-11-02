import yaml
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#import nltk
#nltk.download('vader_lexicon')

# import the data
def load_data(filepath: str):
    with open(filepath, 'r') as file:
        data = yaml.safe_load(file)
    
    return data

# restructure the data
# sentiment analysis
def analyze_sentiment(text):
    sent_analyzer = SentimentIntensityAnalyzer()
    scores = sent_analyzer.polarity_scores(text)

    if scores['pos'] >= .15 and scores['pos'] > scores['neg']:
        sentiment = 'Positive'
    if scores['neg'] >= .15 and scores['neg'] > scores['pos']:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return scores


def add_sentiment():
    pass


def convert_timestamp():
    pass


def show_conversation_sentiment(data):
    neutral = 0
    positive = 0
    negative = 0
    count = 0
    threshold = .10

    for msg in data:
        count += 1
        content = msg['content']
        sent = analyze_sentiment(content)
        #print(f"Message: {sent}\n{content}")
        
        if sent['pos'] > sent['neg']:
            if sent['pos'] >= threshold:
                positive += 1
            else:
                neutral += 1
        elif sent['neg'] > sent['pos']:
            if sent['neg'] >= threshold:
                negative += 1
            else:
                neutral += 1
        else:
            neutral += 1
    

    print(f"Total Messages: {count}\nNeutral: {neutral}\nNegative: {negative}\nPositive: {positive}")


data = load_data('conversations/Community_general-conversation_2024-10-30.yaml')
show_conversation_sentiment(data=data)