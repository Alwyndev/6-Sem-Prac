from textblob import TextBlob


def analyze_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"


inp = input("Enter a sentence to start analysis  :  ")
print("Sentiment:", analyze_sentiment(inp))
