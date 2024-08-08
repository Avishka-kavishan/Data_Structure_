def recurtion (n):
    if n == 0 :
        return 1
    return n*recurtion(n-1)

print(recurtion(5))