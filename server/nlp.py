#import modules for vader lexicon analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

#container type for sentiment
class Sentiment():
    def __init__(self,polarity_score):
        self.polarity_score=polarity_score
        self.analyze_sentiment_compound()
        self.analyze_sentiment_discrete()
    #analyze polarity score compound
    def analyze_sentiment_compound(self):
        if self.polarity_score['compound'] >= 0.05:
            self.sentiment = 'Positive'
        elif self.polarity_score['compound'] <= -0.05:
            self.sentiment = 'Negative'
        else:
            self.sentiment = 'Neutral'
    #analyze polarity score discrete
    def analyze_sentiment_discrete(self):
        self.positive=self.polarity_score["pos"]
        self.negative=self.polarity_score["neg"]
        self.neutral=self.polarity_score["neu"]
    #prepare data for response
    def res(self):
        return {
            "sentiment":self.sentiment,
            "pos":(self.positive*100),
            "neg":(self.negative*100),
            "nue":(self.neutral*100)
        }

#function for analyzing sentiment using vader lexicon
def analyze_sentiment(req_obj,analyzer=SentimentIntensityAnalyzer):
    text=req_obj.text
    #find polarity score
    polarity_score=analyzer().polarity_scores(text)
    #initiate class sentiment and return result

    sentiment=Sentiment(polarity_score)
    return sentiment
