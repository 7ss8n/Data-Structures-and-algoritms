def deleteDuplicates1(inputString):
    assert ((inputString!=None) and (len(inputString)>0)),"empty string" 
    new_string=""
    n=0
    for i in inputString:
        if i not in new_string:
            #new_string=new_string+i
            new_string="".join([new_string,i])
        n=n+1
    return new_string

def deleteDuplicates2(inputString):
    tempDict={}
    newString=""
    for i in inputString:
        if not(tempDict[i]):
            tempDict=1
            newString="".join([newString,i])
    return newString

test_cases=["abcd","aaa","aaabbccdddd",None,"",]
#for i in range(len(test_cases)):
#    print("%s is %s" %(test_cases[i],deleteDuplicates1(test_cases[i])))

for i in range(len(test_cases)):
    print("%s is %s" %(test_cases[i],deleteDuplicates2(test_cases[i])))
