##########################################################
# WumpusLib.py
# Collin F. Lynch
# 1/01/2021
#
# This file provides a basic Wumpus world object for use
# with the AIA course tasks.  It allows the user to create
# a wumpus game and then to interact with it via an agent
# which tries to play it.
#
# This code is based upon a public wumpus game available at:
#     https://rosettacode.org/wiki/Hunt_The_Wumpus#Python
#


# Imports
# ------------------------------------------------
import random


class WumpusGame(object):
    """
    The WumpusGame class provides the basic tasks of creating a
    game board and filling it in with stuff.  It also provides 
    a basic API for accessing elements of the game, getting data
    on a room, and changing the world.  See the API features below.
    """

    # Initialize the game itself.
    # ---------------------------------------------
    def __init__(self, PrintMessages=True):
        """
	Initialize with a basic graph.  If PrintMessages is set then
        updates will be given to the users as things happen.  
        """

        # If a random cave is required this will make a random regular
        # Graph with 26 nodes.  Failing that it will use the regular
        # cave.
        # if (RandomCave == True): self._make_random_cave()
        # else:
        self._make_standard_cave()

        # Now populate the cave with elements including 
        # the threats and the gold itself.  
        self.threats = {}
        self.pits = set([])
        self.gold_pos = -1
        self.exit_pos = -1
        self.wumpus_pos = -1
        self._populate_cave()

        # And finally set the location of our player
        # and parameters to store his information. 
        self.arrows = 1
        self.arrow_travel_distance = 5

        self.has_gold = False
        self.player_pos = -1
        self._add_player()

        # Store the messages
        self.print_messages = PrintMessages

    def _make_standard_cave(self):
        """
        Build a standard 5x5 cave with locations specified by index.
        and once you do that we will fill it in with appropriate 
        items.  
        """
        CaveDict = {1: (2, 6),
                    2: (1, 7, 3),
                    3: (2, 8, 4),
                    4: (3, 9, 5),
                    5: (4, 10),
                    6: (1, 7, 11),
                    7: (2, 6, 8, 12),
                    8: (3, 7, 9, 13),
                    9: (4, 8, 10, 14),
                    10: (5, 9, 15),
                    11: (6, 12, 16),
                    12: (7, 11, 13, 17),
                    13: (8, 12, 14, 18),
                    14: (9, 13, 15, 19),
                    15: (10, 14, 20),
                    16: (11, 17, 21),
                    17: (12, 16, 18, 22),
                    18: (13, 17, 19, 23),
                    19: (14, 18, 20, 24),
                    20: (15, 19, 25),
                    21: (16, 22),
                    22: (17, 21, 23),
                    23: (18, 22, 24),
                    24: (19, 23, 25),
                    25: (20, 24)
                    }

        self.cave = CaveDict

    def _populate_cave(self):
        """ 
        Drop threats and gold into the cave location.
        """
        # First scatter pits around the place and record
        # their location.  
        for threat in ['pit', 'pit', 'pit', 'pit']:
            pos = random.choice(self._get_safe_rooms())
            self.threats[pos] = threat
            self.pits.add(pos)

        # Now drop the wumpus himself into the space. 
        pos = random.choice(self._get_safe_rooms())
        self.threats[pos] = "wumpus"
        self.wumpus_pos = pos

        # Now place the gold in one of the remaining safe rooms.
        pos = random.choice(self._get_safe_rooms())
        self.gold_pos = pos

        # And place the exit somewhere not containing a pit.
        pos = random.choice(self._get_level_rooms())
        self.exit_pos = pos

    def _add_player(self):
        """
        Drop the player into a random safe location.
        """
        # Now place the gold in one of the remaining safe rooms.
        pos = random.choice(self._get_safe_rooms())
        self.player_pos = pos

    # Internal Methods (Do not Use for Agents)
    # -------------------------------------------

    def _get_safe_rooms(self):
        """ 
        Returns a list containing all numbers of rooms that
        do not contain any threats
        """
        return list(set(self.cave.keys()).difference(self.threats.keys()))

    def _get_level_rooms(self):
        """
        Return a list of rooms not containing a pit.
        """
        return list(set(self.cave.keys()).difference(self.pits))

    def _goto_room(self, RoomNum):
        """
        Go to the specified room number (internal only)
        This will process threat consequences if you 
        are there.
        
        NOTE: It does not check if you are next to the 
        room in question.
        """

        self.msg(" Going to room: {}".format(RoomNum))

        # Perform a rudimentary check for a valid num.
        if ((RoomNum < 1) or (RoomNum > 25)):
            self.msg("  Bad room.")
            return (False)

        elif (RoomNum in self.threats):
            Threat = self.threats[RoomNum]
            self.msg("  You hit a {} and are toast.".format(Threat))
            self.player_pos = -1
            return (False)

        else:
            self.msg("  Worked.")
            self.player_pos = RoomNum
            return (True)

    def _shoot_path(self, Dir):
        """
        Shoot the arrow in the given direction till it hits a wall.
        In this case use the current position and iteratively add
        or subtract as needed.
        """

        # Set the update factor to deal with.
        if (Dir == "N"):
            Factor = -5
        elif (Dir == "S"):
            Factor = 5
        elif (Dir == "E"):
            Factor = 1
        elif (Dir == "W"):
            Factor = -1

        # Now handle the update till none is left.
        CurrPos = self.player_pos

        while (CurrPos != None):
            # Do the shooting.
            Threat = self.threats.get(CurrPos)

            # If it is the wumpus print a message, delete
            # it, and then return stopping the action.
            if (Threat == "wumpus"):
                self.msg(" Hurrah you killed the wumpus.")
                del self.threats[CurrPos]
                self.wumpus_pos = -1
                return (True)

            # Calculate the next position.
            Next = CurrPos + Factor

            if ((Next < 1)
                    or (Next > 25)
                    or (Next not in self.cave[CurrPos])):

                self.msg(" Wasted an arrow!")
                return (False)

            else:
                CurrPos = Next

            # # If this was your last arrow and it did not hit the wumpus...
            # if self.arrows < 1:		# This (or the updating of self.arrows) seems to be broken...
            #     self.msg("Your quiver is empty.")
            #     return(-1)

    # Output.
    # -------------------------------------------

    def msg(self, Message):
        """
        Print out the specified message if 
        the print_messages flag is set. 
        """
        if (self.print_messages == True):
            print(Message)

    def printBoard(self):
        """
        Print the board string.
        """
        print(self.makeBoardStr())

    def makeBoardStr(self):
        """
        Print out an ascii version of the board this happens
        in rows of 5 all the way down.  
        """

        # Everything will be dumped into the BoardStr
        # for later return or printing. 
        BoardStr = ""

        # Iterate over each row of our game board.
        for Row in range(0, 25, 5):

            # Generate the (initially empty) string for the row.
            RowStr = ""

            # Iterate over each column of the row.  
            for Col in range(1, 6):

                # Get the location itself.
                Pos = Row + Col

                # Start the string.
                RowStr += "{:2}:(".format(Pos)

                # Determine what features it has.
                if (Pos == self.player_pos):
                    if (self.has_gold):
                        RowStr += "!"
                    else:
                        RowStr += "1"
                else:
                    RowStr += " "

                if (Pos == self.gold_pos):
                    RowStr += "g"
                else:
                    RowStr += " "

                if (Pos in self.threats.keys()):
                    if (self.threats[Pos] == "wumpus"):
                        RowStr += "W"
                    else:
                        RowStr += "U"
                else:
                    RowStr += " "

                if (Pos == self.exit_pos):
                    RowStr += "x"
                else:
                    RowStr += " "

                # and close the item.
                RowStr += ") "

            # Having set the row shift to the next.
            BoardStr += RowStr + "\n"

        # And return the whole thing.
        return (BoardStr)

    # API for access to game
    # -------------------------------------------

    def get_curr_room(self):
        """
        Get the current room that the player is in.
        """
        return (self.player_pos)

    def pickup_gold(self):
        """
        Try to pick up the gold.  If the gold is here
        then set it.  If not then give an error.
        """
        if ((not self.has_gold)
                and (self.player_pos == self.gold_pos)):

            self.msg("Picking up gold.")

            self.has_gold = True
            self.gold_pos = -1
            return (True)

        else:
            self.msg("Can't pick up gold.")
            return (False)

    def shoot_dir(self, Dir):
        """
        This will fire in one of the directions: N,S,E,W.
        and will kill anything along the path. 
        """
        if (Dir not in ["N", "S", "E", "W"]):
            self.msg("Can't shoot unknown dir.")
            return (False)

        elif (self.arrows == 0):
            self.msg("Can't shoot what you don't have.")
            return (False)

        else:
            self.msg("Shooting an arrow to the {}...".format(Dir))
            Result = self._shoot_path(Dir)
            self.arrows -= 1
            return (Result)

    def go_dir(self, Dir):
        """
        Go in the specified direction if possible.
        """

        NewPos = self.player_pos  # if the agent can't move, have it stay where it is

        if (Dir == "N") and 6 <= self.player_pos:
            NewPos = self.player_pos - 5
        elif (Dir == "S") and self.player_pos <= 20:
            NewPos = self.player_pos + 5
        elif (Dir == "E") and self.player_pos % 5 != 0:
            NewPos = self.player_pos + 1
        elif (Dir == "W") and self.player_pos % 5 != 1:
            NewPos = self.player_pos - 1

        # Handle the odd corner cases. (shouldn't be necessary but they are a catch-all)
        # North out of 1
        if (NewPos == -4):
            NewPos = 21

        # West out of 1
        elif (NewPos == 0):
            NewPos = 5

        # South out of 25
        elif (NewPos == 30):
            NewPos = 5

        # East out of 25
        elif (NewPos == 26):
            NewPos = 21

        return (self._goto_room(NewPos))

    def exit(self):
        """
        Try to exit the game.
        """
        if (self.player_pos == self.exit_pos):
            if (self.has_gold == True):
                self.msg("Exiting game with gold.")
                return (True)
            else:
                self.msg("Exiting game without gold!")
                return (False)

        else:
            self.msg("Can't exit.")
            return (False)

    def action_wrapper(self, ActionStr):
        """
        Wrap up the actions as strings.
        """

        self.msg("ActionWrapper: {}".format(ActionStr))

        if (ActionStr == "GetRoom"):
            return (self.get_curr_room())

        elif (ActionStr == "PickupGold"):
            return (self.pickup_gold())

        elif (ActionStr == "ShootNorth"):
            return (self.shoot_dir("N"))

        elif (ActionStr == "ShootSouth"):
            return (self.shoot_dir("S"))

        elif (ActionStr == "ShootEast"):
            return (self.shoot_dir("E"))

        elif (ActionStr == "ShootWest"):
            return (self.shoot_dir("W"))

        elif (ActionStr == "GoNorth"):
            return (self.go_dir("N"))

        elif (ActionStr == "GoSouth"):
            return (self.go_dir("S"))

        elif (ActionStr == "GoEast"):
            return (self.go_dir("E"))

        elif (ActionStr == "GoWest"):
            return (self.go_dir("W"))

        elif (ActionStr == "Exit"):
            return (self.exit())

        else:
            self.msg("I don't know what that means.")
            return (False)

    def get_percepts(self):
        """
        Get the senses of what is around us in line with 
        the game mechanics.  This will check the neighboring
        positions and the current one (for gold or exit) and
        then assemble a set of senses.
        """

        # Generate an empty set for the percepts.
        PerceptSet = set([])

        # Check if there is gold here.  If so add it
        # to the current location.
        if (self.gold_pos == self.player_pos):
            PerceptSet.add("glint")

        # Check if the door is here and if so add it.
        if (self.exit_pos == self.player_pos):
            PerceptSet.add("exit")

        # Check the neighboring spaces for the pits or
        # the wumpus and if so add the breeze and the
        # stench.
        NeighboringPositions = [
            self.player_pos - 5, self.player_pos + 5,
            self.player_pos + 1, self.player_pos - 1]

        for NeighborPos in NeighboringPositions:

            # Check if the wumpus is here and add stench.
            if (NeighborPos == self.wumpus_pos):
                PerceptSet.add("stench")

            # Check if the pit is here and add breeze.
            if (NeighborPos in self.pits):
                PerceptSet.add("breeze")

        # Return the percepts.
        return (PerceptSet)
