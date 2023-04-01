import tweepy
import boto3

# Create an SSM client object
ssm = boto3.client('ssm')

def lambda_handler(event, context):
    # Retrieve the API credentials from the Parameter Store
    consumer_key = ssm.get_parameter(Name='/twitter-api-keys/consumer-key', WithDecryption=True)['Parameter']['Value']
    consumer_secret = ssm.get_parameter(Name='/twitter-api-keys/consumer-secret', WithDecryption=True)['Parameter']['Value']
    access_token = ssm.get_parameter(Name='/twitter-api-keys/access-token', WithDecryption=True)['Parameter']['Value']
    access_token_secret = ssm.get_parameter(Name='/twitter-api-keys/access-secret', WithDecryption=True)['Parameter']['Value']

    # Authenticate with Twitter API
    client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
    )
    
    # Post a tweet
    response = client.create_tweet(
    text="Hello from AWS"
    )
    print(f"https://twitter.com/user/status/{response.data['id']}")
