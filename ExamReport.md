Copyright **`(c)`** 2022 Diego Gasco `<diego.gasco99@gmail.com>`

# Report for Computational Intelligence final exam

# Contents
* [Introduction](#introduction)
* [Laboratory 1](#laboratory-1)
    * [Description](#description-lab-1)
    * [Code](#code-lab-1)
    * [Reviews received](#reviews-received-lab-1)
    * [Reviews done](#reviews-done-lab-1)
* [Laboratory 2](#laboratory-2)
    * [Description](#description-lab-2)
    * [Code](#code-lab-2)
    * [Reviews received](#reviews-received-lab-2)
    * [Reviews done](#reviews-done-lab-2)
* [Laboratory 3](#laboratory-3)
    * [Description](#description-lab-3)
    * [Code](#code-lab-3)
    * [Reviews received](#reviews-received-lab-3)
    * [Reviews done](#reviews-done-lab-3)
* [Personal implementations](#personal-implementations)
* [Final Project: Quarto Agent](#final-project-quarto-agent)
    * [Collaborations and thanks](#collaborations-and-thanks)
    * [The best strategy: Hardcoded](#the-best-strategy-hardcoded)
        * [Description](#description-hardcoded)
        * [Code](#code-hardcoded)
        * [Results](#results-hardcoded)
    * [An alternative tree search method: MonteCarlo Tree Search (MCTS)](#an-alternative-tree-search-method-montecarlo-tree-search-(mcts))
        * [Description](#description-mcts)
        * [Code](#code-mcts)
        * [Results](#results-mcts)
        * [References](#references-mcts)
    * [Let's try to mix: Genetic Algorithm](#lets-try-to-mix-genetic-algorithm)
        * [Description](#description-ga)
        * [Code](#code-ga)
        * [Results](#results-ga)
    * [A disappointing strategy: Reinforcement Learning](#a-disappointing-strategy-reinforcement-learning)
        * [Description](#description-rl)
        * [Code](#code-rl)
        * [Results](#results-rl)
    * [Final considerations](#final-considerations)


# Introduction

# Laboratory 1
## Description lab 1
<br>
Copyright **`(c)`** 2022 Diego Gasco `<diego.gasco99@gmail.com>`

### Set Covering problem

### Problem explanation
Given a number $N$ and some lists of integers $P = (L_0, L_1, L_2, ..., L_n)$, determine, if possible, $S = (L_{s_0}, L_{s_1}, L_{s_2}, ..., L_{s_n})$, such that each number between $0$ and $N-1$ appears in at least one list, and that the total numbers of elements in all $L_{s_i}$ is minimum.

### Algorithm used
For solving this problem I adopted a graph search strategy with an heuristic support. <br> 
Due to this hypothesis I implemented the A* algorithm.
The cost of each edge is measured by the length of the set added to reach a new state. <br>
The heuristic function that determines, added to the state's cost, the priority queue function, is the difference between the length of the goal state and the length of the actual state (a sort of Euclidean distance). <br>
The search implemented uses the concept of frontier and keeps track the parent and the cost of a certain node.

### Data Structures used
I decided to use one class called "State" to wrap the nodes of the graph visited by the A* algorithm. <br>
This class has two attributes: one set for the partial solution reached through this node, one set for the item (a set too) that has brought the path to this state. <br>
During the search steps, the function uses two dictionaries, one for keeping track the parent state of the current state and the other for keeping track the cost of the current state.

### Sources
I based my solution on the search algorithm written by Professor Giovanni Squillero in the Computational Intelligence course. <br>
The link to the code shared to us during the lectures is: https://github.com/squillero/computational-intelligence/blob/master/2022-23/8-puzzle.ipynb <br>
The solution was adapted for this specific problem. <br>
Also the library where is implemented the Priority Queue has been taken from Professor Squillero's repository at link: <br>
https://github.com/squillero/computational-intelligence/blob/master/2022-23/gx_utils.py

### Co-authors
I developed the code independently, but for some points about the algorithm or the Python language I compared my doubts with: Amine Hamdi, Enrico Magliano, Krzysztof Kleist and Giovanni Genna. <br>
They all are enrolled in Computational Intelligence course.

### Results
The original text of the task specifies to use a seed equals to 42 and N with the following values: 10, 20, 50, 100, 500, 1000. <br>
Due to few hardware resources I could try only with values that are smaller. <br>
Facing this fact, I added some cases less expansive to make richer the results section: <br>
* N = 5 &rarr; Found a solution in 3 steps; visited 21 states. The total weight is 5.
* N = 7 &rarr; Found a solution in 4 steps; visited 96 states. The total weight is 7.
* N = 10 &rarr; Found a solution in 4 steps; visited 750 states. The total weight is 16.
* N = 12 &rarr; Found a solution in 5 steps; visited 2,439 states. The total weight is 16.
* N = 15 &rarr; Found a solution in 4 steps; visited 9,831 states. The total weight is 19.
* N = 20 &rarr; Found a solution in 5 steps; visited 15,286 states. The total weight is 23.
* N = 25 &rarr; Found a solution in 4 steps; visited 1,095,111 states. The total weight is 33.
* N = 30 &rarr; Found a solution in 5 steps; visited 2,638,942 states. The total weight is 39.
<br>

### Another strategy: the greedy algorithms
Another strategy that I decided to implement is a best-first one using a greedy approach: the list of sets is sorted following the length of the sets and the first element of the list is the starting point. <br>
The strategy is based on the assumption that, smaller is the length of the starting point (and obviously also the sets'length inserted in the first steps to reach the goal), smaller will be the total weight at the end. <br>
This is actually not true, it is only an assumption to try to keep low the total weight. The solution is reached but it is not the best one. <br>
We can notice that also with huge numbers assigned to N, the greedy approach doesn't require a lot of hardware and time efforts. 

## Code lab 1

`lib.py` <br>
```python
import heapq

class PriorityQueue:
    """A basic Priority Queue with simple performance optimizations"""

    def __init__(self):
        self._data_heap = list()
        self._data_set = set()

    def __bool__(self):
        return bool(self._data_set)

    def __contains__(self, item):
        return item in self._data_set

    def push(self, item, p=None):
        assert item not in self, f"Duplicated element"
        if p is None:
            p = len(self._data_set)
        self._data_set.add(item)
        heapq.heappush(self._data_heap, (p, item))

    def pop(self):
        p, item = heapq.heappop(self._data_heap)
        self._data_set.remove(item)
        return item
```
`lab1.ipynb`
```python
import random
from lib import PriorityQueue
from typing import Callable

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

class State:
    def __init__(self):
        self.set_ = set()
        self.arrived_from = set()
    
    def __hash__(self):
        return hash(bytes(self.set_))

    def __eq__(self, other):
        return bytes(self.set_) == bytes(other.set_)

    def __lt__(self, other):
        return bytes(self.set_) < bytes(other.set_)

    def __str__(self):
        return str(self.set_)

    def __repr__(self):
        return repr(self.set_)
    
    def update_state(self, old_state, new_set):
        self.set_ = old_state.set_.copy()
        self.arrived_from = new_set.copy()
        self.set_.update(new_set.copy())

def search(
    generated_sets: list,
    initial_state: State,
    goal_test: Callable,
    parent_state: dict,
    state_cost: dict,
    priority_function: Callable,
    weight_cost: Callable,
):
    frontier = PriorityQueue()
    parent_state.clear()
    state_cost.clear()

    state = initial_state
    parent_state[state] = None
    state_cost[state] = 0

    while state is not None and not goal_test(state):
        for new_set in generated_sets:
            new_state = State()
            new_state.update_state(state, new_set)
            cost = weight_cost(new_set)
            if new_state not in state_cost and new_state not in frontier:
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                frontier.push(new_state, p=priority_function(new_state))
                #print(f"Added new node to frontier(cost={state_cost[new_state]})")
            elif new_state in frontier and state_cost[new_state] > state_cost[state] + cost:
                old_cost = state_cost[new_state]
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                #print(f"Updated node cost in frontier: {old_cost} -> {state_cost[new_state]}")
        if frontier:
            state = frontier.pop()
        else:
            state = None
    path = list()
    s = state
    while True:
        if s.set_ == set():
            break
        path.append(s.arrived_from)
        s = parent_state[s]
    weight = sum([len(item) for item in path])
    print(f"Found a solution in {len(path):,} steps; visited {len(state_cost):,} states")
    print(f"The total weight is {weight}")
    return list(reversed(path))

def greedySolution(
    generated_sets: list,
    initial_state: State,
    goal_test: Callable,
):
    generated_sets = sorted(generated_sets, key=lambda x: len(x))
    state = initial_state
    parent_state = list()
    flag_found = False

    for new_set in generated_sets:
        new_state = State()
        new_state.update_state(state, new_set)
        parent_state.append(new_state.arrived_from)
        if goal_test(new_state) == True:
            flag_found = True    
            state = new_state
            break
        state = new_state
    
    if flag_found == True:
        weights = [len(item) for item in parent_state]
        print(f"Found a solution in {len(parent_state)-1:,} steps; the total cost is: {sum(weights):,}")
        return parent_state
    else:
        print("Didn't find a solution")

def h(new_state: State):
    return len(GOAL.set_) - len(new_state.set_)
    
if __name__ == "__main__":
    flag_greedy = 0
    if flag_greedy == 0:
        N = [5, 7, 10, 12, 15, 20, 25, 30]
        SELECTED_N = N[4]
        GOAL = State()
        GOAL.set_ = set(range(SELECTED_N))
        INITIAL_STATE = State()
        result = problem(SELECTED_N, seed=42)
        sets_list = list()
        sets_list = [set(item) for item in result]
        parent_state = dict()
        state_cost = dict()
        final = search(
            sets_list,
            INITIAL_STATE,
            lambda s: s.set_ == GOAL.set_,
            parent_state,
            state_cost,
            priority_function=lambda s: state_cost[s] + h(s),
            weight_cost=lambda a: len(a),
        )
        print(final)
    else:
        GREEDY_SET = [10, 20, 50, 100, 500, 1000]
        GREEDY_N = GREEDY_SET[5]
        GREEDY_GOAL = State()
        INITIAL_STATE = State()
        GREEDY_GOAL.set_ = set(range(GREEDY_N))
        result = problem(GREEDY_N, seed=42)
        sets_list = list()
        sets_list = [set(item) for item in result]
        final = greedySolution(
            sets_list,
            INITIAL_STATE,
            lambda s: s.set_ == GREEDY_GOAL.set_,
        )
        print(final)
```

## Reviews received lab 1

* <b> Peer review - set covering by moDal7 </b><br>
    Thanks a lot for proposing your solution with such an exhaustive README document, explaining your solution in great detail, it has been highly informative reading it.

    In general, creating a for loop iterating over the various N for which we test the problem could help with streamlining the whole test; in this way a single run of the notebook could give you all the possible solutions, instead of changing the index value manually for each N value we want to test.

    It's worth noting that for the sake of readability and simplicity it's not that useful to use the

         if __name__ == "__main__":
    formula when using a .ipynb Jupyter notebook; you could just isolate the code contained in the main function and run it at will to reiterate tests.

    Greedy solution<br>

    The greedy solution is working well, but in some parts is maybe a bit overcomplicated, with respect to what it actually does.

    The greedy solution as it was implemented doesn't really benefit from the "state" architecture, since it just goes and add lists to the solution until it reaches the goal. It could be greatly simplified without the state class and the initial state variable.
    Since it is a task that is needed for any possible solution of the set covering problem, it might be a good scripting idea to create a function goal_test with global scope and use it repetitively instead of passing it as an argument of the function. It works the same way without distinction for the greedy solution and any other possible algorithm.
    I realise that the use of flag_found boolean variable, in the hypothesis that the problem has no solution. In that case it would be better to check this even before calling the function, just when the problem is generated, and then not use the flag found variable at all but just return the list of sets and possibly printing the log with the weights and steps as you did. It is good anyway that you made a more generalized version of the function, that works also in the possible cases in which the problem has no complete solution. 👍

    A* solution <br>

    FIrst of all, the heuristic function used in the priority evaluation seems admissible, so this is good. Also it seems a good idea to test the solution on more values in the area of magnitude where the problem doesn't "explode" computationally speaking, so kudos for that too 💯
    In the main function the lines where you create the problem and then make it a list of sets on multiple lines is vaguely redundant. It could be easier to reduce the number of variables to just one, where you have a sorted list of sets generated by the problem function
    In general the search function works well, and seems to use good logic; I am just a bit confused by the while True statement at the end of it which seems to not do much; maybe it's just something that was forgotten there.

* <b> Peer Review - lab1 by ben9809 </b><br>

    A Star Search <br>

    One feature could be implemented to speed up the computation:

    In function search(...) at line 20, every time the cycle is executed, after the first time, you'll get states (nodes) that have already been discovered (inside state_cost variable), so what could be done is just to create a function that from the generated_sets (the global list of all possible sets) just filter sets which states (nodes) aren't part of the local state discovered at the previous cycle.
    All the rest works great!!
    Keep up the good work!

* <b> Lab 1 - Peer Review (s304992) by lucavillanigit </b><br>

    General Comments

    The strategy used leads to good results but has a problem to tackle large N problems, this is because the A* is not so effective for large N, you could have tried to use a 'weight_cost = lambda a: 1' that leads to sub-optimal solutions but can compute larger N in a reasonable amount of time.
    The README is very well detailed and exhaustive, the only thing i would say is that since you used 2 different algorithms, inserting the results of the greedy could have lead to a more simple comparison between the 2 algorithms.
    The code is not commented at all, even though the README was very exhaustive i would have liked more details in the code on which do what and why. <br>

    Minor Issues

    I would have liked to know how actual time (milliseconds/seconds) your algorithm would have taken, for both the algorithms in order to understand if one solution was faster then other

## Reviews done lab 1

* <b> Lab1 Review using Issues by Diego Gasco (s296762) </b><br>

    REVIEW BY DIEGO GASCO (DIEGOMANGASCO) <br>

    SET COVERING (NOT GREEDY): <br>

    MAJOR: <br>
    The idea of counting how many elements are already present in the solution and take the result as a cost is good.
    The division that you made in the cost function to avoid bias by the earlier attempts, maybe is not necessary (I tried to put it off and the algorithm seems work in the same way).

    Removing duplicates from the list of sets at the beginning can be a good thing to speed up the process, especially with large N.

    For the priority queue you used a priority cost made by subtracting "cost" from "N".
    The lowest priority comes out of the queue first.
    In your implementation, an element with lower costs will produce an higher number due to "N-cost", but we want that the element goes in the front of the queue, because the cost is low.
    I tried to change the priority function with only "cost" and for N=20, the elements in the solution are 26 (instead of 46).

    Basing on my results, solutions are not optimal (they have a lot of nodes, reached through a lot of states), so the approach used can be consider first-fit and not best-fit.

    MINOR: <br>
    N is not defined in the frontier's "put" in the search function.

    Why did you use another dictionary "state_elems"? You could easily iterate backward in the "parent_state" dictionary from the latest state that brought you to the solution, to the first one to have all the sets in your solution. Then you can measure the length of this latter.

    SET COVERING (GREEDY): <br>

    Your greedy solution is very fast and the results are good.
    At the beginning of the function "find_best", you could pop the longest set by sorting the "listlist" and taking the first element.

    Your solution, since it is greedy, is not an optimal one in all cases for the set covering problem, because you don't explore the entire group of solutions.
    But it is a very good approach, the heuristics that you used for finding the set to add is nice!

    The results are not so far from the optimal ones and the speed is very good!

* <b> Lab1 Review using Issues by Diego Gasco (s296762) </b><br>

    REVIEW BY DIEGO GASCO (DIEGOMANGASCO) <br>

    SET COVERING (GREEDY): <br>

    I appreciated a lot the comparison between the professor's Naive greedy approach and your greedy approach!
    The idea to implement a sort of priority function to choose the best set to add to the solution is nice (a kind of cherry picking).
    I think you decided to take the set with lowest "f" because you want to keep low the total weight as you can.
    What if you merge this idea with the number of new elements that the new set can bring to your solution?
    You can try to find a sort of trade-off between having a new small set and having a new useful one!

    SET COVERING (A* TRAVERSAL USING PRIORITY QUEUE): <br>

    In my implementation I basically used the same approach in developing my A* algorithm!
    Like you, I decided to implement my heuristics as the number of undiscovered elements, and I took as cost, the length of the new set added in the solution.
    I also noticed that, with cost sets as unit and not as the length of the new set, the process is much faster, but the solution that we reached is not optimal, so I decided to keep the length as cost.

    The only small difference with my implementation is the use of the data structures.
    To don't have to deal with list manipulation, I preferred to focused my structures in a more set-oriented way.
    But never mind, these are just personal preferences!

    SET COVERING (A* TRAVERSAL USING A FULLY CONNECTED GRAPH): <br>

    Unfortunately I couldn't try this implementation of A*, because I didn't understand the data structure "adjacency_list" and there isn't a block that starts this piece of code like for the previous solutions :(
    Reading your explanation about the algorithm idea, I can say that this approach can be useful with a solution space that is not huge, but can become computationally expansive with large N (due to the connections you might have to manage).
    Bu anyway with small/medium N it can be helpful in reducing the time of the classical A*.


## Laboratory 2
### Description lab 2
### Code lab 2
### Reviews received lab 2
### Reviews done lab 2

## Laboratory 3
### Description lab 3
### Code lab 3
### Reviews received lab 3
### Reviews done lab 3
