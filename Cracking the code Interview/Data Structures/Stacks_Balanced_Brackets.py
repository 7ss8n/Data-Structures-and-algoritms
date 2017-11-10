

def is_matched(expression):
    stack=[]
    symbols={'(':')','{':'}','[':']'}
    if len(expression)%2!=0:
        return False
    for x in expression:
        if symbols.get(x):
            stack.append(symbols[x])
        else:
            if len(stack)==0 or x!=stack[len(stack)-1]:
                return False
            stack.pop()
    return len(stack)==0

d=[1,2,3,4]
d.

l.r
t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")