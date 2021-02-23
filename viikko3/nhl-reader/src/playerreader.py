import requests
from player import Player

class PlayerReader:

    players = []
    def __init__(self, url):
        self.url = url
        self.response = requests.get(url).json()

        #print("JSON-muotoinen vastaus:")
        #print(response)
        for player_dict in self.response:
            player = Player(
                player_dict['name'], 
                player_dict['nationality'],
                player_dict['team'],
                player_dict['goals'],
                player_dict['assists']
            )

            self.players.append(player)

    def get_players(self):        
        return self.players
    
    