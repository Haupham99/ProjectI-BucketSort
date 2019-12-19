
import json
from time import process_time

#Sort
def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1 
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      

def bucketSort(x, slot_num): 
    arr = [] 

    for i in range(slot_num): 
        arr.append([]) 
    # 1000 buckets 
    for j in x: 
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
def timeBucketSort(size,j):
    try:
        with open("sdt-Hai-Ba-Trung"+str(j)+".json", encoding='utf-8') as f:
		    data = json.load(f)
        arr = []
        for i,j in data.items():
            arr.append(int(j)/1000000000) # chuẩn hóa về 0..1
    finally:
        f.close()
    timeStart = process_time()
    bucketSort(arr, size)
    timeFinish = process_time()
    return (timeFinish - timeStart)
def thongKe():
    for i in range(100000,1000000,10000):
        sumTime = 0 
        for j in range(100):
            sumTime += timeBucketSort(i,j)
        F = open("ResultTestSpeed.txt", "a+")
        F.write(str(i) + " thung: " + str(sumTime))

