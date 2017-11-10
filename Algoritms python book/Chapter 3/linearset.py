# Implementation of the Set ADT container using a Python list.
class Set:
    #Creates an empty set instance.
    def __init__(self,*initElements):
        self.__theElements=list(initElements)
       
    #Returns the number of items in the set.
    def __len__(self):
        return len(self.__theElements)
    #Determines if an element is in the set.
    def __contains__(self,element):
        return element in self.__theElements
    #Removes an element from the set.
    def add(self,element):
        if element not in self:
            self.__theElements.append(element)
    #Determines if two sets are equal.
    def __eq__(self,setB):
        if len(self)!=len(setB):
            return False
        else:
            return self.isSubsetOf(setB)
    #Determines if this set is a subset of setB.
    def isSubsetOf(self,setB):
        for element in self:
            if element not in setB:
                return False
        return True
    #Creates a new set from the union of this set and setB.
    def union(self,setB):
        newSet=Set()
        newSet.__theElements.extend(self.__theElements)
        for element in setB:
            if element not in self:
                newSet.__theElements.append(element)
        return newSet
    def __add__(self,setB):
        return self.union(setB)
    #Creates a new set from the intersection: self set and setB.
    def intersect(self,setB):
        newSet=Set()
        for element in setB:
            if element in self:
                newSet.__theElements.append(element)
        return newSet

    #Creates a new set from difference:self set and setB.
    def difference(self,setB):
        newSet=Set()
        for element in setB:
            if element not in self:
                newSet.__theElements.append(element)
        for element in self:
            if element not in setB:
                newSet.__theElements.append(element)
        return newSet
    #Returns an interation for traversing the list of items.
    def __iter__(self):
        return _SetIterator(self.__theElements)
    def properSubset(self,setB):
        newSet=Set()
        newSet.__theElements.extend(setB.__theElements)
        for i in self.__theElements:
            if i not in newSet.__theElements:
                return False
        return True
    def __str__(self):
        sal=[]
        for i in self.__theElements:
            sal.append(i)
        return ("{%s}" % (sal))

#iterator class
class _SetIterator():
    def __init__(self,theArray):
        self._arrayref=theArray
        self._i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self._i<len(self._arrayref):
            entry=self._arrayref[self._i]
            self._i+=1
            return entry
        else:
            raise StopIteration()



smith = Set(20,20,30,40)
#for i in smith:
#    print(i) 
smith.add( "CSCI- 112" ) 
smith.add( "MATH- 121" ) 
smith.add( "HIST- 340" ) 
smith.add( "ECON- 101" ) 
#for i in smith:
#    print(i) 
roberts = Set() 
roberts.add( "POL- 101" ) 
roberts.add( "ANTH- 230" ) 
roberts.add( "CSCI- 112" ) 
roberts.add( "ECON- 101" )
l=roberts+smith
print(l)
#new=smith.difference(roberts)
#for i in new:
#    print(i) 

#set1=Set(1,2,3,4,5)
#set2=Set(1,2)
#print(Set(1,2,3).properSubset(Set(1,2,3,4,5)))



