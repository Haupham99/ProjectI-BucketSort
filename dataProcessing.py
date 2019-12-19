import codecs
import json

f = codecs.open('Thanh-Pho-Bien-Hoa.txt', encoding='utf-8')

#Dữ liệu cuối cùng
dataDict = {}

#Cho dữ liệu vào mảng
arr = []
k = 0

#Dữ liệu thô
data = f.read()

f.close()

arr = data.split(',')
# print(arr[0])

i = 0
for x in arr:
	# x = x[1:len(x)-1]
	# print(x)
	nameAndPhone = x.split('-')

	if(len(nameAndPhone) > 2):
		nameAndPhone[0] = nameAndPhone[len(nameAndPhone)-2]
		nameAndPhone[1] = nameAndPhone[len(nameAndPhone)-1]
	if len(nameAndPhone) < 2:
		continue
	nameAndPhone[1] = nameAndPhone[1].replace('(','')
	nameAndPhone[1] = nameAndPhone[1].replace(')','')
	nameAndPhone[1] = nameAndPhone[1].replace(' ','')
	nameAndPhone[1] = nameAndPhone[1].replace('.','') 
	# if i < 20 :
		# print(nameAndPhone[0], nameAndPhone[1])
		# i = i+1

	dataDict[nameAndPhone[0]] = nameAndPhone[1]

print(len(dataDict))
with open("sdt-Thanh-Pho-Bien-Hoa.json", 'w', encoding='utf-8') as f:
	json.dump(dataDict, f)