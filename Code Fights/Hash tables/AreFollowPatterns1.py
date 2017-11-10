def areFollowingPatterns(strings, patterns):
    flag = True
    d = {}
    e = {}
    for i in range(len(patterns)):#o(n)
        p = patterns[i]
        w = strings[i]
        if p in d:                 #o(n) 
            if d[p]!=w:
                flag = False
                break
        else:
            d[p] = w
        if w in e:              #o(n)
            if e[w]!=p:
                flag = False
                break
        else:
            e[w] = p 
strings= [["cat", "dog", "doggy","dogo"]]
patterns= ["a", "b", "b"]
print(areFollowingPatterns(strings,patterns))