arr = [2,3,5,7,6,4,778,54]
def qsort(arr):
    if len(arr) <= 1:
        return arr

    left = 1
    right = len(arr)-1
    pivot = arr[0]

    while left<right:
        while left< right and arr[left] < pivot:
            left+=1

        while right >=left and arr[right] > pivot:
            right -= 1

        if left < right:
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
print(qsort(arr))
