import json
import requests
import urllib3

patch = "9.1.1"
name = "xenostiger"
key = "RGAPI-cd072f74-476b-45ca-ba72-291aff48a1c9"
summoner_request = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key).json()


icon_id = summoner_request["profileIconId"]
icon = "https://cdn.communitydragon.org/" + patch + "/profile-icon/" + str(icon_id)

print(summoner_request)