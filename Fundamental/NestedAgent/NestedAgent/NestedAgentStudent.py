"""
NestedAgent.py

created by:  Travis Martin
Copyright:  2021 AI Academy NC State

The following code will implement the five basic agents for AI
"""

import random

# Import the items.
import WumpusLib

"""
Basic agent class
The class will run 100 moves for the agent
It has no class variables
All other agents inherit this agent
"""


class BasicAgent(object):
    """
    input: none
    1. set the player position or reset it depending on game play
    2. play the game for 100 moves
        a. get game percepts
        b. call the agent function - based on agent type and return new action
        c. if the actrion wrapper returns false - you died - otherwise do action
    output: none
    """

    def play_game(self):

        # this line will persist your start location over multiple runs of the game
        self.Game.player_pos = self.start_pos

        # Iterate the max number of steps.
        for I in range(100):

            # Get the current percepts.
            Percepts = self.Game.get_percepts()

            # Call the agent function to get the action.
            NewAction = self.agent_func(Percepts)

            # Now do the wrapper for the steps.
            if (self.Game.action_wrapper(NewAction)) == False:
                print("Game Over!")
                break
        return


"""
Reflex Agent
This agent will simply move around the board in a specific fashion
If it finds gold it will pick it up
"""


class SimpleReflex(BasicAgent):
    """
    constructor: init gameboard and starting position
    """

    def __init__(self, GameBoard):
        self.Game = GameBoard
        self.start_pos = GameBoard.get_curr_room()

    """
    input: percepts
    1. if length percepts = 0, then go west
    2. if gold in percepts, pick it up
    3. otheriwse go north
    output: the chosen action
    """

    def agent_func(self, Percepts):

        if (len(Percepts) == 0):
            return ("GoWest")

        elif ("glint" in Percepts):
            return ("PickupGold")

        else:
            return ("GoNorth")


"""
inherits the basic agent but not the relfex agent
I wanted it to have a bit more intelligent behavior
initializes a game board model that is updated throughout the game play
"""


class ModelAgent(BasicAgent):
    """
    constructor - init gameboard, start position, and a game model
    """

    def __init__(self, GameBoard):
        self.Game = GameBoard
        self.start_pos = GameBoard.get_curr_room()
        self.Game_Model = {}

    """
    input: none
    1. get the players current position
    2. use the game model and check to see if anything is known about the spaces N, S, E, and W
    3. if any of those spaces are marked with pit or wumpus, do not wove there
    4. gather all the possible directions the player can move
    output: all of the possible directions
    """

    def get_safe_room(self):
        curr_pos = self.Game.get_curr_room()
        posible_directions = []

        if (curr_pos - 5) in self.Game_Model.keys():
            if self.Game_Model[curr_pos - 5] != 'wumpus' and self.Game_Model[curr_pos - 5] != 'pit':
                posible_directions.append('GoNorth')
        else:
            posible_directions.append('GoNorth')

        if (curr_pos + 5) in self.Game_Model.keys():
            if self.Game_Model[curr_pos + 5] != 'wumpus' and self.Game_Model[curr_pos + 5] != 'pit':
                posible_directions.append('GoSouth')
        else:
            posible_directions.append('GoSouth')

        if (curr_pos + 1) in self.Game_Model.keys():
            if self.Game_Model[curr_pos + 1] != 'wumpus' and self.Game_Model[curr_pos + 1] != 'pit':
                posible_directions.append('GoEast')

        if (curr_pos - 1) in self.Game_Model.keys():
            if self.Game_Model[curr_pos - 1] != 'wumpus' and self.Game_Model[curr_pos - 1] != 'pit':
                posible_directions.append('GoWest')
        else:
            posible_directions.append('GoWest')

        return posible_directions

    """
    input: percepts
    1. if nothing in percepts
        a. mark the current space as safe
        b. check adjacent spaces
        c. if the spaces are safe, choose a random one to move to
    2. if the gold is in the percepts, pick it up
        a. mark the space with gold
    3. otheriwse 
        a. add the percepts to the game model
        b. check the adjaceent spaces for safety
        c. choose a radom space to move to
    output: the chosen direction
    """

    def agent_func(self, Percepts):
        if (len(Percepts) == 0):
            self.Game_Model[self.Game.get_curr_room()] = "safe"

            posible_directions = self.get_safe_room()
            index = random.randint(0, len(posible_directions) - 1)
            direction = posible_directions[index]

            return direction

        elif ("glint" in Percepts):
            self.Game_Model[self.Game.get_curr_room()] = "gold"
            return ("PickupGold")

        else:
            for percept in Percepts:
                self.Game_Model[self.Game.get_curr_room()] = percept

            posible_directions = self.get_safe_room()
            index = random.randint(0, len(posible_directions) - 1)
            direction = posible_directions[index]

            return direction


if __name__ == "__main__":

    # initialize a new game - set to true if you want to see messages
    NewGame = WumpusLib.WumpusGame(PrintMessages=True)

    # print the new board
    NewGame.printBoard()

    # agent calls - un comment which ever one you want to run
    Agent = SimpleReflex(NewGame)
    # Agent = ModelAgent(NewGame)

    # play five games on the same board
    for n in range(5):
        Agent.play_game()
