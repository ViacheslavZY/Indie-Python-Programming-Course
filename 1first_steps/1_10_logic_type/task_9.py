# На вход поступают два слова.
# Программа должна вывести True, если хотя бы одно слово равно слову "awesome".
# Сделать задачу необходимо без использования условного оператора.
#
# Sample Input 1:           # Sample Input 2:
# cool                      # aaa
# awesome                   # aaa
# Sample Output 1:          # Sample Output 2:
# True                      # False

a = str(input())
b = str(input())
print(a == 'awesome' or b == 'awesome')
