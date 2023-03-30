import tweepy

consumer_key = "DontHardCodeCreds"
consumer_secret = "DontHardCodeCreds"
access_token = "DontHardCodeCreds"
access_token_secret = "DontHardCodeCreds"

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

response = client.create_tweet(
    text="This Tweet was Tweeted using Tweepy and Twitter API v2!"
)
print(f"https://twitter.com/user/status/{response.data['id']}")
