import graphs as G

def spanningTree(start, end, N, D = None, parents = None):
   if parents is None: 
      parents = { start: None }
      D = { start }
   Dnew = { v for u in D for v in N(u) if v not in parents }
   if len(Dnew) == 0: return None
   parents.update( { u: G.arbitrary( v for v in N(u) if v in parents ) for u in Dnew } )
   if end in parents: return parents
   return spanningTree(start, end, N, Dnew, parents)

# modified from CAB203 code to detect None returned
def shortestPath(start, end, N):
   parents = spanningTree(start, end, N)
   if parents is None: return None
   return G.pathFromTree(parents, end)

def swap(puzzle, i, j):
   ret = list(puzzle)
   ret[i] = puzzle[j]
   ret[j] = puzzle[i]
   return tuple(ret)

def N(v):
   r = set()
   z = v.index(0)
   if z % 3 != 0:  r.add(swap(v, z, z - 1))  # Left
   if z % 3 != 2:  r.add(swap(v, z, z + 1))  # Right
   if z // 3 != 0: r.add(swap(v, z, z - 3))  # Up
   if z // 3 != 2: r.add(swap(v, z, z + 3))  # Down
   return r

def findMove(u, v):
   j = u.index(0)
   k = v.index(0)
   if k == j - 1: return 'Left'
   if k == j + 1: return 'Right'
   if k == j - 3: return 'Up'
   if k == j + 3: return 'Down'
   return None

def eightSolution(start):
   solved = (1, 2, 3, 4, 5, 6, 7, 8, 0)
   path = shortestPath(start, solved, N)
   if path is None: return None
   sequenceOfMoves = [ findMove(u,v) for u,v in zip(path[:-1], path[1:]) ]
   return sequenceOfMoves


if __name__ == '__main__':
   start = (1,5,6,3,0,4,2,8,7) # No solution
   print(eightSolution(start))
   start = (1,5,6,3,0,7,2,8,4) # Solvable
   print(eightSolution(start))
