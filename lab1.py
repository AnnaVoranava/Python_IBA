print("3.11 Даны три числа a, b, c. Значение наибольшего из них присвоить переменной d.")

a = int(4)
b = int(8)
c = int(-7)
print("Даны числа: a=", a,"b=", b,"c=", c)
d = a
if d < b:
    d = b
if d < c:
    d = c
print("Максимальное число из списка равно ", d)
print("--------------------------------------------------------------------------------------------"+"\n")
print("Дана непустая последовательность ненулевых целых чисел, за которой следует 0."+"\n"
      +" Определить, сколько раз в этой последовательности меняется знак."+"\n")
from math import copysign
lst = list(map(int, "18 -21 -49 15 10 -4 12 56 -4 0".split()))
print("Последовательность чисел:",lst)
count = -1
sig = 1
for i in lst:
    if copysign(1, i) != sig:
        count += 1
        sig = -sig

print("Знак меняется",count,"раз.")
print("--------------------------------------------------------------------------------------------"+"\n")
print("3.2 Все четные по значению элементы исходного списка A поместить в новый список B."+"\n")
import random
A = [random.randint(0, 99) for i in range(20)]
print("Рандомный список: ", A)

res = [x for x in A if not x % 2]
B=res
print("Список четных чисел: ", B)

