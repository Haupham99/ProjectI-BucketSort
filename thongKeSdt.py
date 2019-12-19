             
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