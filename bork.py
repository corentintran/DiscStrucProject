import graphs
import digraphs


#The recursive function used to update the map exploring the different exits from the current location
def traverseBorkR(bork, map, oldSave):
   
   currentSave = bork.save()
   currentLoc = bork.description() #current location
   exits = bork.exits() #exits from the current location
   map[currentLoc] = {} #start editing the map with current location as a key

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
   
   map = {} #initialisation of the map
   initSave = bork.save() #first location saving
   traverseBorkR(bork, map, initSave) #call of the recursive function
   
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
