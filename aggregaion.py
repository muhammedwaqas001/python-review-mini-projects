class Player:
    def __init__(self, name):
        self.name = name
class Team:
    def __init__(self, player):
        self.player = player
    def show_player(self):
        return f"Player: {self.player.name}"

player = Player("Babar Azam")
team = Team(player)
print(team.show_player())