"""
@copywright Travis Martin AI academy
@author: TMartin
"""

import math
import networkx as nx
import pandas as pd

"""
This function will open a file:  infile
it will iterate through the file read in each line

roads from cities => Road_List
cities latitudes and longitudes => Lat_Long_Dict

returns:  Road_List and Lat_Long_Dict
"""


def open_file(in_file):
    Lat_Long_Dict = {}
    Road_List = []

    with open(in_file, 'r') as Input:

        count = 0
        The_File = Input.readlines()[:-1]
        for line in The_File:

            if line[0] == '%':
                count += 1

            line = line.replace(',', '')

            if count == 3 and len(line) > 1 and line[0] != '%':
                tempstring = line.split()
                Lat_Long_Dict[tempstring[0]] = float(tempstring[1]), float(tempstring[2])

            if count == 4 and len(line) > 1 and line[0] != '%':
                Road_List.append(line.strip().split())

    return Lat_Long_Dict, Road_List


"""
passes in a node list => Road_List
create a dataframe from the road list
creates a tree from the dataframe
return the created tree => G
"""


def create_tree(node_list):
    df = pd.DataFrame(node_list, columns=['City1', 'City2', 'Miles'])
    G = nx.from_pandas_edgelist(df, 'City1', 'City2', edge_attr='Miles')
    return G


"""
input:  a node, lat long dictionary, and goal city
compute:  the hueristic between the new_node and the goalcity
output:  stores the heuristic in the new_node object
"""


def call_heuristic(new_node, lats_longs, goalCity):
    lat1 = lats_longs[new_node.name][0]
    long1 = lats_longs[new_node.name][1]
    lat2 = lats_longs[goalCity][0]
    long2 = lats_longs[goalCity][1]

    total_distance = math.sqrt(
        (69.5 * (lat1 - lat2)) ** 2 + (69.5 * math.cos((lat1 + lat2) / 360 * math.pi) * (long1 - long2)) ** 2)
    new_node.heuristic = total_distance

    return


"""
input:  startcity, goalcity, typeofsearch, G(tree), lats_longs(dictionary)
calls search on a search object g
calls search based on the type of search
output:  none
"""


def callingSearch(startCity, goalCity, typeOfSearch, G, lats_longs):  # call the specific search algorithm
    g = Search()
    if typeOfSearch == "bfs":
        print("\nStarting BFS search:")
        g.bfs(startCity, goalCity, G)

    elif typeOfSearch == "dfs":
        print("\nStarting DFS search:")
        g.dfs(startCity, goalCity, G)

    elif typeOfSearch == "ucost":
        print("\nStarting uniform cost search:")
        new_node = Node('None', startCity)
        new_node.cost = float(0)
        g.queue.append(new_node)
        g.ucost(goalCity, G, new_node)

    elif typeOfSearch == "astar":
        print("\nStarting A Star Search:")
        new_node = Node('None', startCity)
        new_node.cost = float(0)
        call_heuristic(new_node, lats_longs, goalCity)
        g.queue.append(new_node)
        g.astar(goalCity, G, new_node, lats_longs)


"""
class node
used for search object when calling uniform cost and astar
parent = the parent of the current node
name = name of current node
cost = actual cost to get to the current node
heuristic = straight line distance from current node to goal city
"""


class Node(object):
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.cost = -1  # initialize to non sensical values
        self.heuristic = -1


"""
class search -> inherits node class
visited = a list of visited items
queue = used for bfs, ucost, and astar - items to be visited
stack = used for dfs - a list of items needing to be visited
neighborL = a list of neighbors of the current node
return_path = the path to go from start to goal city
"""


class Search(Node):
    def __init__(self):
        self.visited = []
        self.queue = []
        self.stack = []
        self.neighborL = []
        self.return_path = []

    """
    breadth first search
    input:  node(startcity), goal city, G(tree)
    interate through the tree in a breadth first fashion
    the traversal is performed with a queue
    function will output the return path for bfs and print it to the screen
    """

    def bfs(self, node, goalCity, G):
        self.visited.append(node)
        self.queue.append(node)
        self.node = str(node)
        self.neighborList = (G.adj[node])

        while self.queue:
            s = self.queue.pop(0)
            nList = self.getNeighbor(s)
            if (s == goalCity):
                # print("These are visited nodes\n >>>", self.visited, "\n")

                print("Found: ", goalCity, "")
                self.return_path.append(goalCity)
                self.find_path(goalCity)
                break
            else:
                self.visited.append(s)
                for neighbor in nList:
                    if neighbor not in self.visited and neighbor not in self.queue:
                        self.queue.append(neighbor)

    """
    depth first search
    input:  node(startcity), goal city, G(tree)
    interate through the tree in a depth first fashion
    the traversal is performed with a stack
    similiar to bfs above except it implements with a stack instead of a queue
    function will output the return path for dfs and print it to the screen
    """

    def dfs(self, node, goalCity, G):
        self.visited.append(node)
        self.stack.append(node)
        self.node = str(node)
        self.neighborList = (G.adj[node])

        while self.stack:
            s = self.stack.pop(0)
            nList = self.getNeighbor(s)
            if (s == goalCity):
                print("Found: ", goalCity, "")
                self.return_path.append(goalCity)
                self.find_path(goalCity)  # i did not debug this return path for dfs
                break
            else:
                self.visited.append(s)
                for neighbor in nList:
                    if neighbor not in self.visited and neighbor not in self.queue:
                        self.stack.insert(0, neighbor)

    """
    uniform cost search
    input:  goal city, G(tree), current_node
    Output: prints the path to goal and the total cost to the goal
    """

    def ucost(self, goalCity, G, current_node):
        print("Need to implement Uniform Cost Search...")

    """
    astar search
    input:  goal city, G(tree), current_node, latlongdict
    outputs: prints the path to goal and the total cost to the goal
    """

    def astar(self, goalCity, G, current_node, latlongdict):
        print("Need to implement A Star Search...")

    """
    input:  current node
    finds all neighbors of the current node
    checks to see if neighbors have already been visited
    returns list of neighbors
    """

    def getNeighbor(self, CurrNode):
        new_nodes = []
        inpt = str(CurrNode)
        neighbor = list(G.adj[inpt])
        for n in neighbor:
            if n not in self.queue:
                if n not in self.visited:
                    new_nodes.append(n)

        newNeighbor = new_nodes
        self.neighborL.append(new_nodes)

        return newNeighbor

    """
    input:  goal city
    iterates through the visited queue and finds the path from start to goal
    output:  path to goal from start city
    """

    def find_path(self, goalCity):
        currNode = goalCity
        neighbor = list(G.adj[currNode])

        for n in neighbor:
            if n == self.visited[0]:
                self.return_path.insert(0, n)
                print("Here is the path to the goal")
                print(self.return_path)
                break

            if n in self.visited and n not in self.return_path:
                self.return_path.insert(0, n)
                self.find_path(n)
                if self.return_path[0] == self.visited[0]:
                    break

    """
    input:  current node
    find the path from start to goal city
    use the parent of each node to find the path
    output:  path from start to goal
    """

    def cost_path(self, current_node):
        if current_node.parent == 'None':
            return

        self.return_path.insert(0, current_node.parent)
        for node in self.visited:
            if node.name == current_node.parent:
                self.cost_path(node)
                return
        return


if __name__ == "__main__":

    in_file = "Cities.txt"

    StartCity = "raleigh"  # choose a start and goal city
    GoalCity = "houston"

    lats_longs, roads_list = open_file(in_file)

    G = create_tree(roads_list)
    # nx.draw(G, with_labels=True, arrows=True)
    # plt.show()

    # this program will run through all the search algorithms including: bfs, dfs
    print("Starting Node: " + StartCity)
    for type_of_search in ['bfs', 'dfs', 'ucost', 'astar']:
        callingSearch(StartCity, GoalCity, type_of_search, G, lats_longs)
