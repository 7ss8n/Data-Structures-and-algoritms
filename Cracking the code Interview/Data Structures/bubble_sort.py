def bubble_sort(n,a):
    i,j,movs=0,0,0
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
                movs=movs+1
    return a[0],a[-1],movs