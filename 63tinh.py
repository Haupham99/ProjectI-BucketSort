import json
import random

numberOfPhone = 0
phone = []

data1 = []

for i in range(1, 63):
	path = "SDT" + str(i)
	with open(path + '.json', encoding='utf-8') as f:
		data = json.load(f)

	for name, phone1 in data.items():
		phone.append(phone1)

	# numberOfPhone += len(data)
for i,phone1 in enumerate(phone):
	phone1 = phone1.replace('"','')
	if phone1[0] != '0':
		phone.remove(phone1)
	else :
		phone[i] = int(phone1)

for i in range(len(phone)):
	phone[i] = int(phone[i]) - 2000000000

for i in range(100):
	data1 = []
	path = str(i+1)

	for j in range(100000):
		index = random.randint(1, len(phone)-1)
		data1.append(phone[index])

	with open('63tinh/' + path + '.json','w', encoding='utf-8') as f:
		json.dump(data1, f)

	data1 = []