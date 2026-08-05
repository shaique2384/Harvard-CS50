# Agent: An entity that perceives its environment and acts upon the environment.
# State: A configuration of the agent and its environment. A context which requires unique set of actions to achieve a goal.
# Initial State: The state in which the agent begins. From this state the agent will start reaning about the environment and how to achieve its goals.
# Actions: Choices that can be made in a state. In AI we are always going to formalize these ideas little bit more precisely and a little bit more mathematically.
## We are more precisely going to define the actions in terms functions. 
## ACTION(s) returns the set of actions that can be executed in state s.
## An ACTION() will take a state as input and return a set of actions that can be executed in that state.
## Some actions may be available in some states but not in others. For example, if the agent is in a state where it is standing in front of a door, it may have the action "open door" available. However, if the agent is in a state where it is standing in front of a wall, the action "open door" would not be available.
## So somehow our AI program need some encoding of the state which will often going to be some numerical format of some encoding of these actions.
## But it also needs some encoding of the relationships[conditionals?] between them.
# Transitional Model: A description of what state results from performing any applicable action in any state.
# Formal definition, RESULT(s, a) returns the state resulting from performing action a in state s.
# RESULT(s, ACTION(s)) returns the set of states that can result from performing any applicable action in state s.
# Actions can be represented as a number or an enum that allows us to enumerate multiple possibilities.
# Enumerate is just an iteration that automatically tracks and returns the index alongside each item.
# In English: If you "enumerate" your reasons for quitting a job, you don't just say "I have reasons." 
## You list them out loud: "First, the pay. Second, the commute. Third, the hours." You are naturally numbering them as you speak.
## i.e,

if False:
    items = ['a', 'b', 'c']

    # Iterating (Values only)
    for item in items:
        print(item)

    # Enumerating (Index + Value)
    for index, item in enumerate(items):
        print(index, item)

# The state can be represented as an array, 2d array, tensor or geometrinc manifold. The state can be represented as a number or an enum that allows us to enumerate multiple possibilities.
# The return value of RESULT(s, a) is the transition model. The transition model is a function that takes a state and an action as input and returns the resulting state. The transition model can be represented as a table, a function, or a set of rules. The transition model can be deterministic or stochastic. In a deterministic transition model, the resulting state is always the same for a given state and action. In a stochastic transition model, the resulting state is probabilistic and can vary for a given state and action.
# If we take this transition model and think about it more generally across the entire problem we can form what we call a state space. A state space is a set of all possible states that can be reached from the initial state by any sequence of actions. The state space can be represented as a graph, where the nodes are the states and the edges are the actions that connect them. The state space can be finite or infinite, depending on the problem. In a finite state space, there are a limited number of states that can be reached, while in an infinite state space, there are an unlimited number of states that can be reached.
# State Space: the set of all possible states reachable from the initial state by any sequence of actions.
# It's like an universal set of all possible states that can be reached from the initial state by any sequence of actions. The state space can be represented as a graph, where the nodes are the states and the edges are the actions that connect them. The state space can be finite or infinite, depending on the problem. In a finite state space, there are a limited number of states that can be reached, while in an infinite state space, there are an unlimited number of states that can be reached.
# We can simplify the state space set as a graph, some sequence of nodes and edges that connect them. The nodes are the states and the edges are the actions that connect them. The state space can be finite or infinite, depending on the problem. In a finite state space, there are a limited number of states that can be reached, while in an infinite state space, there are an unlimited number of states that can be reached.
# The node bubbles are the states and the edges with direction are the actions that connect them. The state space can be finite or infinite, depending on the problem. In a finite state space, there are a limited number of states that can be reached, while in an infinite state space, there are an unlimited number of states that can be reached.
# Next step is for the AI to know that the GOAL has been achieved.
# Goal Test: A way to determine wheather a given state is a goal state. The goal test can be represented as a function that takes a state as input and returns a boolean value indicating whether the state is a goal state. The goal test can be simple or complex, depending on the problem. In a simple goal test, the state is compared to a predefined goal state, while in a complex goal test, the state is evaluated based on multiple criteria.
# In some problems there can be one goal state, while in others there can be multiple goal states. In some problems, the goal test can be simple, while in others it can be complex. In some problems, the goal test can be deterministic, while in others it can be stochastic. In some problems, the goal test can be static, while in others it can be dynamic. In some problems, the goal test can be complete, while in others it can be incomplete.
# Sometimes the computer doesn't only care about only finding a goal but also finding a goal well., the one with a low cost.
# The last piece of terminology that we will use to define these search problem.
# Path Cost: Numerical cost associated with a given path. Remember the veritasium video.

# the first problem in the lecture is a search problem of 15 puzzle where states are diffferent configuration of puzzles and actions are moving 4 fold.
# The cost is not affected by right or left but the total number of actions as less action is less expensive and preferable.
# So all of the actions have a constant cost like 1

# Search Problems
## initial state
## actions
## transition model
## goal test
## path cost function

# The goal ultimately is to find a solution
# Solution: A sequence of actions that leads from the initial state to a goal state
# Optimal Solution: A solution that has the lowest path cost among all solutions. It simply means that there are no way we could find a better solution.

# To solve this problem our computer is going to need ro represent a whole bunch of data about this particular problem
# We need to represent data about where we are in the problem and we need to consider multiple solutions simultaneously
# To do so oftentime we will be trying to package a whole bunch of data related to a state together using a data structure called a node

# Node: A data structure that keeps track of, [for this search problem]
## A state
## A parent (a state that caused this state)
## An action (action applied to parent to get node)
## A path cost (from initial state to node, represented by a number, almost like a resistance value)(Optimization) [Remember the veritasium video?]
#### nodes and states can be synonymous

# Once we reach the goal we need to know what sequence of actions we used in order to get here
# We will knnow that by comparing it with the parent
# We can also back track upto the begining
# The path cost number can be analogous to the idea of using math patterns to compose new style of music

# Approach
## We are going to start from a particular state and we are going to explore from there
## The intuition is that from a given state we have multiple options that we can explore
## While exploring those options we will find out that even more options are available
## We are going to consider all of the available options to be stores inside of a single data struction that we will call frontier

# Frontier: Frontier is going to represent all of the things that we could explore next, that haven't been explored yet

# To start with our start problem let's start with a frontier that contains the initial state, the only state we know about
# Then our search algorith is effectively going to follow a loop repeatedly
# Repeat:
## If the frontier is empty then there is no solution, no way to reach the goal
#### If the AI concludes  that there is absolutely no way mathmatically to reach the goal state, that's a useful information as well
## Next AI will remove a node from the frontier 
#### Initially the frontier has only one node but overtime the frontier might grow multiple states
#### In that case we are going to remove a single node from that frontier
## If the node at the brink of removal contains the goal state, return the solution
## We will figure that out by applying the goal test


