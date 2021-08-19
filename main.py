from YandexImageSearch import *

file = input("Enter filename: ")
yis = YandexImageSearch(file)
print("Найдены следующие упоминания в сети: ")
for i in range(len(yis[0])):
	print(yis[0][i]+"\n")
if len(yis[1]) > 0:
	print("Найдены предпологаемы соцсети: ")
	for j in range(len(yis[1])):
		print(yis[1][j]+"\n")
else:
	print("Соцсети не найдены!")