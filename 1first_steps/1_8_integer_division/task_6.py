# Дано целое положительное трехзначное число, ваша задача найти сумму
# разрядов этого числа
# Sample Input 1:
# 123
# Sample Output 1:
# 6
# Sample Input 2:
# 109
# Sample Output 2:
# 10

a = int(input())
b = a // 100
c = a // 10 % 10
d = a % 10
print(b + c + d)
