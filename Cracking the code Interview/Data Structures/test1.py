
def my_func(a,b):
    c=[]
    while len(a)>0 or len(b)>0:
        if(len(a))>0:
            c.append(a.pop(0))

        if(len(b)>0):
            c.append(b.pop(0))

    return c

#a=[]
#b=['a','b','c','d','e']
#print(my_func(a,b))


def almost_palindromes(stre):
    c=0
    d=list(stre)
    for i in range(len(d)):
        if  d[-1*i]!=d[i]:
            c=c+1
    
    return c
erprint(almost_palindromes("abba"))