# У вас есть N рублей и вы хотите купить максимальное количество пар кроссовок
# по цене R рублей. Сколько пар кроссовок Вы можете себе купить?
#
# На вход программе поступают два натуральных числа N и R
# Sample Input 1:       # Sample Input 2:
# 150                   # 120
# 50                    # 41
# Sample Output 1:      # Sample Output 2:
# 3                     # 2

n = int(input())
r = int(input())
print(n // r)
