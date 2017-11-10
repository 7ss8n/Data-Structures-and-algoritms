def contains_close_nums(nums,k):
    dicto={}
    for i in range(len(nums)):
        if nums[i] in dicto.keys():
            dicto[nums[i]].append(i)
      

        else:
            dicto[nums[i]]=list([i])
    for i in dicto.keys():
        if len(dicto[i])>1:
            if (dicto[i][-1]-dicto[i][-2])<=k:
                return True
            
    return False
lista=[0, 1, 2, 3, 4, 0, 0, 7, 8, 9, 10, 11, 12,0]
print(contains_close_nums(lista,3))
