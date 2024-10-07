# ==============================================
# Basic import of the networkx library.
import networkx
import matplotlib.pyplot as plt


# Static Directed Graph
# ==============================================
# Generate a simple fixed undirected graph.
# In this case we are adding in the nodes and
# edges to the graph manually to make a tree.
NewGraph = networkx.Graph()
NewGraph.add_nodes_from(range(10))
NewGraph.add_edges_from(
    [(0,1), (0,3), (0,5), (2,3), (3,5),
     (3,8), (3,9), (4,7), (4,9), (5,9),
     (6,8), (8,9)])

# This code generates a basic plot for the graph and then
# shows the resulting graph value.
networkx.draw(NewGraph,
              with_labels=True,
              arrows=False)
plt.show()



# Accessing the members of a graph is straightforward.
# The actual contents are kept in special view items
# but they can be converted to lists.
NodeList = list(NewGraph.nodes)
EdgeList = list(NewGraph.edges)

for NeighborNode in NewGraph.neighbors(3):
    print(NeighborNode)

    




# Static Undirected Graph
# ====================================================
# Generating a directed graph is a matter
# of changing the type.
NewDiGraph = networkx.DiGraph()
NewDiGraph.add_nodes_from(range(10))
NewDiGraph.add_edges_from(
    [(0,1), (0,3), (0,5), (2,3), (3,5),
     (3,8), (3,9), (4,7), (4,9), (5,9),
     (6,8), (8,9)])


networkx.draw(NewDiGraph,
              with_labels=True,
              arrows=False)
plt.show()



# Accessing the members of a graph is straightforward.
# The actual contents are kept in special view items
# but they can be converted to lists.
NodeList = list(NewDiGraph.nodes)
EdgeList = list(NewDiGraph.edges)

# Notice in this case the directed nature of the graph
# restricts what we will see as the neighbors to the
# outgoing arcs.
for NeighborNode in NewDiGraph.neighbors(3):
    print(NeighborNode)

    

# Finally we can generate a random graph using built in algorithms.
# We will use these to provide a simple search space.  The first
# generates a clear balanced tree, while the second generates a
# more complex pseudofractal graph.  Note the primary argument is
# exponential growth so stay to single digits.
BalancedTree = networkx.generators.classic.balanced_tree(4,3)
networkx.draw(BalancedTree,
              with_labels=True,
              arrows=False)
plt.show()


RandomDGMGraph = networkx.generators.dorogovtsev_goltsev_mendes_graph(5)
networkx.draw(RandomDGMGraph,
              with_labels=True,
              arrows=False)
plt.show()
