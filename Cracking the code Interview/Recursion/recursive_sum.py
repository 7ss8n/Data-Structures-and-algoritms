def ways(n):
    if n<=1:
        return 1
    else:
        return n + ways(n-1)

print(ways(3))

