def bubble_sort(arr):
    for x in range(len(arr)):
        for y in range (0,len(arr)-x-1):
            if arr[y] > arr[y+1]:
                arr[y],arr[y+1] = arr[y+1], arr[y]
    return arr

arr = [4,67,1,89,56,4,23,5,99,100,56]
sorted_arr = bubble_sort(arr)
print(sorted_arr)

def oredred_search(sorted_arr,val):
    for i in range (len(sorted_arr)):
        if sorted_arr[i] == val:
            return i
        elif sorted_arr[i] > val:
            return None
    return None

val = int(input("Enter the value : "))
print(oredred_search(sorted_arr,val))
