import heapq
class solution:
    def __init__(self, array):
         self.array=array
         self.lowers=[]
         self.highers=[]
    def addNumber(self,number):
        if len(self.lowers)==0 or number<abs(self.lowers[0]):
            heapq.heappush(self.lowers,-number)
        else:
            heapq.heappush(self.highers,number)
    def reBalance(self):
        if len(self.lowers)>len(self.highers):
     
            if len(self.lowers)-len(self.highers)>=2:
                heapq.heappush(self.highers,abs(heapq.heappop(self.lowers)))
        else:
            
            if len(self.highers)-len(self.lowers)>=2:
                heapq.heappush(self.lowers,-1*heapq.heappop(self.highers))
    def getMedian(self):
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

    def getMedians(self):
        medians=[]
        for i in range(len(self.array)):
            number=self.array[i]
            self.addNumber(number)
            self.reBalance()
            medians.append(self.getMedian())
        return medians
list1=[6,5,4,3,2,1,67,90]
demo=solution(list1)
print(demo.getMedians())
#heapq.heapify(list1)
#heapq._heapify_max(list3)
#print(list1)
#print(list3)
