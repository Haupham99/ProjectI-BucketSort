
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
    # slot_num buckets 
    for j in x: 
        j = int(j)
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
def timeBucketSort(size,s):
    count = 0
    with open("63tinh/"+str(s)+".json", encoding='utf-8') as f:
        data = json.load(f)
    arr = []
    for j in data:
        if(j< 1000000000):
            count+=1
            arr.append(int(j)/1000000000) # chuẩn hóa về 0..1
        # t = int(j)/1000000000
        # if(t >= 1):
        #     print(t)
    # print("count:" ,count)
    timeStart = process_time()
    bucketSort(arr, size)
    timeFinish = process_time()
    return (timeFinish - timeStart)

def thongKe():
    print("Starting...")
    F = open("ResultTestSpeed.txt", "w+")
    for i in range(5000,100000,5000):
        sumTime = 0 
        for j in range(1,100):
            sumTime += timeBucketSort(i,j)
        print(str(i) + " thung: " + str(sumTime) + "\n")
        F.write(str(i) + " thung: " + str(sumTime) + "\n")
    print("Finish.....")
    F.close()

def thongKeHaNoi():
    print("Starting...")
    F = open("Result-Ha-Noi.txt", "w+")

    for i in range(1000,11000,1000):
        sumTime = timeBucketSort(i,"ha-noi")
        print(str(i) + " thung: " + str(sumTime) + "\n")
        F.write(str(i) + " thung: " + str(sumTime) + "\n")
    for i in range(5000,105000,5000):
        sumTime = timeBucketSort(i,"ha-noi")
        print(str(i) + " thung: " + str(sumTime) + "\n")
        F.write(str(i) + " thung: " + str(sumTime) + "\n")
    print("Finish.....")
    F.close()
if __name__ == "__main__":
    # thongKe()
    thongKeHaNoi()


