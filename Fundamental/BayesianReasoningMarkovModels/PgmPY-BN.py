#!/usr/bin/env python
# =======================================
# Alarm Example Code.
# Copyright 2021: Collin F. Lynch
#
# This code provides a basic example of pgmpy usage with
# the alarm network used in the lectures.  When run it
# will generate a basic network, plot it, give tables,
# and let us run some simple inference. 

from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination
# Imports
# ========================================
from pgmpy.models import BayesianModel

# This call sets up the basic alarm network.  Here we
# are instantiating a BN class and giving it the variables
# as well as the parents of each variable.  Thus we
# specify "Burglary" as the variable and its parent "Alarm"

alarm_model = BayesianModel([('Burglary', 'Alarm'),
                             ('Earthquake', 'Alarm'),
                             ('Alarm', 'JohnCalls'),
                             ('Alarm', 'MaryCalls')])

# Now we specify the conditional probability tables for each
# of the variables.  Because we specified the parents above
# these tables are specied as lists of lists.
#
# Here we set the Burglary variable, which has cardinality (states)
# of 2 indicating two possible values.  And we set the odds of each
# value.  Because this variable has no parents there is only one
# number in each set with 0.999 indicating the odds of it being 0
# or false in this case and 0.001 chance of it being 1 or true.
# because we do not name the cardinality in this example we are
# only using numbers as a stand-in.

cpd_burglary = TabularCPD(
    variable='Burglary',
    variable_card=2,
    values=[[.999], [0.001]])

cpd_earthquake = TabularCPD(
    variable='Earthquake', variable_card=2,
    values=[[0.998], [0.002]])

# In this case Alarm has 2 parents so we need to specify the
# table of variables with the odds of it being 0 if they
# are both 0 (0.999), 0 if one is 1 and the other false (0.71)
# etc. This mirrors the example shown in the slides and the
# use of the evidence and evidence_card allows us to set the
# parent information.

cpd_alarm = TabularCPD(
    variable='Alarm', variable_card=2,
    values=[[0.999, 0.71, 0.06, 0.05],
            [0.001, 0.29, 0.94, 0.95]],
    evidence=['Burglary', 'Earthquake'],
    evidence_card=[2, 2])

cpd_johncalls = TabularCPD(variable='JohnCalls', variable_card=2,
                           values=[[0.95, 0.1], [0.05, 0.9]],
                           evidence=['Alarm'], evidence_card=[2])
cpd_marycalls = TabularCPD(variable='MaryCalls', variable_card=2,
                           values=[[0.99, 0.3], [0.01, 0.7]],
                           evidence=['Alarm'], evidence_card=[2])

# Since we defined the conditional probability tables for each
# of our variables as separate objects it is now necessary to
# associate them with the actual BN.  This code does that and
# links them based upon the variable names that we specified.

alarm_model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_johncalls, cpd_marycalls)

# We can perform a simple check to show if the model is valid here.
print(alarm_model.check_model())
print("\n")

# We can call these to get the variables and edges in the model
# in much the same way that we get the structure of a networkx
# graph.
print(alarm_model.nodes())
print(alarm_model.edges())
print("\n")

# This will then give us alol the independencies in the network.
# what this is doing is in fact using the same rules of d-separation
# to recognize pure and conditional independencies.
print(alarm_model.get_independencies())
print("\n")

# You can plot the model using networkx although that produces errors
# on some GUI displays.
import networkx as nx
import pylab

# nx_graph = nx.DiGraph(alarm_model.edges())   #lines 108 and 109 will run if 111 does not
# nx.draw(nx_graph, with_labels=True)

nx.draw(alarm_model, with_labels=True)  # this line may cause an error

pylab.show()

# And finally we can get some basic inference.  To do this we need to
# instantiate the variable elimination algorithm as an object and then
# make calls to it.
alarm_infer = VariableElimination(alarm_model)

# And get the output for John calling if Earthquake is 1.  Note this
# uses the same general model as the queries shown in the slides.
query = alarm_infer.query(variables=["JohnCalls"],
                          evidence={"Earthquake": 1}, show_progress=False)

print("\n")
print(query)
