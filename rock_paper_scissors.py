# Author: Mark Tao
# Date: 4 January 2022
# Purpose: Design a rock paper scissors game 

import random

class rock_paper_scissors:

    # constructor holds number of players, as well as a dictionary
    # containing the playerID and the random item thrown.
    # this will be updated each round as players are removed.
    # also contains all of the items from which a random one
    # will be assigned to a player each round
    def __init__(self):
        self.number_of_players = random.randint(2, 10)
        self.player_items = {}
        self.tuple_of_items = ("paper", "rock", "scissors")
        self.winner = None
        self.loser = None
        
    # method to add all playerIDs to the dictionary.
    def generate_IDs(self):
        for i in range(self.number_of_players):
            # 64 is the offset ascii value which we will use as the playerID.
            # for instance, player 1 is logged as player A (ascii of A is 64.).
            self.player_items[chr(i + 65)] = random.choice(self.tuple_of_items)
    
    # plays the round, removing players/returns result of the game
    def play_round(self):
        eliminated = 0
        # checking to see how many items were thrown
        number_of_items = len(set(self.player_items.values()))

        # check which item is the "winner"
        if number_of_items == 2:
            self.winner = self.check_winner(self.player_items.values())
            self.loser = self.obtain_loser(self.winner)
            # checking which is the loser state and returning.
            for key in list(self.player_items):
                # then, remove its players from the game.
                if self.player_items[key] == self.loser:
                    self.player_items.pop(key)
                    eliminated += 1

        # if three different items are thrown,
        if number_of_items == 3:
            frequency_of_item = {"rock": 0, "scissors": 0, "paper": 0}
            for key in self.player_items:
                frequency_of_item[self.player_items[key]] += 1
            
            # first check to make sure there was no tie
            if len(set(frequency_of_item.values())) == 3:
                # get the winning state and the losing one
                self.winner = max(frequency_of_item, key=frequency_of_item.get)
                self.loser = self.obtain_loser(self.winner)
                # remove losers from game.
                for key in list(self.player_items):
                    if self.player_items[key] == self.loser:
                        self.player_items.pop(key)
                        eliminated += 1
        if eliminated == 0:
            self.winner = None
        return eliminated

    # helper that determines the outcome of the round
    def check_winner(self, list_of_items):

        if self.tuple_of_items[0] in list_of_items and self.tuple_of_items[1] in list_of_items:
            return self.tuple_of_items[0]
        elif self.tuple_of_items[1] in list_of_items and self.tuple_of_items[2] in list_of_items:
            return self.tuple_of_items[1]
        elif self.tuple_of_items[2] in list_of_items and self.tuple_of_items[0] in list_of_items:
            return self.tuple_of_items[2]

    def obtain_loser(self, item):
        if item == self.tuple_of_items[0]:
            return self.tuple_of_items[1]
        elif item == self.tuple_of_items[1]:
            return self.tuple_of_items[2]
        elif item == self.tuple_of_items[2]:
            return self.tuple_of_items[0]
    
    def next_round(self):
        for key in self.player_items:
            self.player_items[key] = random.choice(self.tuple_of_items)

if __name__ == "__main__":
    new_game = rock_paper_scissors()
    new_game.generate_IDs()

    while len(new_game.player_items) > 1:

        for player in new_game.player_items:
            print("Player", player, "threw", new_game.player_items[player])

        print("Eliminated:", new_game.play_round())
        if new_game.winner == None:
            print("tie")
        else:
            print(new_game.winner, "beats", new_game.loser)

        new_game.next_round()
        print("-------------------------")

    print("Player", next(iter(new_game.player_items)), "is the winner!")
