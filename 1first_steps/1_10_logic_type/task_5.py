# На вход поступает целое положительное число.
# Программа должна вывести True, если у введенного числа последняя цифра 2,
# в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# Sample Input 1:           # Sample Input 2:
# 32                        # 76
# Sample Output 1:          # Sample Output 2:
# True                      # False

a = int(input())
print(a % 10 == 2)