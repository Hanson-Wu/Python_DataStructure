__author__ = 'Nan'

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(1,n-i):
            if  arr[j-1] > arr[j] :
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr

############################################################################

def select_sort(arr):
    n = len(arr)
    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if arr[j] < arr[min] :
                min = j
        arr[min],arr[i] = arr[i],arr[min]
    return arr

############################################################################

def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            index = i
            for j in range(i-1,-1,-1):
                if arr[j] > temp :
                    arr[j+1] = arr[j]
                    index = j
                else :
                    break
            arr[index] = temp
    return arr

############################################################################

def shell_sort(arr):
    n = len(arr)
    gap = round(n/2)
    while gap > 0 :
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while ( j >= gap and arr[j-gap] > temp ):
                arr[j] = arr[j-gap]
                j = j - gap
            arr[j] = temp
        gap = round(gap/2)
    return arr

############################################################################

def merge_sort(arr):
    if len(arr) <= 1 : return arr
    num = int(len(arr)/2)
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    return merge(left,right)


def merge(left,right):

    l,r = 0,0
    result = []
    while l<len(left) and r<len(right) :
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

############################################################################

def quick_sort(arr):
    return qsort(arr,0,len(arr)-1)

def qsort(arr,left,right):

    if left >= right : return arr
    key = arr[left]
    lp = left
    rp = right
    while lp < rp :
        while arr[rp] >= key and lp < rp :
            rp -= 1
        while arr[lp] <= key and lp < rp :
            lp += 1
        arr[lp],arr[rp] = arr[rp],arr[lp]
    arr[left],arr[lp] = arr[lp],arr[left]
    qsort(arr,left,lp-1)
    qsort(arr,rp+1,right)
    return arr

############################################################################

def heap_sort(arr) :
    n = len(arr)
    first = int(n/2-1)
    for start in range(first,-1,-1) :
        max_heapify(arr,start,n-1)
    for end in range(n-1,0,-1):
        arr[end],arr[0] = arr[0],arr[end]
        max_heapify(arr,0,end-1)
    return arr



def max_heapify(arr,start,end):
    root = start
    while True :
        child = root*2 +1
        if child > end : break
        if child+1 <= end and arr[child] < arr[child+1] :
            child = child+1
        if arr[root] < arr[child] :
            arr[root],arr[child] = arr[child],arr[root]
            root = child
        else :
            break