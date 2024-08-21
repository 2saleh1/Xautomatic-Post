import tweepy
import time
import random

# Twitter API credentials
consumer_key = ""
consumer_secret = ""
bearer_token = ""
access_token = ""
access_token_secret = ""

# Authenticate to Twitter using OAuth2
client = tweepy.Client(bearer_token=bearer_token, consumer_key=consumer_key,
                       consumer_secret=consumer_secret, access_token=access_token,
                       access_token_secret=access_token_secret)


random_phrases = [
    "phrase1",
    "phrase2",
    "phrase3",
    "phrase4"
]

# Function to post a tweet
def post_tweet():
    print("Attempting to post a tweet...")
    base_tweet = "This is an automated tweet posted every 5 minutes!"
    random_tweet = random.choice(random_phrases)
    full_tweet = f"{base_tweet}\n\n{random_tweet}"
    random_phrases.remove(random_tweet)
    try:
        client.create_tweet(text=full_tweet)
        print(f"Tweet posted: {full_tweet}")
    except tweepy.TweepyException as e:
        print(f"Error: {e}")

# Loop to post a tweet every 5 minutes (300 seconds)
while True:
    post_tweet()
    time.sleep(300)  # Sleep for 300 seconds (5 minutes)
