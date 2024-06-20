import pandas as pd
from pathlib import Path

def shift_sentiment_features(input_file, output_file):
    # Load the processed data with sentiment features
    processed_data = pd.read_csv(input_file, header=None, names=['Message', 'sentiment_neg', 'sentiment_neu', 'sentiment_pos', 'sentiment_compound', 'Category'])

    # Transform sentiment features to non-negative values
    min_neg = processed_data['sentiment_neg'].min()
    min_neu = processed_data['sentiment_neu'].min()
    min_pos = processed_data['sentiment_pos'].min()
    min_compound = processed_data['sentiment_compound'].min()

    processed_data['sentiment_neg'] = processed_data['sentiment_neg'] - min_neg
    processed_data['sentiment_neu'] = processed_data['sentiment_neu'] - min_neu
    processed_data['sentiment_pos'] = processed_data['sentiment_pos'] - min_pos
    processed_data['sentiment_compound'] = processed_data['sentiment_compound'] - min_compound

    processed_data.to_csv(output_file, index=False, header=False)
    print(f"Sentiment-shifted data saved to {output_file}")


if __name__ == "__main__":
    data_folder = Path(__file__).resolve().parent.parent / 'spambase'
    input_file = data_folder / 'processed_data3_with_sentiment.data'
    output_file = data_folder / 'processed_data3_with_sentiment_shifted.data'
    shift_sentiment_features(input_file, output_file)
