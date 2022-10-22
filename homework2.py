'''
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11
'''
'''
# ввод и преобразование вещественного числа в строку
digit = float(input("Введите вещественное число: "))
s_digit = str (digit) 

# замена в строке разделителя '.' типа float на 0
s_digit = s_digit.replace('.', '0')

i = 0
sum = 0
while i < len(s_digit):
  sum = sum + int(s_digit[i])
  i = i + 1
print("Сумма цифр числа составляет: ", sum) 
'''

"""
# 1. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

N = int(input("Введите число: "))
buffer = 1
s = ""
print (f"\t N\t значение \t выражение ")
for i in range (1, N+1):
      buffer = buffer * i
      s = s + str(i) + "*"
      print (f"\t {i}\t\t {buffer}\t\t {s}")
"""

"""
#1. Задайте список из n чисел последовательности $(1+ 1\n)^n и выведите на экран их сумму.
n = int(input("Введите число: "))
buffer = 0
result = 0
print (f"\t n\t значение ")
for i in range (1, n+1):
      buffer = round (((1 + (1/i))**i), 3)
      result = (result + buffer)
      print (f"\t {i}\t\t {buffer}")
print()
print("сумма элементов последовательности =", result)
"""

"""
# 1. Реализуйте алгоритм перемешивания списка.
import random
# исходный список
Original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = len(Original_list)
print("исходный список: ")
print(Original_list)
print()

# результат запишем в новый список
buffer_list = Original_list
new_list = list()

# копируем исх список в буфер, берем из него случ. элемент, кладем в новый список
# удаляем элемент из буфера
while (size >0):
    index = random.randint(0, size-1)
    new_list.append(buffer_list[index])
    del buffer_list[index]
    size = size - 1

print("Перемешанный список: ")
print(new_list)
"""


# 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.
#with open('file.txt', 'r') as f:

# генерация списка со случ числами
import random
def Create_random (size):
   n_list = list()
   for i in range (size):
      buf = random.randint((size)*(-1), (size+1) )
      n_list.insert(i, buf)
   print ("Заданный список: ")
   print (n_list)
   return n_list

# ввели N, задали список из N элементов
N = int(input("Введите (N) количество элементов списка: "))
result_list = Create_random(N)
print ()
index_list = list()
result = 1

# работа с файлом
f = open('file.txt','r')
for lines in f:
   index_list.append(int(lines))
print("номера позиций из файла")
print(index_list)
print ()

# если в файле указана позиция > N должна вернуться ошибка
max_ind = max(index_list)
if (int(max_ind) > N):
    print("в файле file.txt указано значение", max_ind, "которое больше размера исходного списка (больше N)")
# считаем результат
else:
    for i in index_list:
        result = result * result_list[i]
    print ("произведение элементов: ")
    print (result)
    