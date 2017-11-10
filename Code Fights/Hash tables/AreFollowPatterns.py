def areFollowingPatterns(strings, patterns):
    #returns true if the the strings and pattern list follow the same pattern or false if are not the same
    if(len(strings)!=len(patterns)):# if the len of one list is bigger is not following the constraint
        return False
    dict1,dict2={},{}
    ind1,ind2=0,0
    for i in range(len(strings)):
        if i==0:
            dict1[strings[i]]=ind1
            dict2[patterns[i]]=ind2
        else:
            if(strings[i-1]!=strings[i]):
                ind1+=1
                dict1[strings[i]]=ind1
            if(patterns[i-1]!=patterns[i]):
                ind2+=1
                dict2[patterns[i]]=ind2
        print(dict1,dict2)
        if len(dict1)!=len(dict2):
            return False
    return True

strings= [["cat", "dog", "doggy"]]
patterns= ["a", "b", "b"]
print(areFollowingPatterns(strings,patterns))