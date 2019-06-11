import random as rnd
class Organism:

    organism_count = 0

    def __init__(self, color):
        self.bases = ["A", "T", "C", "G"]
        self.genome = ""
        for i in range(100):
            self.genome += bases[rnd.randint(0,3)]
    
