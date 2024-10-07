# KanrenExample.py
# Copyright 2022: Collin F. Lynch
#
# This script will walk use through the use of Kanren to
# develop a logic program and to evaluate the code.  The
# goal of this work is to introduce the idea of a logic
# library and the way in which you build and evaluate a
# logic database for later use.

# Kanren is a logic programming library for Python that
# provides basic features similar to a full-grade language
# like Prolog.  It is designed to allow us to define sets
# of facts and rules, which are specialized types of facts.

# You will need to install kanren as part of Anaconda. Since
# it is not a default package you will need to open the
# console in Spyder or your chosen interface and issue the
# following command:

#    pip install kanren

# This will use the pip tool which is Python's default
# package manager to install Kanren from the Python
# Package Index.  This is a standard tool to access most
# native python packages.


# Once installed you can import Kanren directly to run the
# remainder of the code. 

import kanren

# Logic Programming Example.
# ---------------------------------------------------------

# Kanren allows us to handle basic database logic
# programming by declaring types of relationships.  To use
# a classic example due to the Kanren page we can declare
# a family structure.  In this case part of the line of
# polish monarchs (not F1).

# We define a new type of relationship between people in this
# case as a parent.

parent = kanren.Relation()

# Then we define a database of facts that represent the parens
# of polish nobility.  Each of these is an individual declaration
# that will be stored in the running database.  In this case each
# of the pairs will be treated as an example of the parent.  Thus
# in FOL terms we are declaring:

#  parent("Charles VII", "Theresea Sobieska"),
#  parent("Charles VII", "Maximilian II of Bavaria"),
# ...

kanren.facts(parent,
             ("Charles VII", "Theresea Sobieska"),
             ("Charles VII", "Maximilian II of Bavaria"),
             ("Theresea Sobieska", "John III Sobieski"),
             ("Maximilian II of Bavaria", "Ferdinand Maria of Bavaria"),
             ("Ferdinand Maria of Bavaria", "Maria of Austria"))

# Having declared that we can now run a query that is a test for a
# direct match.  In this case we declare a variable that will "hold"
# the match result and then we seek the parents of a given X.

X = kanren.var()

# Now we run a query seeking the parents of charles, either the first parent
# two of them, or all of them.

kanren.run(1, X, parent("Charles VII", X))
kanren.run(2, X, parent("Charles VII", X))
kanren.run(0, X, parent("Charles VII", X))

# Complex queries can involve multiple variables which we put together to
# form an implicit conjunction.  Here we are looking for any X that
# satisfies the parent of a parent of Charles relationship.

Y = kanren.var()

kanren.run(0, X, parent("Charles VII", Y), parent(Y, X))


# This lets us begin to form rules as python functions.
# We can then include these in a standard run.  Here "conde"
# is a conjunction declaring that both of these facts must
# be true.  While the syntax of this rule is odd it is in
# fact equivalent to the conjunctive normal form used in
# the Prolog logic programming language.  

def grandparent(X, Z):
    M = kanren.var()
    return (kanren.conde((parent(X, M), parent(M, Z))))


def great_grandparent(X, Z):
    M = kanren.var()
    return (kanren.conde((parent(X, M), grandparent(M, Z))))


kanren.run(0, X, grandparent("Charles VII", X))
kanren.run(0, X, great_grandparent("Charles VII", X))


# Conde can also provide an "or" construction by wrapping
# the goals into sublists.  Note that the items in the tuples
# must end in a comma or be a list of items to represent that
# they are iterable.  

def ancestor(X, Z):
    M = kanren.var()
    return (kanren.conde((parent(X, Z),),
                         (grandparent(M, Z),)))


# As you run each of these notice that all that the code is doing
# is seeking to map variables to values through unification to
# make the logical statements correct.  Through the conde, lall
# and related operations you can build up more complex FOL calls.


# Constraint Decisions.
# ------------------------------------------------
# We can also use Kanren to represent constraint problems.
# here we turn back to the basic zebra problem using an
# example defined here:
#  https://www.tutorialspoint.com/artificial_intelligence_with_python/artificial_intelligence_with_python_logic_programming.htm

# In this case the runes of the puzzle are these:
#  There are five houses.
#  The English man lives in the red house.
#  The Swede has a dog.
#  The Dane drinks tea.
#  The green house is immediately to the left of the white house.
#  They drink coffee in the green house.
#  The man who smokes Pall Mall has birds.
#  In the yellow house they smoke Dunhill.
#  In the middle house they drink milk.
#  The Norwegian lives in the first house.
#  The man who smokes Blend lives in the house next to the house with cats.
#  In a house next to the house where they have a horse, they smoke Dunhill.
#  The man who smokes Blue Master drinks beer.
#  The German smokes Prince.
#  The Norwegian lives next to the blue house.
#  They drink water in a house next to the house where they smoke Blend.

# Here we treat each of the houses as a set of variables
# representing the features.  And we define two of the relations
# between the features as left and right.

def left(X, Y, list):
    return kanren.membero((X, Y), zip(list, list[1:]))


def next(X, Y, list):
    return kanren.conde([left(Y, X, list)], [left(X, Y, list)])


# Now we can store all the rules in a single conjunction
# that is specified by the lall operator which specifies
# that all of the things listed must be true.  
Houses = kanren.var()

Zebra_Rules = kanren.lall(
    (kanren.eq, (kanren.var(), kanren.var(), kanren.var(), kanren.var(), kanren.var()), Houses),

    (kanren.membero, ('Englishman', kanren.var(), kanren.var(), kanren.var(), 'red'), Houses),
    (kanren.membero, ('Swede', kanren.var(), kanren.var(), 'dog', kanren.var()), Houses),
    (kanren.membero, ('Dane', kanren.var(), 'tea', kanren.var(), kanren.var()), Houses),
    (left, (kanren.var(), kanren.var(), kanren.var(), kanren.var(), 'green'),
     (kanren.var(), kanren.var(), kanren.var(), kanren.var(), 'white'), Houses),
    (kanren.membero, (kanren.var(), kanren.var(), 'coffee', kanren.var(), 'green'), Houses),
    (kanren.membero, (kanren.var(), 'Pall Mall', kanren.var(), 'birds', kanren.var()), Houses),
    (kanren.membero, (kanren.var(), 'Dunhill', kanren.var(), kanren.var(), 'yellow'), Houses),
    (kanren.eq, (
    kanren.var(), kanren.var(), (kanren.var(), kanren.var(), 'milk', kanren.var(), kanren.var()), kanren.var(),
    kanren.var()), Houses),
    (kanren.eq, (
    ('Norwegian', kanren.var(), kanren.var(), kanren.var(), kanren.var()), kanren.var(), kanren.var(), kanren.var(),
    kanren.var()), Houses),
    (next, (kanren.var(), 'Blend', kanren.var(), kanren.var(), kanren.var()),
     (kanren.var(), kanren.var(), kanren.var(), 'cats', kanren.var()), Houses),
    (next, (kanren.var(), 'Dunhill', kanren.var(), kanren.var(), kanren.var()),
     (kanren.var(), kanren.var(), kanren.var(), 'horse', kanren.var()), Houses),
    (kanren.membero, (kanren.var(), 'Blue Master', 'beer', kanren.var(), kanren.var()), Houses),
    (kanren.membero, ('German', 'Prince', kanren.var(), kanren.var(), kanren.var()), Houses),
    (next, ('Norwegian', kanren.var(), kanren.var(), kanren.var(), kanren.var()),
     (kanren.var(), kanren.var(), kanren.var(), kanren.var(), 'blue'), Houses),
    (next, (kanren.var(), 'Blend', kanren.var(), kanren.var(), kanren.var()),
     (kanren.var(), kanren.var(), 'water', kanren.var(), kanren.var()), Houses),
    (kanren.membero, (kanren.var(), kanren.var(), kanren.var(), 'zebra', kanren.var()), Houses)
)

# Finally to solve this we will get the solutions using the same
# kanren run operation which pulls the values as variable bindings.
#
# You will note in running this that it takes a noticeable amount
# of time.  This stems from the fact that the code is actually
# doing a search of possible binding

Solution = kanren.run(0, Houses, Zebra_Rules)

# The resulting solution is in fact a binding to the full set of variables
# representing all of the bindings for the house.  You can see this if
# you just print it.  This is essentially consistent with the database
# logic shown.  Since the result is just a tuple however we can actually
# pull out the desired answer by selecting the appropriate entry.

# Since the resulting list is just a tuple of tuples of strings we can
# use basic python code to find the desired match for the zebra.
# Similar code can be used to pull out other values as needed such
# as water.

for (Owner, Smokes, Drink, Pet, Paint) in Solution[0]:
    if (Pet == "zebra"):
        print(Owner)
