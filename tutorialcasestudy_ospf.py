from graphs import *

def adjacencyListToGraph(adjacencyList):
   V = set(adjacencyList.keys())
   E = { (u, v) for u, Nu in adjacencyList.items() for v in Nu}
   return V, E

def firstHop(V, E, start, end):
   path = solveSpp(V, E, start, end)
   return path[1] if len(path) > 1 else None

def routingTable(V, E, u):
   return {v: firstHop(V, E, u, v) for v in V }

def solveRTP(adjacencyList, u):
   V, E = adjacencyListToGraph(adjacencyList)
   return routingTable(V, E, u)

if __name__ == "__main__":
   neighbours = {
      "A": { "B", "D" },
      "B": { "A", "C", "D" },
      "C": { "B", "D", "E" },
      "D": { "A", "B", "C" },
      "E": { "C" }
   }
   print(solveRTP(neighbours, "A"))