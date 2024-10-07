# SchedulingSkeleton.py
# Copyright 2021 Dr. Collin F. Lynch
#
# This provides skeleton code for the scheduling problem
# for Week 6 of the AI Academy course.  It provide a basic
# class structure for the problem and should be used as
# a guide for implementation.

import csv

# Imports
# ==================================

import re
import networkx
import matplotlib.pyplot as pyplot

# 
# ==================================

class SchedulingProblem(object):
    """
    This class wraps up the business of the scheduling problem
    for the sake of clarity.  On load it will pull in a problem
    file and then handle the calculations.  It has a built in 
    method to actually print the directed graph for the user.
    """
    
    # Initialization
    # ---------------------------------------
    
    def __init__(self, FileName):
        """
        Load in the specified file.  And generate
        the relevant storage.

        Parameters
        ----------
        FileName : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        # Generate storage.
        self.Graph = networkx.DiGraph()
        
        # Do the file loading.
        
        
        
    def __add_task(self, Name, Dur, ParentNames):
        """
        Add in the specified task 

        Parameters
        ----------
        Name : TYPE
            DESCRIPTION.
        Duration : TYPE
            DESCRIPTION.
        Parents : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        self.Grap.add_node(Name, Duration=Dur)
        for ParentName in ParentNames:
            self.Graph.add_edge(ParentName, Name)
    
    
    # Calculations
    # ---------------------------------------------
    
    def calc_es(self):
        """
        Calculate the early start of each item.
        

        Returns
        -------
        None.

        """
        
        # First set the ES of the start.
        self.Graph.nodes["start"]["ES"] = 0
        
        # Then we deal with the subsequent items.
        WorkingNodes = [self.Graph.nodes["start"].successors()]
        
        # Loop till the queue is done.
        
        
        
        
    def calc_node_es(self, NodeName):
        """
        Calculate the ES for the node.

        Parameters
        ----------
        NodeName : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        
        # Make sure all the parents are set.
        # Find the slowest parent.
        # Set my value.
        
        
        
        
        
    # Output
    # --------------------------------------------
    def drawgraph(self):
        """
        Draw out the graph for the user.

        Returns
        -------
        None.

        """
        
        networkx.draw(self.Graph, with_labels=True, arrows=True)
        pyplot.show()


if __name__ == "__main__":
    problems = SchedulingProblem('team')
    problems.drawgraph()