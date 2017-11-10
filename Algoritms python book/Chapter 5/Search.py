import random
def linearSearch(theValues, target):
    n=len(theValues)
    i=0
    for i in range(n):
        #If the target is in the ith element, return True
        if theValues[i]==target:
            return True,i
        i=i+1
    return False,i


def sortedLinearSearch(theValues,item):
    n=len(theValues)
    j=0
    for i in range(n):
        #if the target is found in the ith element,return True
        if theValues[i]==item:
            return True,j
        #if the target is arger than the ith, its not in the list
        elif theValues[i]>item:
            return False,j
        j=j+1
    return False,j


def binarySearch(theValues,target):
    #Start with the entire sequence of elements for a ordered list
    low=0
    high=len(theValues)-1
    i=0
    #reapeatedly subdivide the sequence in half until the target is found.
    while low<=high:
        #find the midpoint of the sequence.
        mid=(high+low)//2
        #does the midpoint contains target
        if theValues[mid]==target:
            return True,i
        #or does the target precede the midpoint?
        elif target<theValues[mid]:
            high=mid-1
        #or does it follow the midpoint?
        else:
            low=mid+1
        i=i+1
    #if the sequence cannot be subdivided further, we're done.
    return False,i
items=list(range(0,10000))
#random.shuffle(items)
items2=list(range(0,1000))        
#random.shuffle(items2)
items3=list(range(0,100))
#random.shuffle(items3)    
unit_test=[items,items2,items3]
for i in unit_test:
    print("linearsearch for ",len(i)//2,linearSearch(i,len(i)//2))
    print("sortedLinearSearch for",len(i)//2,sortedLinearSearch(i,len(i)//2))
    print("binarySearch for ",len(i)//2 ,(binarySearch(i,len(i)//2)))
