# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    initState = problem.getStartState()
    fringe = util.Stack()
    visited = []

    #Checking whether the initial state is goal state
    if(problem.isGoalState(initState)):
        return []

    fringe.push((initState, []))

    #iterating through elements in fringe
    while(not fringe.isEmpty()):
        currNode = fringe.pop()
        nodeCoor = currNode[0]
        nodePath = currNode[1]

        #processing node if not visited yet
        if nodeCoor not in visited:

            visited.append(nodeCoor)

            #checking whether the current processing is node is goal state or not
            if(problem.isGoalState(nodeCoor)):
                return nodePath

            #finding all the successors/adjacent nodes
            adjacentNodes = problem.getSuccessors(nodeCoor)

            #fetching next move information
            #populating fringe
            for node in adjacentNodes:
                nodeCoor = node[0]
                nodeNextMove = node[1]
                tempNodePath = list(nodePath)
                tempNodePath.append(nodeNextMove)
                fringe.push((nodeCoor, tempNodePath))

    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    initState = problem.getStartState()
    fringe = util.Queue()
    visited = []

    #checking if the initstate is goal state
    if(problem.isGoalState(initState)):
        return []

    fringe.push((initState,[]))
    visited.append(initState)

    #interating fringe elements till fringe is not empty
    while(not fringe.isEmpty()):
        currNode = fringe.pop()
        nodeCoor = currNode[0];
        nodePath = currNode[1];

        #checking current processed is goal or ot
        if(problem.isGoalState(nodeCoor)):
            return nodePath

        #pushing all the successor nodes of currnet processed node
        # pushing them to visited node
        for node in problem.getSuccessors(nodeCoor):
            nodeCoor = node[0]
            nodeNextMove = node[1]
            nodeTempPath = list(nodePath)

            if(nodeCoor not in visited):
                nodeTempPath.append(nodeNextMove)
                visited.append(nodeCoor)
                fringe.push((nodeCoor, nodeTempPath))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    initState = problem.getStartState()
    fringe = util.PriorityQueue()
    visited = []

    if(problem.isGoalState(initState)):
        return []

    #taking state as position, current traversed path, total cost of that path
    fringe.push((initState,[], 0), 0)

    while(not fringe.isEmpty()):
        currNode = fringe.pop()
        nodeCoor = currNode[0];
        nodePath = currNode[1];
        nodeCost = currNode[2];

        #Processing the node if not already processed
        if nodeCoor not in visited:
            visited.append(nodeCoor)

            #checking if the current processed node is goal or not
            if(problem.isGoalState(nodeCoor)):
                return nodePath

            #fetching all the successor of the current processed nodes
            for node in problem.getSuccessors(nodeCoor):
                nodeCoor = node[0]
                nodeNextMove = node[1]
                nodeOprCost = node[2]
                nodeTempPath = list(nodePath)
                nodeTempCost = nodeCost

                #calculating the current successor path and path cost to push in fringe
                nodeTempPath.append(nodeNextMove)
                nodeTempCost += nodeOprCost
                fringe.push((nodeCoor, nodeTempPath, nodeTempCost), nodeTempCost)

    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    initState = problem.getStartState()
    fringe = util.PriorityQueue()
    visited = []

    if (problem.isGoalState(initState)):
        return []

    #node item pushing in fringe is ((position, corners eaten), path list, path cost)
    fringe.push((initState, [], 0), 0)

    while (not fringe.isEmpty()):
        currNode = fringe.pop()
        nodeCoor = currNode[0];
        nodePath = currNode[1];
        nodeCost = currNode[2];
        if nodeCoor not in visited:
            visited.append(nodeCoor)

            #checking if popped out node is goal or not
            if (problem.isGoalState(nodeCoor)):
                return nodePath

            for node in problem.getSuccessors(nodeCoor):
                nodeCoor = node[0]
                nodeNextMove = node[1]
                nodeOprCost = node[2]
                nodeTempPath = list(nodePath)

                #Appending the current move to node path
                #Calculating the path cost
                #Calculating the total path cost by including heuristic cost as well
                #Pushing item to fringe
                nodeTempPath.append(nodeNextMove)
                nodeTempCost = problem.getCostOfActions(nodeTempPath);
                nodeTempCostPlusHeuristic = nodeTempCost + heuristic(nodeCoor, problem)
                fringe.push((nodeCoor, nodeTempPath, nodeTempCost), nodeTempCostPlusHeuristic)

    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
