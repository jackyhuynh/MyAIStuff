# -*- coding: utf-8 -*-
# NaiveBayse-BaseCode.py
# @copyright: Collin Lynch
#
# This code provides a rough skeleton for the object heirarchy
# of a Naive Bayes model.  You can use these objects to flesh
# out your development.


# Imports
# ===============================


# NB Structure
# ===============================
class Naive(object):
    """
    This class represents a basic Naive Bayes structure
    given the hypothesis variable and the evidence.
    """

    # Initialization
    # --------------------------------
    def __init__(self, SourceFile, HypothesisVariable):
        # General name storage.
        self.HypothesisVar = HypothesisVariable
        self.EvidenceVars = []

        # Storage of frequencies.  This will use 
        # dicts indexed by values.
        self.HypothesisFreqDict = {}
        self.EvidenceFreqDict = {}

        # Handle file loading.
        self.SourceFile = SourceFile
        self._load_source_file()

    def _load_source_file(self):
        """
        Given the source file name load it and add the values.

        Returns
        -------
        None.

        """

        # Open the source file.

        # For each row update counts for the variables.

        # Then based on that set the probabilities.

    # Now do calculations.
    # ------------------------------------------
    def get_hypothesis_values(self):
        """
        Return a list of the possible values
        for the hypothesis variable.

        Returns
        -------
        A list of strings.

        """
        Vals = list(self.HypothesisFreqDict.keys())
        return (Vals)

    def calculate_event_odds(self, HypothesisValue, EvidenceValues):
        """
        Given an event defined by a hypothesis value and a dict of the 
        values for the evidence what do you have?

        Parameters
        ----------
        HypothesisValue : String
            A value for the hypothesis.
            
        EvidenceValues : Dict
            A dict mapping one value to each piece of evidence.

        Returns
        -------
        A probability as a float.

        """
        pass

    def classify(self, EvidenceValues):
        """
        Given values for the evidence pick the most likely hypothesis value.

        Parameters
        ----------
        EvidenceValues : dict
         A dict mapping evidence variable names to value strings.

        Returns
        -------
        A most likely hypothesis value and a probability.

        """

        pass
