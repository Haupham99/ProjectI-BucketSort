import json

with open("data.json", encoding='utf-8') as f:
	data = json.load(f)

#Chuẩn hóa về 0-1
phone1 = []

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
              
def bucketSort(x): 
    arr = [] 
    slot_num = 10 

    for i in range(slot_num): 
        arr.append([]) 
          
    # 10 buckets 
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

#Menu

def showContacts():
	with open("data.json", encoding='utf-8') as f:
		data = json.load(f)
	print("Danh bạ : ")
	for x in data :
		print(x + ":" + data[x])

def addContacts():
	print("Nhập tên : ")
	name = input()
	print("Nhập số điện thoại : ")
	phoneNumber = input()
	data[name] = phoneNumber

	with open("data.json", 'w', encoding='utf-8') as f:
		json.dump(data, f)
	sortContacts()
	showContacts()

def editContacts():
	print("Nhập tên hoặc số điện thoại muốn sửa : ")
	nameOrPhone = input()
	
	# if it is number
	if nameOrPhone[0].isdigit():
		found = 0
		for name, phone in data.items():
			if nameOrPhone == phone:
				print("Tìm thấy!")
				print(name + " : " + phone)
				found = 1
		if found == 0:
			print("Không tìm thấy người này!")
	# if it is name
	else:
		found = 0
		for name, phone in data.items():
			if nameOrPhone == name:
				print("Tìm thấy!")
				print(name + " : " + phone)
				found = 1
		if found == 0:
			print("Không tìm thấy người này!")
	# Edit
	if found == 1:
		print("Nhập tên mới : ")
		newName = input()
		print("Nhập số điện thoại mới : ")
		newPhoneNumber = input()
		data.pop(name)
		data[newName] = newPhoneNumber
		with open("data.json", 'w', encoding='utf-8') as f:
			json.dump(data, f)
	sortContacts()
	showContacts()

def deleteContacts():
	print("Nhập tên hoặc số điện thoại muốn xóa : ")
	nameOrPhone = input()
	
	# if it is number
	if nameOrPhone[0].isdigit():
		found = 0
		for name, phone in data.items():
			if nameOrPhone == phone:
				print("Tìm thấy!")
				print(name + " : " + phone)
				found = 1
				nameFound = name
		if found == 0:
			print("Không tìm thấy người này!")
	#if it is name
	else:
		found = 0
		for name, phone in data.items():
			if nameOrPhone == name:
				print("Tìm thấy!")
				print(name + " : " + phone)
				found += 1
		if found == 0:
			print("Không tìm thấy người này!")

	# Delete
	if found == 1:
		if nameOrPhone[0].isdigit():
			data.pop(nameFound)
		else:
			data.pop(nameOrPhone)
		with open("data.json", 'w', encoding='utf-8') as f:
			json.dump(data, f)
	showContacts()

def sortContacts():
	with open("data.json", encoding='utf-8') as f:
		data = json.load(f)
	for i,j in data.items():
		phone1.append(int(j)/1000000000)

	bucketSort(phone1)

	dataSorted = {}

	for x in phone1:
		for name, phonex in data.items():
			if int(phonex) == x*1000000000:
				dataSorted[name] = phonex
	with open("data.json", 'w', encoding='utf-8') as f:
		json.dump(dataSorted, f)
	print("Đã sắp xếp theo số điện thoại !")
	showContacts()

def searchContactByPhone():
	print("Nhập số điện thoại muốn tìm kiếm : ")
	phoneSearch = input()
	found = 0
	for name, phone in data.items():
		if phoneSearch == phone:
			print("Tìm thấy!")
			print(name + " : " + phone)
			found = 1
	if found == 0:
		print("Không tìm thấy người này!")

def searchContactByName():
	print("Nhập tên cần tìm kiếm : ")
	nameSearch = input()
	found = 0
	for name, phone in data.items():
		if nameSearch == name:
			print("Tìm thấy!")
			print(name + " : " + phone)
			found = 1
	if found == 0:
		print("Không tìm thấy người này!")

def menu():
	print("1. Hiển thị số điện thoại")
	print("2. Thêm số điện thoại")
	print("3. Sửa số điện thoại")
	print("4. Xóa số điện thoại")
	print("5. Sắp xếp số điện thoại")
	print("6. Tìm theo số điện thoại")
	print("7. Tìm kiếm theo tên")
	print("8. Thoát")
	s = input()

	if(s == '1'):
		showContacts()
		menu()
	elif(s == '2'):
		addContacts()
		menu()
	elif(s == '3'):
		editContacts()
		menu()
	elif(s == '4'):
		deleteContacts()
		menu()
	elif(s == '5'):
		sortContacts()
		menu()
	elif(s == '6'):
		searchContactByPhone()
		menu()
	elif(s == '7'):
		searchContactByName()
		menu()
	else:
		exit()


if __name__ == '__main__':
	menu()
