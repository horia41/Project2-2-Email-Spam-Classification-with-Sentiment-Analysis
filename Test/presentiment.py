import nltk

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
nltk.download('punkt')

import pandas as pd
import re
from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

def preprocess_email(text):
    if not isinstance(text, str):
        return ''
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove email addresses
    text = re.sub(r'\S*@\S*\s?', '', text)
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stop words
    tokens = [word for word in tokens if word not in stopwords.words('english')]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    # Rejoin tokens into a single string
    text = ' '.join(tokens)
    
    return text

def analyze_sentiment(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    
    text_blob = TextBlob(text)
    text_blob_polarity = text_blob.sentiment.polarity
    text_blob_subjectivity = text_blob.sentiment.subjectivity
    
    sentiment_scores.update({
        'text_blob_polarity': text_blob_polarity,
        'text_blob_subjectivity': text_blob_subjectivity
    })
    
    return sentiment_scores

def load_and_preprocess_data(file_path):
    # Determine the file format based on the file name
    file_name = Path(file_path).name
    
    if file_name == 'enron_spam_data.csv':
        df = pd.read_csv(file_path)
        df = df.rename(columns={'Message': 'Message'})
        df['Category'] = df['Spam/Ham'].map({'spam': 'spam', 'ham': 'ham'})
    
    elif file_name == 'SMSSpamCollection':
        df = pd.read_csv(file_path, sep='\t', header=None, names=['Category', 'Message'])
    
    elif file_name == 'spam.csv':
        df = pd.read_csv(file_path)
        df = df.rename(columns={'Category': 'Category', 'Message': 'Message'})
    
    elif file_name == 'spam_or_not_spam.csv':
        df = pd.read_csv(file_path)
        df = df.rename(columns={'email': 'Message'})
        df['Category'] = df['label'].map({1: 'spam', 0: 'ham'})
    
    elif file_name == 'spambase.data':
        column_names = ['feature_' + str(i) for i in range(1, 58)] + ['label']
        df = pd.read_csv(file_path, header=None, names=column_names)
        df['Category'] = df['label'].map({1: 'spam', 0: 'ham'})
        df['Message'] = df.apply(lambda row: ' '.join(row.drop('label').astype(str)), axis=1)
    
    else:
        raise ValueError(f"Unsupported file: {file_name}")
    
    # Preprocess the messages
    df['Message'] = df['Message'].fillna('').apply(preprocess_email)
    
    # Add sentiment analysis
    df['sentiment'] = df['Message'].apply(analyze_sentiment)
    df['sentiment_neg'] = df['sentiment'].apply(lambda x: x['neg'])
    df['sentiment_neu'] = df['sentiment'].apply(lambda x: x['neu'])
    df['sentiment_pos'] = df['sentiment'].apply(lambda x: x['pos'])
    df['sentiment_compound'] = df['sentiment'].apply(lambda x: x['compound'])
    df['text_blob_polarity'] = df['sentiment'].apply(lambda x: x['text_blob_polarity'])
    df['text_blob_subjectivity'] = df['sentiment'].apply(lambda x: x['text_blob_subjectivity'])
    
    # Drop the sentiment column as it's no longer needed
    df.drop(columns=['sentiment'], inplace=True)
    
    # Return the preprocessed data
    return df[['Message', 'sentiment_neg', 'sentiment_neu', 'sentiment_pos', 'sentiment_compound', 'text_blob_polarity', 'text_blob_subjectivity', 'Category']]

def save_preprocessed_data(df, output_file_path):
    df.to_csv(output_file_path, index=False, header=False)
    print(f"Processed data saved to {output_file_path}")

# Fetch the dataset
data_folder = Path(__file__).resolve().parent.parent / 'spambase'
data_file = data_folder / 'SMSSpamCollection'  # Ensure this points to the correct processed data file

df = load_and_preprocess_data(data_file)
output_file = data_folder / 'processed_data_SMS_with_sentiment_advanced.data'
save_preprocessed_data(df, output_file)
