def is_unique1(StringInput):
#O(n^2)
    for i in range(len(StringInput)):           #O(n)
        if StringInput[i] in StringInput[i+1:]: #O(1)+O(n)+O(n)=O(n)
            return False                        #O(1)
    return True                                 #(1)
def is_unique2 (alist : [int]):
    copy = list(alist)			    #O(N)
    copy.sort()				        #O(N Log N) - for fast Python sorting
    for i in range(len(alist)-1):	#O(N) - really N-1, but that is O(N); len is O(1)
        if copy[i] == copy[i+1]:	#O(1): +, 2 [i],and  == ints: all O(1)
            return False		    #O(1) - never executed in worst case
    return True	  
def is_unique3 (alist):
    aset = set(alist)			    #O(N): construct set from alist values
    return len(aset) == len(alist)	#O(1): 2 len (each O(1)) and == ints O(1)
print(is_unique2("aababababab"))
print(is_unique1("abcdefg"))
print(is_unique1("abcdabcd"))
print(is_unique1("abc"))
