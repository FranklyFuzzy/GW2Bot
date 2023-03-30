import requests

url = "https://api.guildwars2.com/v2/achievements/daily"
response = requests.get(url)
data = response.json()

ids = []
for key in data.keys():
    if key == "pve" or key == "pvp" or key == "wvw" or key == "fractals" or key == "special":
        for i in range(len(data[key])):
            ids.append(data[key][i]["id"])

ids_to_check = [2908, 3201, 2989, 1930]

if any(x in ids_to_check for x in ids):
    print("Today's fun activities include :")
    for x in ids_to_check:
        if x in ids:
            url = "https://api.guildwars2.com/v2/achievements?ids=" + str(x)
            response = requests.get(url)
            data = response.json()
            print(data[0]["name"], data[0]["id"])
else:
  print("no fun today")
