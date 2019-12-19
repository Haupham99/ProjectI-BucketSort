from random import randrange
from time import process_time
# Heap sort
# To heapify subtree rooted at index i.
#  n is size of heap

# -----------Heap Sort -----------
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
    # return arr 

def timeHeapSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(int(f.readline()))
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    heapSort(arr)
    timeFinish = process_time()
    return (timeFinish - timeStart)


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
    # return arr 

def timeQuickSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(int(f.readline()))
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    quickSort(arr, 0, n-1)
    timeFinish = process_time()
    return (timeFinish - timeStart)



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
    # return arr 

def timeMergeSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(int(f.readline()))
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    mergeSort(arr, 0, n-1)
    timeFinish = process_time()
    return (timeFinish - timeStart)



# -------------Couting Sort--------------
# Python program for counting sort 

# The main function that sort the given string arr[] in 
# alphabetical order 
def countSort(array1):
             
    arrMax = array1[0]
    for a in array1:
        arrMax = a if a>arrMax else arrMax
    m = arrMax + 1   
    count = [0] * m 
    for a in array1:
    # count occurences
        count[a] += 1                
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            array1[i] = a
            i += 1
    # return array1


def timeCoutingSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(int(f.readline()))
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    countSort(arr)
    timeFinish = process_time()
    return (timeFinish - timeStart)



#   --------------------Bucket Sort----------
def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(arr, num): 
    arr2 = [] 
    slot_num = num

    for i in range(slot_num): 
        arr2.append([]) 
          
    # 1000 buckets 
    for j in arr: 
        index_b = int(slot_num * j)  
        arr2[index_b].append(j) 
      
    # Sort buckets  
    for i in range(slot_num): 
        arr2[i] = insertionSort(arr2[i]) 
          
    # concatenate bucket 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr2[i])): 
            arr[k] = arr2[i][j] 
            k += 1
    # return arr

def timeBucketSort(n, num):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(float((f.readline()))/MAX) # chuẩn hóa về 0..1
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    arr = bucketSort(arr, num)
    timeFinish = process_time()
    # F = open("ResultTestSpeed.txt", "w+")
    # print("f.write is: " + f.mode)
    # t = randrange(n)
    # print(str(t))
    # F.write(str(t))
    # for i in range(n):
    #     # t = randrange(MAX)
    #     # print(str(t))
    #     F.write("\n"+str(t))
    return (timeFinish - timeStart)

def radixSort(arr, n):
    max1 = max(arr) 
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp1 = 1
    while max1/exp1 > 0: 
        # The output array elements that will have sorted arr 
        output = [0] * (n) 
        # initialize count array as 0 
        count = [0] * (10) 
        # Store count of occurrences in count[] 
        for i in range(0, n): 
            index = (arr[i]/exp1) 
            count[ int((index)%10) ] += 1
        # Change count[i] so that count[i] now contains actual 
        #  position of this digit in output array 
        for i in range(1,10): 
            count[i] += count[i-1] 
        i = n-1
        while i>=0: 
            index = (arr[i]/exp1) 
            output[ count[ int((index)%10) ] - 1] = arr[i] 
            count[ int(index)%10 ] -= 1
            i -= 1
        i = 0
        for i in range(0,len(arr)): 
            arr[i] = output[i] 
        exp1 *= 10

def timeRadixSort(n):
    try:
        f = open("testSpeed.txt", "r")
        arr = []
        for i in range(n):
            arr.append(float((f.readline())))
            # print(arr[i])
    finally:
        f.close()
    timeStart = process_time()
    radixSort(arr,n)
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
        t = randrange(MAX)
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
    print("--->> your chose is: ")
    s = input()
    if(s=="1"):
        sinhSo(n)
    if(s=="2"):
        print("\n")
        # print("timeHeapSort = ", timeHeapSort(n))
        # print("timeMergeSort = ", timeMergeSort(n))
        # print("timeQuickSort = ", timeQuickSort(n))
        # print("timeCoutingSort = ", timeCoutingSort(n))
        # print("timeRadixSort = ", timeRadixSort(n))
        # print("timeBucketSort = ", timeBucketSort(n, 1000000))
        
        i=1000
        f= open("timeSort.txt", "w+")
        while(i <= 100000):
           t = timeBucketSort(n, i)
           print("timeBucketSort[",i,"] = ", t) 
           i += 1000
           f.write(str(t)+ '\n')

        print("OK!!!")
    if(s.upper() == "Q"):
        exit()
    else:
        menu(n)

MAX = 1000000
if __name__ == '__main__':
    n = 100000
    print("\nBấm [enter] để bắt đầu")
    menu(n)