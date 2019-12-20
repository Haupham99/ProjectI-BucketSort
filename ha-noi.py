import json
import random

numberOfPhone = 0
phone = []

data1 = []

path = 'ha-noi/ha-noi'

#Mở file
with open(path + '.json', encoding='utf-8') as f:
	data = json.load(f)

for name, phone1 in data.items():
	phone.append(phone1)

#Xóa sđt ko có định dạng sđt
for i,phone1 in enumerate(phone):
	phone1 = phone1.replace('"','')
	if phone1[0] != '0':
		phone.remove(phone1)
	else :
		phone[i] = int(phone1)

#Chuẩn hóa về 9 chữ số
for i in range(len(phone)):
	phone[i] = int(phone[i])
	# if(phone[i] >= 1000000000):
		# phone.remove(phone[i])	

#Xuất file
with open('63tinh/' + 'ha-noi' + '.json','w', encoding='utf-8') as f:
	json.dump(phone, f)

def test():
	with open('ha-noi/ha-noi.json', encoding='utf-8') as f:
		data = json.load(f)

	print(len(data))

if __name__ == '__main__':
	test()

