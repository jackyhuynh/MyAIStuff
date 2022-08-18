# ======================================
# Decision Support Code.
# Copyright: Dr. Collin F. Lynch
# 2021
#
# Sample decision support code to support decisionmaking. The
# classes here provide some guidance on the pieces.  Your task
# to build up the components into a decision graph.  What
# this code provides is a set of basic objects for doing the
# code and the calculations.


class DecRoot(object):
    """
    The DecRoot object is the root class for our 
    decisions and lotteries.  What it provides is
    an interface for the value.  All successors 
    have to implement the method.
    """

    

    def get_value(self):
        """
        In order to make the classes work every
        class must be able to return a value since
        that is part of how we get outcomes.
        """
        raise RuntimeError("Not Implemented")
    



class DecLeaf(DecRoot):
    """
    The decision Leaf class presents the endpoint 
    and is defined by an ID, and a static value 
    """


    def __init__(self, ID, Value):
        """
        Initialize with the ID and Value.
        """
        self.ID = ID
        self.Value = Value


    def get_value(self):
        """
        Return the static value.
        """
        return(self.Value)

    

class Decision(DecRoot):
    """
    The Decision class represents a choice over a set 
    of options.  The decision elements are a list of 
    objects which can be decisions or lotteries.  The
    object has the capacity to find the max choice,
    return an ID, and return its' value.
    """

    
    def __init__(self, ID, Choices):
        """
        Initialize with an ID and a list of choices.
        """

        self.ID      = ID
        self.Choices = list(Choices)



    def get_value(self):
        """
        The value of a decision node is the value 
        of the maximum choice on the assumption 
        that we will always pick the best.  Thus 
        we first find the max choice, then return
        its' value.
        """

        MaxChoice = self.get_max_choice()
        MaxValue  = MaxChoice.get_value()
        return(MaxValue)


    def get_max_choice(self):
        """
        Get the maximum value choice and return it.
        """
        
        Max    = self.Choices[0]
        MaxVal = Max.get_value()

        for Choice in self.Choices[1:]:
            NewVal = Choice.get_value()
            if (NewVal > MaxVal):
                Max    = Choice
                MaxVal = NewVal

        return(Max)
                

class Lottery(DecRoot):
    """
    The lottery class works as a simple lottery to calculate 
    the odds.  Each of the outcomes is represented as a 2-tuple
    that has the probability and the item.  Values are then
    calculated for each one.
    """

    
    def __init__(self, ID, Outcomes):
        """
        Initialize with an ID and a list of outcomes.
        """

        self.ID       = ID
        self.Outcomes = list(Outcomes)



    def get_value(self):
        """
        The value of a lottery is based upon multiplying 
        each of the outcomes by its probability and value
        and then returning the result.
        """
        CurrValue = 0

        for (Probability, Outcome) in self.Outcomes:

            NewValue  = (Probability * Outcome.get_value())
            CurrValue += NewValue

        return(CurrValue)



if __name__ == "__main__":

    Leaf1 = DecLeaf("A", 10)
    Leaf2 = DecLeaf("B", -12)

    DecTest = Decision("DecTest", [Leaf1, Leaf2])
    print(DecTest.get_max_choice().ID)
    print(DecTest.get_value())

    LotTest = Lottery("LotTest", [(0.1, Leaf1), (0.9, Leaf2)])
    print(LotTest.get_value())
