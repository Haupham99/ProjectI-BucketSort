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


#checkPhoneNumber:
def phoneError(phone):
	if(len(phone) != 10): 
		print("Nhập đủ 10 số nhé! Nhập lại nào: ")
		return True
	return False
#Menu

def showContacts():
	print("Danh bạ của bạn:")
	with open("data.json", encoding='utf-8') as f:
		data = json.load(f)
	print("Dạnh bạ : ")
	for x in data :
		print(x + ":" + data[x])
	i=input()
	

def addContacts():
	print("Chức năng: Thêm liên lac: \n")
	print("Nhập tên : ")	
	name = input()
	if name in data:
		print("Đã tồn tại tên.")
	else:
		print("Nhập số điện thoại : ")
		phoneNumber = input()
		while(phoneError(phoneNumber)):
			phoneNumber = input()
		data[name] = phoneNumber
		with open("data.json", 'w', encoding='utf-8') as f:
			json.dump(data, f)
		print("Thêm "+name+" : "+phoneNumber+" OK!")
	i=input()


def editContacts():
	print("Chức năng: Sửa liên lạc\n")
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
		while(phoneError(newPhoneNumber)):
			newPhoneNumber = input()
		data.pop(name)
		data[newName] = newPhoneNumber
		with open("data.json", 'w', encoding='utf-8') as f:
			json.dump(data, f)
		
		print("Sửa "+newName+" : "+newPhoneNumber+" OK!")
	else:
		print("Không tìm thấy người này !")
	i=input()

def deleteContacts():
	print("Chức năng: Xóa liên lạc:\n")
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
		phoneNumber = data[name]
		data.pop(name)
		with open("data.json", 'w', encoding='utf-8') as f:
			json.dump(data, f)
		
		print("Xoa "+name+" : "+phoneNumber+" OK!")
	else:
		print("Không tìm thấy người này !")
	i=input()

def sortContacts():
	with open("data.json", encoding='utf-8') as f:
		data = json.load(f)
	print("Chức năng: Sắp xếp:")
	for i,j in data.items():
		phone1.append(int(j)/1000000000)
	# for i in phone:
		# print(i)
	bucketSort(phone1)

	dataSorted = {}

	for x in phone1:
		for name, phonex in data.items():
			if int(phonex) == x*1000000000:
				dataSorted[name] = phonex
	with open("data.json",'w', encoding='utf-8') as f:
		json.dump(dataSorted, f)
	print("Đã sắp xếp theo số điện thoại !")
	showContacts()
	i=input()

def searchContact():
	print("Nhập tên hoặc số điện thoại muốn tìm kiếm : ")
	phoneSearch = input()
	found = 0
	for name, phone in data.items():
		if phoneSearch == phone:
			print("Tìm thấy!")
			print(name + " : " + phone)
			found = 1
	if found == 0:
		print("Không tìm thấy người này!")
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
	print("\n************************\n\tMenu\n")
	print("1. Hiển thị các liên lạc hiện tại")
	print("2. Thêm liên lạc")
	print("3. Sửa số liên lạc")
	print("4. Xóa số liên lạc")
	print("5. Sắp xếp theo số điện thoại")
	print("6. Tìm danh bạ")
	print("7. Thoát")
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
		searchContact()
	elif(s == '7'):
		exit()
	else:
		menu()

if __name__ == '__main__':
	menu()
