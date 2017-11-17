def split(array):
    letters={'even':[],'odd':[]}
    for i in range(len(array)):
       if i%2!=0:
           letters['even'].append(array[i])
       else:
           letters['odd'].append(array[i])
    return "".join(letters['even'])+" ".join(letters['odd'])
n = int(input())
for a_i in range(n):
    print(split(input()))




