# -*- coding: utf-8 -*-
"""
Sample Stationary Bandit Skeleton.
Author: Dr. Collin F. Lynch

This code probides a basic skeleton for the 
stationary bandit code.  It should be adapted
by the students for their work.
"""


class BanditSet(object):
    """
    This object represents a set of arms for a stationary multi-armed 
    bandit problem it will store a fixed set of arms from a set and
    will then maintain them over multiple iterations.
    """

    def __init__(self, DataRows, ArmNames, ExpRate,
                 DistribParam, DecayRate, RewardWeight):
        """
        This initializes the set of choices by acting as a factory
        class to create one arm instance for each of the choices.
        The names and the rows will come from the file that 
        is read in. 
        """

        # Store the Data for later use.
        self.Data = DataRows

        # Initialize the parameters.
        self.ExplorationRate = ExpRate
        self.DistributionParameter = DistribParam
        self.DecayRate = DecayRate
        self.RewardWeight = RewardWeight

        # Store items for each of the arms.
        self.Names = ArmNames

        # Store a list for the weights.
        self.Weights = [-1 for I in len(ArmNames)]

        # Calculate the starting probability and add it.
        StartProb = 1 / float(len(ArmNames))
        self.Probabilities = [StartProb for I in len(ArmNames)]

        # And store the Cumulative Reward
        self.CumulativeReward = 0

    def handleRows(self):
        """
        Process each of the rows and update our running reward 
        and the basic probabilities for each one.
        """
        # We initialize the cumulative
        # Reward to be 0
        self.CumulativeReward = 0

        # Now iterate over the rows and make each
        # of the choices.
        for CurrRow in self.Rows:
            print("in a loop")
            # Now pick one from the list of probabilities.
            # Get the reward value from the row.
            # Update the reward weight.
            # And update the probabilities.

        # Return the cumulative reward.
        return self.CumulativeReward

    def pickArmIndex(self):
        """
        Pick an index based upon the probabilities
        using the cumulative score approach based
        upon a random value.
        """
        pass

    def getReward(self, Index):
        """
        Use the Armnames to get the reward for the 
        chosen arm.
        """
        pass

    def updateWeight(self, Index, Reward):
        """
        Update the weight for the chosen index using 
        the parameters.
        """
        pass

    def updateProbability(self, Index):
        """
        Update the probability for the index from its weight.
        """
        pass

    def normalizeProbabilities(self, Index, Reward):
        """
        Normalize the probability values.
        """
        pass
