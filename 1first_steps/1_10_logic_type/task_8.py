# На вход поступает целое число.
# Программа должна вывести True, если введенное значение принадлежит
# интервалу от 5 не включительно до 19 включительно , в противном случае - False.
# Сделать задачу необходимо без использования условного оператора.
#
# Sample Input 1:       # Sample Input 2:       # Sample Input 3:
# 10                    # 5                     # 19
# Sample Output 1:      # Sample Output 2:      # Sample Output 3:
# True                  # False                 # True

a = int(input())
print(a > 5 and a <= 19)
