# Dijkstra: Shortest Reach

Given an undirected graph and a starting node, determine the lengths of the shortest paths from the starting node to all other nodes in the graph. If a node is unreachable, its distance is -1. 

Nodes will be numbered consecutively 1 from to n, and edges will have varying distances or lengths.

For example, consider the following graph of 5 nodes:

```
Begin	End	Weight
1	2	5
2	3	6
3	4	2
1	3	15
```

![alt text][graph1]
__
Starting at node 1, the shortest path to 2 is direct and distance5. 
Going from 1 to 3, there are two paths: 1 -> 2 -> 3 at a distance of 5+ 6 or 1 -> 3 at a distance 15. 
Choose the shortest path, 11. 

From to 1 to 4, choose the shortest path through 3 and extend it 1 -> 2 -> 3 -> 4: for a distance of 11 + 2 = 13. 

There is no route to node 5, so the distance is -1.

The distances to all nodes in increasing node order, omitting the starting node, are 5 11 13 -1.

##Function Description

Complete the shortestReach function in the editor below. It should return an array of integers that represent the shortest distance to each node from the start node in ascending order of node number.

shortestReach has the following parameter(s):

 * n: the number of nodes in the graph
 * edges: a 2D array of integers where each edges[i] consists of three integers that represent the start and end nodes of an edge, followed by its length
 * s: the start node number

## Input Format

The first line contains t, the number of test cases.

Each test case is as follows:
*  The first line contains two space-separated integers n and m, the number of nodes and edges in the graph.
*  Each of the next lines contains three space-separated integers x, y, and r, the beginning and ending nodes of an edge, and the length of the edge.
*  The last line of each test case has an integer s, denoting the starting position.

#Output Format

For each of the t test cases, print a single line consisting n- 1 space separated integers denoting the shortest distance to the n-1 nodes from starting position s in increasing order of their labels, excluding s.

For unreachable nodes, print -1

###Sample Input

```
1
4 4
1 2 24
1 4 20
3 1 3
4 3 12
1
```

###Sample Output

```
24 3 15
```

###Explanation

The graph given in the test case is shown as :

![alt text][graph2]

The lines are weighted edges where weight denotes the length of the edge.

The shortest paths followed for the three nodes 2, 3 and 4 are as follows :

- 1/S->2 - Shortest Path Value : 24
- 1/S->3 - Shortest Path Value : 3
- 1/S->3->4 - Shortest Path Value : 15 


[graph2]: djikstraexample_1.png 
[graph1]: djikstraexample_0.png 