import random as rnd
class Player:

    playercount = 0

    def __init__(self, name):
        self.name = name.lower()
        Player.playercount += 1

    def Cooperator(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Cooperator chosen!")

        print("Current round: {}".format(current_round))
        decision = 0
        if decision != 1 and decision != 0:
            print("ERROR. No value decided!")
            return(3)

        return decision

    def Defector(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Defector chosen")

        decision = 1
        if decision != 1 and decision != 0:
            print("ERROR. No value detected")
            return

        return decision

    def Randomy(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Randomy chosen")

        decision = rnd.randint(0,1)
        if decision != 1 and decision != 0:
            print("ERROR. Incorrect value detected!")
            return 3

        return decision

    def Opposite(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("Opposite chosen!")

        if player_number == 0:
            # Determines itself to be player 1 and the other to be player 2
            other_player = 1
        elif player_number == 1:
            # Determines itself to be player 2 and the other to be player 1
            other_player = 0

        if current_round == 0:
            decision = rnd.randint(0,1)
        elif previous_games[other_player][current_round-1] == 0:
            decision = 1
        elif previous_games[other_player][current_round-1] == 1:
            decision = 0

        return decision

    def MeFirst(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("MeFirst chosen!")

        if player_number == 0:
            decision = 0
        elif player_number == 1:
            decision = 1

        return decision

    def HappyFlop(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("HappyFlop chosen!")
            decision = 0
        else:
            decision = (current_round) % 2

        if decision != 1 and decision != 0:
            print("ERROR. Incorrect value detected!")
            return 3

        return decision


    def AngryFlop(self, previous_games, player_number, current_round):
        if current_round == 0:
            print("AngryFlop chosen!")
            decision = 1
        else:
            decision = (current_round+1) % 2

        if decision != 1 and decision != 0:
            print("ERROR. Incorrect value detected!")
            return 3

        return decision

    def Play(self, previous_games, player_number, current_round):
        if self.name == "cooperator":
            return self.Cooperator(previous_games, player_number, current_round)

        elif self.name == "defector":
            return self.Defector(previous_games, player_number, current_round)

        elif self.name == "randomy":
            return self.Randomy(previous_games, player_number, current_round)

        elif self.name == "opposite":
            return self.Opposite(previous_games, player_number, current_round)

        elif self.name == "mefirst":
            return self.MeFirst(previous_games, player_number, current_round)

        elif self.name == "happyflop":
            return self.HappyFlop(previous_games, player_number, current_round)

        elif self.name == "angryflop":
            return self.AngryFlop(previous_games, player_number, current_round)

        else:
            print("No strategy chosen!")
            return 3
