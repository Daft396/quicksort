import random
import time
starttime = time.time()
arr = []
def generate_array(arr):
    elmnts = int(input("Enter the amount of numbers: "))
    lowerbound = int(input("Enter the lower bound of your numbers: "))
    upperbound = int(input(f"Enter the range of your numbers, from {lowerbound} to: "))
    for i in range(elmnts):
        arr.append(random.randint(lowerbound,upperbound))
    return arr
def qsort(arr):
    if len(arr) <= 1:
        return arr

    left = 1
    right = len(arr)-1
    pivot = arr[0]

    while left<right:
        while left< right and arr[left] < pivot:
            left+=1

        while right >=left and arr[right] >= pivot:
            right -= 1

        if left <= right:
            temp = arr[left]
            arr[left] =arr[right]
            arr[right] = temp
            
    if pivot > arr[right]:
        temp = pivot
        arr[0] = arr[right]
        arr[right] = temp
    left_list = qsort(arr[0:(right)])
    right_list = qsort(arr[right+1:(len(arr))])
    return left_list + [arr[right]] + right_list
generate_array(arr)
print(qsort(arr))
endtime = time.time()
timetaken = endtime - starttime
print(f"This sorting algorithm took {timetaken} seconds")
