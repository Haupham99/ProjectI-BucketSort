import json
import random

numberOfPhone = 0
phone = []

data1 = []

path = 'sdt-Hai-Ba-Trung'

#Mở file
with open(path + '.json', encoding='utf-8') as f:
	data = json.load(f)

for i, j in data.items():
	phone.append(j)

for i, x in enumerate(phone):
	x = int(x) - 2000000000
	phone[i] = x

numberPhoneRandom = 100000 - len(phone)

#Sinh ngau nhien :
for i in range(numberPhoneRandom):
	chuSoDau = random.randint(436,439)
	chuSoCuoi = random.randint(1,999999)

	phoneRandom = chuSoDau*1000000+chuSoCuoi
	phone.append(phoneRandom)

with open("63tinh/ha-noi.json", 'w', encoding='utf-8') as f:
	json.dump(phone, f)