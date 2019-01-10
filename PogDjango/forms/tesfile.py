
import json
import requests
import urllib3

         
key = "RGAPI-be0138f2-42c5-4edd-9cf7-a5ee8197419a"

def call_riot():
    name = "minecraft import"

    summoner_request = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key).json()
    raw = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key)

    status = raw.status_code
    
    if status == 200:
        id = summoner_request["id"]
        id_request = requests.get("https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/" + str(id) + "?api_key=" + key).json()



        print(id_request)
    else:
        print()
        print("Input: " + name)
        print("Error:" + str(status))  
        print()  
    
    return summoner_request  

call_riot()
