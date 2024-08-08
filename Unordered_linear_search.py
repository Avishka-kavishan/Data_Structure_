def unordered(arr,val):
    for x in range (len(arr)):
        if arr[x] == val:
            return x # x = index of the value
    return ("value id not found")
        
arr = [5,22,89,45,1,3,8,5]
val = int(input("enter the value : ")) # user input
print(unordered(arr,val))
