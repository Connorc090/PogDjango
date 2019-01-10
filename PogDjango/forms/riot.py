import json
import requests
import urllib3

         
key = "RGAPI-be0138f2-42c5-4edd-9cf7-a5ee8197419a"

def call_riot(name):
    summoner_request = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key).json()
    raw = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key)

    status = raw.status_code

    if status == 200:
        id = summoner_request["id"]
        id_request = requests.get("https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/" + str(id) + "?api_key=" + key).json()          
        formatted_name = str(summoner_request["name"])

        print()
        print(("Status code: ") + str(status))
        print()
        print(formatted_name)
        print(("Level: ") + str(summoner_request["summonerLevel"]))
        print()
        
        if len(id_request) == 3:
            flex = id_request[0]
            solo_duo = id_request[1]
            tt = id_request[2]

            print("Solo/Duo: " + solo_duo["tier"], end=' ')
            print(solo_duo["rank"], end=' ')
            print(str(solo_duo["leaguePoints"]) + "lp")
            print("Flex: " + flex["tier"], end=' ')
            print(flex["rank"], end=' ')
            print(str(flex["leaguePoints"]) + "lp")
            print("Twisted Treeline: " + tt["tier"], end=' ')
            print(tt["rank"], end=' ')
            print(str(tt["leaguePoints"]) + "lp")
            print()
        elif len(id_request) == 2:
            flex = id_request[0]
            solo_duo = id_request[1]

            print("Solo/Duo: " + solo_duo["tier"], end=' ')
            print(solo_duo["rank"], end=' ')
            print(str(solo_duo["leaguePoints"]) + "lp")
            print("Flex: " + flex["tier"], end=' ')
            print(flex["rank"], end=' ')
            print(str(flex["leaguePoints"]) + "lp")
            print("Twisted Treeline: Unranked")
            print()
        elif len(id_request) == 1:
            solo_duo = id_request[0]

            print("Solo/Duo: " + solo_duo["tier"], end=' ')
            print(solo_duo["rank"], end=' ')
            print(str(solo_duo["leaguePoints"]) + "lp")
            print("Flex: Unranked")
            print("Twisted Treeline: Unranked")
            print()
        elif len(id_request) == 0:
            print("Solo/Duo: Unranked")
            print("Flex: Unranked")
            print("Twisted Treeline: Unranked")
            print()    

    else:
        print()
        print("Input: " + formatted_name)
        print("Error:" + str(status))  
        print()  
    
    return summoner_request  




