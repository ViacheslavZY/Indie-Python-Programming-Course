# Напишите программу, которая  принимает на вход три целых числа в одной
# строке через пробел и выводит их последовательно через запятую как в
# примерах ниже
# Sample Input 1:
# 1 2 3
# Sample Output 1:
# 1,2,3

z, x, c = map(int, input().split())
print(z, x, c, sep=',')
