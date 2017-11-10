def binary_search(a,item):
    first=0
    last=len(a)-1
    found=False

    while found==False and first<=last:
        mid=(first+last)//2
        if a[mid]==item:
            return True
        else:
            if item<a[mid]:
                last=mid-1
            else:
                first=mid+1
    return found


a=[1,2,3,4,5,89,100,167]
print(binary_search(a,89))
