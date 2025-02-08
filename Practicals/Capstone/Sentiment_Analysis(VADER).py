from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def vader_sentiment_analysis(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    print(score)
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Example


while int(input("Continue (1/0)  :  ")):
    text = input("Enter the Sentence to start analysis  :  ")
    print("Sentiment:", vader_sentiment_analysis(text))
