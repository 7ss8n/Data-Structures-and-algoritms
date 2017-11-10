def ransom_note(magazine, ransom):
    mag,rans={},{}
    m, n = map(int, input().strip().split(' '))
    magazine = magazine.split(' ')
    ransom = ransom.split(' ')
    
    for i in range(int(m)):
        if magazine[i] in mag.keys():
            mag[magazine[i]].append(i)

        else:
            mag[magazine[i]]=[i]
    
    for i in range(int(n)):
        if ransom[i] in rans.keys():
            rans[ransom[i]].append(i)

        else:
            rans[ransom[i]]=[i]
    for r in rans.keys():
        if(len(rans[r]))>len(mag[r]):
            return False
    return True
   
maga="two times two three is not four"
rans="two times two is four"
print(ransom_note(maga,rans))
    