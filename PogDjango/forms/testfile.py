
import json
import requests
import urllib3


key = "RGAPI-5a60b593-bf11-46c3-9f3d-a4e1266f259a"

class riot_class:
    def call_riot(self, name):
        self.summoner_request = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key).json()
        self.raw = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key)

        self.status = self.raw.status_code

        if self.status == 200:
            self.id = self.summoner_request["id"]
            self.id_request = requests.get("https://na1.api.riotgames.com/lol/league/v4/positions/by-summoner/" + str(id) + "?api_key=" + key).json()          
            self.formatted_name = str(self.summoner_request["name"])

            print()
            print(("Status code: ") + str(self.status))
            print()
            print(self.formatted_name)
            print(("Level: ") + str(self.summoner_request["summonerLevel"]))
            print()
            
            self.solo = False
            self.flexx = False
            self.twisted = False


            if len(self.id_request) == 3:
                self.one = self.id_request[0]
                self.two = self.id_request[1]
                self.three = self.id_request[2]

                if self.one['queueType'] == "RANKED_SOLO_5x5":
                    self.solo_duo = self.one
                elif self.one['queueType'] == 'RANKED_FLEX_SR':
                    self.flex = self.one
                else:
                    self.tt = self.one
                
                if self.two['queueType'] == "RANKED_SOLO_5x5":
                    self.solo_duo = self.two
                elif self.two['queueType'] == 'RANKED_FLEX_SR':
                    self.flex = self.two
                else:
                    self.tt = self.two

                if self.three['queueType'] == "RANKED_SOLO_5x5":
                    self.solo_duo = self.three
                elif self.three['queueType'] == 'RANKED_FLEX_SR':
                    self.flex = self.three
                else:
                    self.tt = self.three    
                    
                
                print("Solo/Duo: " + self.solo_duo["tier"], end=' ')
                print(self.solo_duo["rank"], end=' ')
                print(str(self.solo_duo["leaguePoints"]) + "lp")
                print("Flex: " + self.flex["tier"], end=' ')
                print(self.flex["rank"], end=' ')
                print(str(self.flex["leaguePoints"]) + "lp")
                print("Twisted Treeline: " + self.tt["tier"], end=' ')
                print(self.tt["rank"], end=' ')
                print(str(self.tt["leaguePoints"]) + "lp")
                print()
            elif len(self.id_request) == 2:
                self.one = self.id_request[0]
                self.two = self.id_request[1]

                if self.one['queueType'] == "RANKED_SOLO_5x5":
                    self.solo_duo = self.one
                    self.solo = True
                elif self.one['queueType'] == 'RANKED_FLEX_SR':
                    self.flex = self.one
                    self.flexx = True
                else:
                    self.tt = self.one
                    self.twisted = True
                
                if self.two['queueType'] == "RANKED_SOLO_5x5":
                    self.solo_duo = self.two
                    self.solo = True
                elif self.two['queueType'] == 'RANKED_FLEX_SR':
                    self.flex = self.two
                    self.flexx = True                
                else:
                    self.tt = self.two
                    self.twisted = True

                if self.solo == True:
                    print("Solo/Duo: " + self.solo_duo["tier"], end=' ')
                    print(self.solo_duo["rank"], end=' ')
                    print(str(self.solo_duo["leaguePoints"]) + "lp")
                else:
                    print("Solo/Duo: Unranked")    
                if self.flexx == True:
                    print("Flex: " + self.flex["tier"], end=' ')
                    print(self.flex["rank"], end=' ')
                    print(str(self.flex["leaguePoints"]) + "lp") 
                else:
                    print("Flex: Unranked") 
                if self.twisted == True:
                    print("Twisted Treeline: " + self.tt["tier"], end=' ')
                    print(self.tt["rank"], end=' ')
                    print(str(self.tt["leaguePoints"]) + "lp")
                else:
                    print("Twisted Treeline: Unranked") 
                print()
            elif len(self.id_request) == 1:
                self.one = self.id_request[0]

                if self.one['queueType'] == "RANKED_SOLO_5x5":
                    self.solo_duo = self.one
                    self.solo = True
                elif self.one['queueType'] == 'RANKED_FLEX_SR':
                    self.flex = self.one
                    self.flexx = True
                else:
                    self.tt = self.one
                    self.twisted = True


                if self.solo == True:
                    print("Solo/Duo: " + self.solo_duo["tier"], end=' ')
                    print(self.solo_duo["rank"], end=' ')
                    print(str(self.solo_duo["leaguePoints"]) + "lp")
                else:
                    print("Solo/Duo: Unranked") 
                if self.flexx == True:
                    print("Flex: " + self.flex["tier"], end=' ')
                    print(self.flex["rank"], end=' ')
                    print(str(self.flex["leaguePoints"]) + "lp") 
                else:
                    print("Flex: Unranked") 
                if self.twisted == True:
                    print("Twisted Treeline: " + self.tt["tier"], end=' ')
                    print(self.tt["rank"], end=' ')
                    print(str(self.tt["leaguePoints"]) + "lp")
                else:
                    print("Twisted Treeline: Unranked") 
                print()
            elif len(self.id_request) == 0:
                print("Solo/Duo: Unranked")
                print("Flex: Unranked")
                print("Twisted Treeline: Unranked")
                print()    

        else:
            print()
            print("Input: " + name)
            print("Error:" + str(self.status))  
            print() 


        return riot_class()



riot_class().call_riot("xenostiger")