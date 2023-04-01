import requests

url = "https://api.guildwars2.com/v2/achievements/daily"
response = requests.get(url)
data = response.json()

ids = []
for key in data.keys():
    if key == "pve" or key == "pvp" or key == "wvw" or key == "fractals" or key == "special":
        for i in range(len(data[key])):
            ids.append(data[key][i]["id"])
for x in ids:
    url = "https://api.guildwars2.com/v2/achievements?ids=" + str(x)
    response = requests.get(url)
    data = response.json()
    print(data[0]["name"], data[0]["id"])
