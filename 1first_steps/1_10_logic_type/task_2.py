# На вход поступает целое число.
# Программа должна вывести True, если введенное значение является
# четным числом, в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
# Sample Input 1:       # Sample Input 2:
# 6                     # 9
# Sample Output 1:      # Sample Output 2:
# True                  # False

a = int(input())
print(a % 2 == 0)