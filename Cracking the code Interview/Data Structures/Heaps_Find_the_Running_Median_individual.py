#The median of a dataset of integers is the midpoint value of the dataset for 
#which an equal number of integers are less than and greater than the value. 
import heapq
class solution:
    # class with all methods and arrays needed to solve the problem
    def __init__(self, array):# start the two heaps needed to solve the problem
         self.lowers=[]#lowers is a max heap to improve the access to the max value
         self.highers=[]#highers is a min heap to imtprove the speed of min value
    def addNumber(self,number):
    # add a element to the heap(highers or lowers)
        if len(self.lowers)==0 or number<abs(self.lowers[0]):
            heapq.heappush(self.lowers,-number)
        else:
            heapq.heappush(self.highers,number)
    def reBalance(self):
    # this method balance the number of elements in the heaps
        if len(self.lowers)>len(self.highers):
     
            if len(self.lowers)-len(self.highers)>=2:
                heapq.heappush(self.highers,abs(heapq.heappop(self.lowers)))
        else:
            
            if len(self.highers)-len(self.lowers)>=2:
                heapq.heappush(self.lowers,-1*heapq.heappop(self.highers))
    def getMedian(self):
    # this method return the median of the two heaps
        if len(self.lowers)>len(self.highers):
            if(len(self.lowers))==len(self.highers):
                return (abs(self.lowers[0])+self.highers[0])/2
            else:
                return abs(self.lowers[0])
        else:
            if(len(self.highers))==len(self.lowers):
                return (self.highers[0]+abs(self.lowers[0]))/2
            else:
                return self.highers[0]

    def UpdateHeap(self,num):
        #This method update take one element and send this to the internal methods
        self.addNumber(num)
        self.reBalance()
        self.getMedian()
        return self.getMedian()
list1=[6,5,4,3,2,1,67,90]
demo=solution(list1)
for i in range(len(list1)):
    print(demo.UpdateHeap(i))
print(demo.getMedians())
#heapq.heapify(list1)
#heapq._heapify_max(list3)
#print(list1)
#print(list3)

