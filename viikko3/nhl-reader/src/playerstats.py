from playerreader import PlayerReader

class PlayerStats:
    top_scorers = []
    def __init__(self, PlayerReader):
        self.players = PlayerReader.get_players()
        
    def top_scorers_by_nationality(self, nationality):
        for player in self.players:
            if player.nationality == "FIN":
                self.top_scorers.append(player)
        
        return sorted(self.top_scorers, key=lambda x: (x.goals + x.assists), reverse=True)
        
