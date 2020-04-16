# import SentimentIntensityAnalyzer class from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

# Import dataset
# tweet_list = pd.read_csv('trumptweets.csv')

# function to print sentiments of the sentence.


def sentiment_scores(sentence):

    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)

    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")

    print("Sentence Overall Rated As", end=" ")

    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05:
        print("Positive")

    elif sentiment_dict['compound'] <= - 0.05:
        print("Negative")

    else:
        print("Neutral")


# Driver code
if __name__ == "__main__":

    print("\n1st statement :")
    sentence = "What do I know about branding, maybe nothing (but I did become President!), but if I were Boeing, I would FIX the Boeing 737 MAX, add some additional great features, & REBRAND the plane with a new name. No product has suffered like this one. But again, what the hell do I know?"

    # function calling
    sentiment_scores(sentence)

    print("\n2nd Statement :")
    sentence = "As your President, one would think that I would be thrilled with our very strong dollar. I am not! The Fed’s high interest rate level, in comparison to other countries, is keeping the dollar high, making it more difficult for our great manufacturers like Caterpillar, Boeing,....."
    sentiment_scores(sentence)

    print("\n3rd Statement :")
    sentence = "Why didn’t President Obama do something about the so-called Russian Meddling when he was told about it by the FBI before the Election? Because he thought Crooked Hillary was going to win, and he didn’t want to upset the apple cart! He was in charge, not me, and did nothing."
    sentiment_scores(sentence)
