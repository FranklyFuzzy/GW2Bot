import requests
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
    
    url = "https://api.guildwars2.com/v2/achievements/daily"
    response = requests.get(url)
    data = response.json()
    
    ids = []
    for key in data.keys():
        if key == "pve" or key == "pvp" or key == "wvw" or key == "fractals" or key == "special":
            for i in range(len(data[key])):
                ids.append(data[key][i]["id"])

    ids_to_check = [2908, 3201, 2989, 1930, 1852, 1839]

    if any(x in ids_to_check for x in ids):
        message = "Today's fun activities include:\n"
        for x in ids_to_check:
            if x in ids:
                url = "https://api.guildwars2.com/v2/achievements?ids=" + str(x)
                response = requests.get(url)
                data = response.json()
                #message += f"{data[0]['name']} ({data[0]['id']})\n"
                message += f"{data[0]['name']}\n"
    else:
        message = "No fun today :("

    # Authenticate with Twitter API
    client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
    )
    
    # Post a tweet
    response = client.create_tweet(
    text=message
    )
    print(f"https://twitter.com/user/status/{response.data['id']}")
