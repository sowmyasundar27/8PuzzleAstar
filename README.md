# 8PuzzleAstar

The 8 Puzzle problem is the smaller version of the famous 15 puzzle Problem. To generate an 8 Puzzle problem, 3 by 3 grid is created with each tile having a random number from 1 to 8 and one blank spot (Empty or zero). We are given an initial state or the shuffled state & the goal state, Initial state will have numbers randomly placed on the 3*3 grid, we need to reach to the goal state, which can again be random state given in the problem or a sorted 8 Puzzle Board. The number of moves taken to solve the problem determines the effectiveness of the solution. We need to find the solution in least possible steps. We are going to take a look at one such algorithm, which is considered as the best algorithm to solve Sequential Problems like 8 Puzzle. 
 
What is A* Algorithm? 
In Computer Science A*, is an algorithm mainly used to solve sequential problems. Problems which include finding the path and traversing the path to reach to a solution in the least minimum cost possible. It finds the path from Initial State (Node 1) to Goal State (Node 2) in least number of steps and the shortest route possible. It is considered as the fastest Algorithm to partially visible graphs, it is slow as compared the algorithms who preprocess the graph and solve it. 
To solve problems using A* Algorithm we would need the Path Cost [g(n)] and a Heuristic Score [h(n)]. 
Path Cost [g(n)]: Also known as Step Cost. Each Step is given a cost and g(n) is addition of all the path costs. 
 e.g. – Consider path cost for A -> B = 14, from B -> C = 16 and C = Goal be 15, Let h(n)C -> Goal be 5 
 Therefore, f(n) = g(n) + h(n) = (14 + 16 + 15) + (5) = 50, Goal reached in 50 f(n) 
Heuristic Cost [h(n)]: Also know as desirability cost, derived from estimation. This cost can be calculated using different methods and each of the methods can give different cost for the same node path. 
 e.g. – Consider if we are finding the cost from A -> B, we are using Straight Line Distance as a Heuristic Function. 
 Then, h(n) = Distance (A -> B), which can be calculated mathematically or by using given facts. 
As A* Considers both Heuristic and Path Cost, it is able to derive the shortest path possible to the goal and reach the goal. 
 
Problem Formulation 
To Solve the 8 Puzzle Problem, given the Initial and Goal State, using A* Algorithm.  
1. To test it with different Heuristic to prove the which of the two is better for a particular case.  2. To prove the correctness of the algorithm. 
 
Initial State: The state of the 8 Puzzle Board in the beginning. 
2 8 1 3 4 6 7 5 0 
 
Goal State: The state of the 8 Puzzle Board we need to attain. 
3 2 1 8 0 4 7 5 6 
Goal Test: The procedure to determine if the goal is reached. 1. Check if Current State == Goal State. 2. If equal check f(n)current state. 3. Check if any other Node has f(n) less than f(n)current state. 4. If such f(n) exist traverse that f(n) to the Goal State (if possible). 5. When we have all the f(n) values to the goal state select the minimum of them and determine the path. 
 
 
