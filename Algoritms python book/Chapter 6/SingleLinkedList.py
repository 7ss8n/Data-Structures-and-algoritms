#Construct a node
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

#Create an empty linked list or with elements if a list is provided
class LinkedList:
    def __init__(self,listElements=None):
        self.__head=None
        self.__tail=None
        self.size=0
        if(listElements!=None):
            for i in listElements:
                self.addTobeg(i) 
    #Add a new element to the beggining of the linked list
    def addTobeg(self,data):
        new_node=ListNode(data)
        if self.__head==None:
            self.__tail=new_node
        new_node.next=self.__head
        self.__head=new_node
        self.size+=1
    #Add a new element to the end of the linked list    
    def addToTail(self,data):
        new_node=ListNode(data)
        if self.__head== None:
            self.addTobeg(data)
        else:
            self.__tail.next=new_node
        self.__tail=new_node
        self.size+=1
    def testing(self):
        print(self.__head.next.next.next)
        
    def remove(self,data):
        predNode=None
        curNode=self.__head
        while curNode is not None and curNode.data!=data:
            predNode=curNode
            curNode=curNode.next
        assert curNode is not None,"data is not in the linked list"

        self.size-=1
        if curNode is self.__head:
            self.__head=curNode.next
        else:
            predNode.next=curNode.next
        return curNode.data

    def search(self,data):
        curNode=self.__head
        while curNode is not None and curNode.data != data:
            curNode=curNode.next
        return curNode is not None
  
        
    """Run in all elements of the linked list"""
    def traversal(self):
        curNode=self.__head
        while curNode is not None:
            print (curNode.data)
            curNode=curNode.next
#myListElements=[3,1,2,3,4,5]
#myList=LinkedList(myListElements)
#myList.addTobeg(1)
#myList.addTobeg(2)
#myList.traversal()
#myList.addToTail(8)
#myList.addTobeg(1)
#myList.addTobeg(4)
#myList.addToTail(1)
#myList.remove(5)
#myList.traversal()
#print("Size of %d element"%(myList.size))
#print("is the element 8 in the linked list: ",(myList.search(8)))
myListElements=[3,1,2,3,4,5]
myList2=LinkedList(myListElements)
print(myList2.testing())



        

