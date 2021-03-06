class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""
        base_score = 0

        def equal(player_score):
            if player_score == 0:
                score = "Love-All"
            elif player_score  == 1:
                score = "Fifteen-All"
            elif player_score  == 2:
                score = "Thirty-All"
            elif player_score  == 3:
                score = "Forty-All"
            else:
                score = "Deuce"
            return score

        def advantage(player_score):
            minus_result = player_score
            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
            return score

        if self.player1_score == self.player2_score:
            score = equal(self.player1_score)
            
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = advantage(self.player1_score - self.player2_score)
            
        else:
            for i in range(1, 3):
                if i == 1:
                    base_score = self.player1_score
                else:
                    score = score + "-"
                    base_score = self.player2_score

                if base_score == 0:
                    score = score + "Love"
                elif base_score == 1:
                    score = score + "Fifteen"
                elif base_score == 2:
                    score = score + "Thirty"
                elif base_score == 3:
                    score = score + "Forty"

        return score
