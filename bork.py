import graphs
import digraphs

# You can define some helper functions here if you like!
def breadthFirstBork(V, E, map):
     V0 = V              # V_0 = V
   D = [ {u} ]         # D[0] = D_0 = {u}
   return distanceClassesR(V0, E, D)



def breadthFirstBorkR(V, E, map):
   Vnew = V - D[-1]            # V_{j} = V_{j-1} / D_{j-1}
   if len(Vnew) == 0: return D # Already considered all elements?
   Dnew = D + [ NS_out(Vnew, E, D[-1]) ]  # D_{j} = N_{V_j}(D_{j-1})
   return distanceClassesR(Vnew, E, Dnew)

   saveNo = bork.save()
   oldLoc
   for e in exits :
      bork.move(e)
      newloc = bork.description
      if newloc in set(map.keys()):
         bork.restore(saveNo)
      else:
         breadthFirstBorkR(bork, map)


def traverseBork(bork):
   # code your solution here

   map = {}
   bork.__init__()

   E = bork.exits()

   breadthFirstBorkR(bork, map)

   saveNo = bork.save()
   exits = bork.exits()
   
   //visit exit
   //if 

   # Access the bork automator like so:
   bork.restart()
   location = bork.description()
   exits = bork.exits()
   exit = "???"
   bork.move(exit)
   saveGame = bork.save()
   bork.restore(saveGame)

   # Access functions from the imported files like this:
   n = graphs.N(V, E, u)
   t = digraphs.topOrdering(V, E)

   return map

# To play in hard core mode, define the function traverseBorkHardCore(bork)
# You shoud also define traverseBork either way!
# def traverseBorkHardCore(bork):

# The following will be run if you execute the file like python3 bork_n1234567.py
# Your solution should not depend on this code.
if __name__ == "__main__":
   import borkAutomator
   bork = borkAutomator.Bork()
   print(traverseBork(bork))

   try:
      borkHC = borkAutomator.Bork(hardCore=True)
      print(traverseBorkHardCore(borkHC))
   except NameError:
      print("Not attempting hard core mode")
