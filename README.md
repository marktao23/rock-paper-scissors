# Coding Sample 2: rock paper scissors

## Design Spec

The goal of this exercise is to write a class (implementing object-oriented principles) in which N players play rock paper scissors. No less than 2 and no more than 10 players play at a time.

Number of players are randomly selected, and are removed from a hashtable data structure as they lose the game. Their moves are also randomly decided. The rules are as follows:
    * Scissors beats Paper
    * Rock beat Scissors
    * Paper beats Rock
    * If one item is thrown by all, the result is a tie, and no one is eliminated
    * If two items are thrown, all those who threw the losing item are eliminated
    * If all three items are thrown, the item that was thrown by the most players is the winner and all items that are defeated by the winning item are eliminated. 
    * If all three items are thrown and there is a tie for highest number of throws, no one is eliminated.

The __main__ method continues to run until just 1 player remains. 

## User Interface

To run, simply run

```bash
python3 rock_paper_scissors.py
```

You can also adjust the __main__ function to view different output. Functional decomposition into modules is clearly indicated in the file.

# Testing output

Here are some sample testing outputs:

```c
Player A threw paper
Player B threw rock
Player C threw rock
Player D threw scissors
Player E threw rock
Player F threw scissors
Player G threw scissors
Player H threw rock
Player I threw rock
Eliminated: 3
rock beats scissors
-------------------------
Player A threw paper
Player B threw paper
Player C threw scissors
Player E threw rock
Player H threw scissors
Player I threw scissors
Eliminated: 2
scissors beats paper
-------------------------
Player C threw rock
Player E threw rock
Player H threw paper
Player I threw scissors
Eliminated: 0
tie
-------------------------
Player C threw paper
Player E threw rock
Player H threw paper
Player I threw rock
Eliminated: 2
paper beats rock
-------------------------
Player C threw rock
Player H threw scissors
Eliminated: 1
rock beats scissors
-------------------------
Player C is the winner!
(base) News-MacBook-Pro:STR admin$ python3 rock_paper_scissors.py 
Player A threw paper
Player B threw scissors
Player C threw rock
Player D threw paper
Player E threw rock
Player F threw scissors
Player G threw paper
Player H threw rock
Player I threw scissors
Eliminated: 0
tie
-------------------------
Player A threw rock
Player B threw rock
Player C threw scissors
Player D threw paper
Player E threw rock
Player F threw rock
Player G threw paper
Player H threw paper
Player I threw paper
Eliminated: 0
tie
-------------------------
Player A threw scissors
Player B threw rock
Player C threw scissors
Player D threw scissors
Player E threw scissors
Player F threw rock
Player G threw scissors
Player H threw scissors
Player I threw rock
Eliminated: 6
rock beats scissors
-------------------------
Player B threw rock
Player F threw paper
Player I threw rock
Eliminated: 2
paper beats rock
-------------------------
Player F is the winner!
```

```c
Player A threw rock
Player B threw scissors
Eliminated: 1
rock beats scissors
-------------------------
Player A is the winner!
(base) News-MacBook-Pro:STR admin$ python3 rock_paper_scissors.py 
Player A threw paper
Player B threw scissors
Player C threw paper
Player D threw paper
Player E threw paper
Player F threw scissors
Player G threw paper
Player H threw scissors
Player I threw rock
Eliminated: 1
paper beats rock
-------------------------
Player A threw scissors
Player B threw scissors
Player C threw scissors
Player D threw scissors
Player E threw paper
Player F threw rock
Player G threw paper
Player H threw rock
Eliminated: 0
tie
-------------------------
Player A threw scissors
Player B threw scissors
Player C threw paper
Player D threw paper
Player E threw paper
Player F threw paper
Player G threw scissors
Player H threw scissors
Eliminated: 4
scissors beats paper
-------------------------
Player A threw paper
Player B threw paper
Player G threw paper
Player H threw rock
Eliminated: 1
paper beats rock
-------------------------
Player A threw rock
Player B threw paper
Player G threw rock
Eliminated: 2
paper beats rock
-------------------------
Player B is the winner!
```
