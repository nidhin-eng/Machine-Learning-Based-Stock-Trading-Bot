from transformers import BertTokenizer, BertForSequenceClassification
from transformers import pipeline
import torch

# Load the FinBERT model for sentiment analysis
finbert = BertForSequenceClassification.from_pretrained("yiyanghkust/finbert-tone", num_labels=3)
tokenizer = BertTokenizer.from_pretrained("yiyanghkust/finbert-tone")
nlp = pipeline("sentiment-analysis", model=finbert, tokenizer=tokenizer)

def estimate_sentiment(news_headlines):
    results = nlp(news_headlines)
    
    # Count results
    counts = {"positive": 0, "neutral": 0, "negative": 0}
    for result in results:
        label = result['label'].lower()
        counts[label] += 1
    
    sentiment = max(counts, key=counts.get)
    probability = counts[sentiment] / len(news_headlines)
    
    return probability, sentiment
