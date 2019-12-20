import codecs
import json

for i in range(1,63):
	file_name = "SDT"+str(i)
	f = codecs.open(file_name + '.txt', encoding='utf-8')

	#Dữ liệu cuối cùng
	dataDict = {}

	#Cho dữ liệu vào mảng
	arr = []
	k = 0

	#Dữ liệu thô
	data = f.read()

	f.close()

	arr = data.split(',')
	print(arr[0])

	i = 0
	for x in arr:
		x = x[1:len(x)-1]
		# print(x)
		nameAndPhone = x.split('-')

		if(len(nameAndPhone) > 2):
			nameAndPhone[0] = nameAndPhone[len(nameAndPhone)-2]
			nameAndPhone[1] = nameAndPhone[len(nameAndPhone)-1]

		if(len(nameAndPhone) < 2):
			continue
		# print(nameAndPhone[0], nameAndPhone[1])
		nameAndPhone[1] = nameAndPhone[1].replace(' ','')
		nameAndPhone[1] = nameAndPhone[1].replace('(','')
		nameAndPhone[1] = nameAndPhone[1].replace(')','')
		nameAndPhone[1] = nameAndPhone[1].replace('.','')
		# if i < 20 :
			# print(nameAndPhone[0], nameAndPhone[1])
			# i = i+1
		dataDict[nameAndPhone[0]] = nameAndPhone[1]

	print(dataDict)
	with open(file_name+'.json', 'w', encoding='utf-8') as f:
		json.dump(dataDict, f)