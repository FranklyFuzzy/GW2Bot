import requests

url = "https://api.guildwars2.com/v2/achievements/daily"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    found = False
    for daily in data["fractals"]:
        x = [3973,2929,11111,2966,1848]
        for id in x:
            if daily["id"] == id:
                url = "https://api.guildwars2.com/v2/achievements?ids=" + str(id)
                response = requests.get(url)
                data = response.json()
                print("Todays fun activities include ", data[0]["name"], data[0]["id"])
                found = True
                break
        if not found:
            continue
else:
    print("Error: Could not retrieve data from the API.")
