import random as rnd
class Player:

    playercount = 0

    def __init__(self, name):
        self.name = name.lower()
        Player.playercount += 1

    def Play(self, previous_games, player_number, round):
        if self.name == "cooperator":
            print("Cooperator chosen!")
            decision = 0
            if decision != 1 and decision != 0:
                print("ERROR. No value decided!")
                return
            return decision

        elif self.name == "defector":
            print("Defector chosen!")
            decision = 1
            if decision != 1 and decision != 0:
                print("ERROR. No value decided!")
                return
            return decision

        elif self.name == "randomy":
            print("Randomy chosen!")
            decision = rnd.randint(0,1)
            if decision != 1 and decision != 0:
                print("ERROR. No value decided!")
                return
            return decision

        elif self.name == "opposite":
            print("Opposite chosen!")

            if player1_previous == None:
                decision = rnd.randint(0,1)
            elif player2_previous == 0:
                decision = 1
            elif player2_previous == 1:
                decision = 0

            if decision != 1 and decision != 0:
                print("ERROR. No value decided!")
                return

            return decision

        elif self.name == "mefirst":
            print("mefirst chosen!")

            if player_number == 0:
                decision = 0
            elif player_number == 1:
                decision = 1
        else:
            print("No strategy chosen!")
