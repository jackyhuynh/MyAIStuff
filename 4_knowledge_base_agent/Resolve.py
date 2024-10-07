# First we define a data structure for statements.
# When given an individual statement (e.g. (-a or b))
# we need to convert it into a single unified form
# for execution of the algorithm.
#
# The simplest structure for this would be a tuple which
# represents all of the variables as true, false or absent
# that can be done with a simple -1, 0, 1 encoding.
# so if we have say 5 variables then the following logic
# statments: (-a or b) (-b or -c or d) would be translated as:

Statement1 = (-1, 1, 0, 0, 0)
Statement2 = (0, -1, -1, 1, 0)

# Performing resolution on the two tasks would then be a
# matter of first checking that they only differ by one
# and then going through and keeping the singleton variable.

def check1off(StatementA, StatementB):
    """
    Check that the two statements are 1 off.
    through a simple for loop.
    """
    Count = 0
    
    for Index in range(len(StatementA)):

        Aval = StatementA[Index]
        Bval = StatementB[Index]
        print("Checking Index {} {} {}".format(Index, Aval, Bval))

        # Simple mask check for 0.
        if ((Aval != 0) and (Aval + Bval == 0)):
            Count += 1

        # Short circuit the loop if needed.
        if (Count > 1):
            return(False)

    # Indicate success.
    return(True)


# Having implemented the difference then handle the production
# of a new statement.  This uses a list for efficiency.
def resolveStatements(StatementA, StatementB):
    """
    Resolve a pair of statements, and yield a new example.
    """

    # Generate as a list for addition.
    NewStatement = []

    for Index in range(len(StatementA)):

        Aval = StatementA[Index]
        Bval = StatementB[Index]
        
        # NewStatement.append(Aval + Bval)
        if (Aval + Bval) > 1:
            NewStatement.append(1) 
        elif (Aval + Bval) < -1:
            NewStatement.append(-1)
        else:
            NewStatement.append(Aval + Bval)

    return(tuple(NewStatement))


# Now we can show the effect of these with different
# statements.
Statement3 = (-1, -1, 0, 0, -1)


print("\nChecking 1 and 2")
print(check1off(Statement1, Statement2))
print("\nChecking 1 and 3")
print(check1off(Statement1, Statement3))
print("\nResolving 1 and 2")
print(resolveStatements(Statement1, Statement2))


# The primary advantage of the tuple is that it is immutable
# and thus uses less space and is more efficient for iteration
# due to memory structures.  However that effect is nullified
# if we have a sparse variable space with a lot of possible
# variables few of which are present.  At that point a dict
# structure would be more efficient.
#
# How would you represent it as a dict?  And how would the code
# above need to change?



    
