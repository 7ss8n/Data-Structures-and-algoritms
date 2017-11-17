
def my_func(a,b):
    c=[]
    while len(a)>0 or len(b)>0:
        if(len(a))>0:
            c.append(a.pop(0))

        if(len(b)>0):
            c.append(b.pop(0))

    return c

a=[1,2,3]
b=['a','b','c','d','e']
print(my_func(a,b))

