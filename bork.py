import graphs
import digraphs

# You can define some helper functions here if you like!

def traverseBorkR(bork, map, oldSave):
   
   currentSave = bork.save()
   currentLoc = bork.description()
   exits = bork.exits()
   map[currentLoc] = {}

   for e in exits :
      #for each exit we move into it and update the map with the exit location
      bork.move(e)
      newloc = bork.description()
      map[currentLoc][e] = newloc
      if newloc in map:
         #if the location is already in the map we go back to the precedent location
         bork.restore(currentSave)
      else:
         #else we use the recurrent function to explore from this new location
         traverseBorkR(bork, map, currentSave)
   #we have explored all the path from this current location, we go back to the old one
   bork.restore(oldSave)


def traverseBork(bork):
   # code your solution here

   map = {}
   initSave = bork.save()
   traverseBorkR(bork, map, initSave)
   
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
