#Sort a sequence in ascending order using the bubble sort algoritm.
def bubbleSort(theSeq):
    n,r=len(theSeq),0                       #n=9
    for i in range(n-1):                #to range(8)
        for j in range(n-i-1):          #9-0-1=8
            if theSeq[j]>theSeq[j+1]:
                tmp=theSeq[j]
                theSeq[j]=theSeq[j+1]
                theSeq[j+1]=tmp
            r=r+1
    return theSeq,r
#Sorts a sequence in ascending order using the selection sort algoritm
def selectionSort(theSeq):
    n,r=len(theSeq),0
    for i in range(n-1):
        #Asume the ith element is the smallest.
        smallNdx=i
        #determine if any other element contains a smaller value
        for j in range(i+1,n):
            if theSeq[j]<theSeq[smallNdx]:
                smallNdx=j
            r=r+1
        # Swap the ith value and smallNdx value only if the smallest value is 13 
        # not already in its proper position. Some implementations omit testing 14 
        # the condition and always swap the two values.
        if smallNdx!=i:
            tmp=theSeq[i]
            theSeq[i]=theSeq[smallNdx]
            theSeq[smallNdx]=tmp
    return theSeq,r 

# Sorts a sequence in ascending order using the insertion sort algorithm.
def insertionSort(theSeq):
    n,r=len(theSeq),0
    # Starts with the first item as the only sorted entry.
    for i in range(1,n):
        # Save the value to be positioned.
        value=theSeq[i]
        # Find the position where value fits in the ordered part of the list.
        pos=i
        while pos > 0 and value < theSeq[pos- 1] :
        # Shift the items to the right during the search. 
            theSeq[pos] = theSeq[pos- 1]
            pos-=1 
            r=r+1
        # Put the saved value into the open slot.
        theSeq[pos] = value
    return theSeq,r

         
 

lista=[1,31,30,29,27,34,25,24,23,3434]
print("non sorted %s"%(lista))
print("sorted:",(bubbleSort(lista)))
lista=[1,31,30,29,27,34,25,24,23,3434]
print("non sorted %s"%(lista))
print("sorted:",(selectionSort(lista)))
lista=[1,31,30,29,27,34,25,24,23,3434]
print("non sorted %s"%(lista))
print("sorted:",(insertionSort(lista)))
