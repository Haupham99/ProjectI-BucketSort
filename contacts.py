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
    slot_num = 1000

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

def bucketSortByName(x):
	arr = []
	slot_num = 100
	for i in range(slot_num):
		arr.append([])

	#10 buckets
	for j in x:
		nameLower = str.lower(j)
		index_b = int(slot_num * (ord(nameLower[0])-97)/(123-97))
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
	print("----------Danh bạ---------")
	print("    {:<15} {}\n".format("Tên","Số điện thoại"))
	for x in data :
		print("| {:<15} |   {}   |".format(x,data[x]))
		print("------------------------------------")
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
	name = isContacts(nameOrPhone)

	# Edit
	if name != "###":
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
	i=input()

def deleteContacts():
	print("Chức năng: Xóa liên lạc:\n")
	print("Nhập tên hoặc số điện thoại muốn xóa : ")
	nameOrPhone = input()
	name = isContacts(nameOrPhone)
	# Delete
	if name!="###":
		phoneNumber = data[name]
		data.pop(name)
		with open("data.json", 'w', encoding='utf-8') as f:
			json.dump(data, f)
		print("Xoa "+name+" : "+phoneNumber+" OK!")
	i=input()

def sortContactsByNumPhone():
	with open("data.json", encoding='utf-8') as f:
		data = json.load(f)
	listPhone = []
	print("Chức năng: Sắp xếp theo số điện thoại:")
	for i,j in data.items():
		listPhone.append(int(j)/1000000000)
	# for i in phone:
		# print(i)
	bucketSort(listPhone)
	dataSorted = {}
	for x in listPhone:
		for name, phone in data.items():
			if int(phone) == x*1000000000:
				dataSorted[name] = phone
	with open("data.json",'w', encoding='utf-8') as f:
		json.dump(dataSorted, f)
	print("Đã sắp xếp theo số điện thoại !")
	showContacts()
	i=input()



def sortContactsByName():
	with open("data.json", encoding='utf-8') as f:
		data = json.load(f)
	listName = []
	print("Chức năng: Sắp xếp theo tên:")
	for i, j in data.items():
		listName.append(i)
	bucketSortByName(listName)
	dataSorted = {}
	for x in listName:
		for name, phone in data.items():
			if str.lower(x) == str.lower(name):
				dataSorted[name] = phone
	with open("data.json",'w', encoding='utf-8') as f:
		json.dump(dataSorted, f)
	print("Đã sắp xếp theo tên !")
	showContacts()
	i=input()


def isContacts(nameOrPhone):
	found = 0
	for name, phone in data.items():
		if nameOrPhone == phone or nameOrPhone == name:
			print("Tìm thấy!")
			print(name + " : " + phone)
			found = 1
			return name
	if found == 0:
		print("Không tìm thấy người này!")
		return "###"

def searchContact():
	print("Nhập tên hoặc số điện thoại muốn tìm kiếm : ")
	nameOrPhone = input()
	name = isContacts(nameOrPhone)
	i= input()

def menu():
	print("\n************************\n\tMenu\n")
	print("1. Hiển thị các liên lạc hiện tại")
	print("2. Thêm liên lạc")
	print("3. Sửa số liên lạc")
	print("4. Xóa số liên lạc")
	print("5. Sắp xếp theo số điện thoại")
	print("6. Sắp xếp theo tên liên lạc ")
	print("7. Tìm danh bạ")
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
		sortContactsByNumPhone()
		menu()
	elif(s == '6'):
		sortContactsByName()
		menu()
	elif(s == '7'):
		searchContact()
		menu()
	elif(s == '8'):
		exit()
	else:
		menu()

if __name__ == '__main__':
	menu()
