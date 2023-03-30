import requests
import datetime

# Get the current date
now = datetime.datetime.now()

# Format the date as YYYY-MM-DD
date_string = now.strftime('%Y-%m-%d')

url = "https://api.guildwars2.com/v2/achievements/daily"
response = requests.get(url)
data = response.json()

ids = []
for key in data.keys():
    if key == "pve" or key == "pvp" or key == "wvw" or key == "fractals" or key == "special":
        for i in range(len(data[key])):
            ids.append(data[key][i]["id"])
with open(f'output_{date_string}.txt', 'w') as f:
    for x in ids:
        url = "https://api.guildwars2.com/v2/achievements?ids=" + str(x)
        response = requests.get(url)
        data = response.json()
        print(data[0]["name"], data[0]["id"])
        print(data[0]["name"], data[0]["id"], file =f)
