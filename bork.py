import graphs
import digraphs

# You can define some helper functions here if you like!

def traverseBork(bork):
   # code your solution here

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
