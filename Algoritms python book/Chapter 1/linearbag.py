#Implements the bag ADT container using a Python List.
class Bag:
    #Constructs an empty bag.
    def __init__(self):
        self.theItems=list()
    #Returns the number of items in the bag.
    def __len__(self):
        return len(self.__theItems)
    #Determines if an item is contained in the bag.
    def __contains__(self,items):
        return item in self.__theItems
    #Adds a new item to the bag.
    def add(self,item):
        self.__theItems.append(item)
    #Removes and return an instance of the item from the bag.
    def remove(self,item):
        assert item in self.theItems,"The item must be in the bag."
        ndx=self.__theItems.index(item)
        return self.theItems.pop(ndx)
    #Returns an iterator for traversing the list of items.
    def __iter__(self,item):
        return _BagIterator(self.__theItems)
        
#An iterator for the Bag ADT implemented as a python list.
class _BagIterator:
    def __init__(self, theList):
        self._bagItems=theList
        self._curItem=0
    def __iter__(self):
        return self
        
    def __next__(self):
        if self._curItem<len(self._bagItems):
            item=self._bagItems[self._curItem]
            self._curItem+=1
            return item
        else:
            raise StopIteration