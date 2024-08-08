def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
        left = []
        right = []
        for item in arr:
            if item < pivot:
                left.append(item)
            else:
                right.append(item)
        return quick_sort(left)+[pivot]+quick_sort(right)
    
arr = [4,67,1,89,56,4,23,5,99,100,56]
sorted_arr = quick_sort(arr)
print(sorted_arr)

def Binary_search(sorted_arr,val):
    m = len(sorted_arr)
    middle = m // 2
    left1 = sorted_arr[:middle]
    right1 = sorted_arr[middle+1:]
    x = 0
    y = 0
    if sorted_arr[middle] <= val:
        for x in range (len(left1)):
            if left1[x] == val:
                return x
            else:
                return None
    else:
        for y in range (len(right1)):
            if right1[y] == val:
                return y
            else:
                return None

val = int(input("enter the value : "))
print(Binary_search(sorted_arr,val))

