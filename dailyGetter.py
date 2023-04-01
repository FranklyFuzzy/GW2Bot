import requests

url = "https://api.guildwars2.com/v2/achievements/daily"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    found = False
    for daily in data["fractals"]:
        x = [3973,2929,11111,2966]
        for id in x:
            if daily["id"] == id:
                url = "https://api.guildwars2.com/v2/achievements?ids=" + str(id)
                response = requests.get(url)
                fractals_data = response.json()
                print("Todays fun activities include ", fractals_data[0]["name"], fractals_data[0]["id"])
                found = True
                break
        if not found:
            continue
    found = False
    for daily in data["wvw"]:
        x = [1848]
        for id in x:
            if daily["id"] == id:
                url = "https://api.guildwars2.com/v2/achievements?ids=" + str(id)
                response = requests.get(url)
                wvw_data = response.json()
                print("Todays fun activities include ", wvw_data[0]["name"], wvw_data[0]["id"])
                found = True
                break
        if not found:
            continue
    found = False
    for daily in data["pve"]:
        x = [1981]
        for id in x:
            if daily["id"] == id:
                url = "https://api.guildwars2.com/v2/achievements?ids=" + str(id)
                response = requests.get(url)
                pve_data = response.json()
                print("Todays fun activities include ", pve_data[0]["name"], pve_data[0]["id"])
                found = True
                break
        if not found:
            continue
else:
    print("Error: Could not retrieve data from the API.")
