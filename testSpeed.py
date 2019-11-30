from random import randrange
from time import process_time
# Heap sort
# To heapify subtree rooted at index i.
#  n is size of heap


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)


#----------------------------------------------------____#
# Quick sort
def partition(arr, low, high):
    i = (low-1)		 # index of smaller element
    pivot = arr[high]	 # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
def quickSort(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

#----------------------------------------------------____#
# Merge sort


# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
    l = int(l)
    m = int(m)
    r = int(r)
    n1 = m - l + 1
    n2 = r - m
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0	 # Initial index of first subarray
    j = 0	 # Initial index of second subarray
    k = l	 # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

# l is for left index and r is right index of the
# sub-array of arr to be sorted


def mergeSort(arr, l, r):
    if l < r:

        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l+(r-1))/2
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

# Couting Sort
def countingSort(arr, n, exp):
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        t = (int(arr[i])/int(exp))%10
        count[int(t)] += 1

    # hange count[i] so that count[i] now contains actual
    #  position of this digit in output[]
    for i in range(10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n-1,0):
        output[count[ (arr[i]/exp)%10 ] - 1] = arr[i]
        count[ (arr[i]/exp)%10 ] -= 1

    # Copy the output array to arr[], so that arr[] now
    #  contains sorted numbers according to current digit
    for i in range(n):
        arr[i] = output[i]


# Bucket sort
def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x): 
    arr = [] 
    slot_num = 10 

    for i in range(slot_num): 
        arr.append([]) 
          
    # 10 buckets 
    for j in range(x): 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort buckets  
    for i in range(slot_num): 
        arr[i] = insertionSort(arr[i]) 
          
    # concatenate bucket 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x 

def timeBucketSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(f.readline())
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    bucketSort(arr)
    timeFinish = process_time()
    return (timeFinish - timeStart)

def timeQuickSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(f.readline())
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    quickSort(arr, 0, n-1)
    timeFinish = process_time()
    return (timeFinish - timeStart)


def timeMergeSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(f.readline())
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    mergeSort(arr, 0, n-1)
    timeFinish = process_time()
    return (timeFinish - timeStart)


def timeHeapSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(f.readline())
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    heapSort(arr)
    timeFinish = process_time()
    return (timeFinish - timeStart)


def timeCoutingSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(f.readline())
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    countingSort(arr, n, 10)
    timeFinish = process_time()
    return (timeFinish - timeStart)


def sinhSo(n):
    print("Dang tao so...")
    f = open("testSpeed.txt", "w+")
    # print("f.write is: " + f.mode)
    t = randrange(n)
    # print(str(t))
    f.write(str(t))
    for i in range(n):
        t = randrange(1000000000)
        # print(str(t))
        f.write("\n"+str(t))
    f.close()
    print("Da tao xong!!!")


def menu(n):
    input()
    print("\n")
    print("***********************")
    print("1. Sinh so")
    print("2. timeSort: ")
    print("Bam Q de thoat!")
    print("\n")
    s = input()
    if(s=="1"):
        sinhSo(n)
    if(s=="2"):
        print("\n")
        print("timeHeapSort = ", timeHeapSort(n))
        print("timeMergeSort = ", timeMergeSort(n))
        print("timeQuickSort = ", timeQuickSort(n))
        print("timeCoutingSort = ", timeCoutingSort(n))
        print("timeBucketSort = ", bucketSort(n))
    if(s.upper() == "Q"):
        exit()
    else:
        menu(n)


if __name__ == '__main__':
    n = 100000
    print("\nBấm [enter] để bắt đầu")
    menu(n)