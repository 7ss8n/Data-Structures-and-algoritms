# Implementation of the Stack ADT using a Python list.
class Stack:
    #Creates an empty.
    def __init__(self):
        self.__theItems=list()
    #Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        return len(self)==0

    #Returns the number of items in the stack.
    def __len__(self):
        return len(self.__theItems)

    #Returns the top item on the stack withouy removin it.
    def peek(self):
        assert not self.isEmpty(),"Cannot peek an empty stack"
        return self.__theItems[-1]

    #Remoevs and returns the top item on the stack.
    def pop(self):
        assert not self.isEmpty(),"Cannot pop from empty stack"
        return self.__theItems.pop()

    #Push and item onto the top of the stack.
    def push(self,item):
        self.__theItems.append(item)

new_stack=Stack()
new_stack.push(2)
new_stack.push(3)
new_stack.push(4)
new_stack.push(5)
new_stack.push(6)
print(len(new_stack))
print(new_stack.peek())