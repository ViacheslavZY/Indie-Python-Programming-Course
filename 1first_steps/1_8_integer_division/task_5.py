# Дано целое положительное число, ваша задача вывести разряд сотен этого числа
#
# Sample Input 1:
# 123
# Sample Output 1:
# 1
# Sample Input 2:
# 56789
# Sample Output 2:
# 7

a = int(input())
print(a // 100 % 10)