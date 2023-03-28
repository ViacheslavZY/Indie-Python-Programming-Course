# Напишите программу, которая вычисляет длину отрезка
# (т.е. расстояние между двумя точками), заданного двумя
# значениями x1 и x2 (вещественные числа).
#
# Sample Input 1:
#
# -2
# 6.5
# Sample Output 1:
#
# 8.5
# Sample Input 2:
#
# 3
# -9
# Sample Output 2:
#
# 12.0
# Sample Input 3:
#
# 5
# 3
# Sample Output 3:
#
# 2.0
# Sample Input 4:
#
# 10.5
# 8.0
# Sample Output 4:
#
# 2.5




a = int(input())
b = int(input())
c = int(input())
s1 = a + b + c
s2 = a * b + c
s3 = a * (b + c)
s4 = a + b * c
s5 = (a + b) * c
s6 = a * b * c
print(max(s1, s2, s3, s4, s5, s6))

a, b, c, d = map(int, input().split())
print((a + b + c + d) / 4)

a, b, c, d, f = map(int, input().split())
print(max(a, b, c, d, f))
