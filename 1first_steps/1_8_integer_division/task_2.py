# Дележ яблок - 1
# n школьников делят k яблок поровну, неделящийся остаток
# остается в корзинке. Сколько яблок достанется каждому школьнику?
# Программа получает на вход сперва число n, а потом k.
#
# Sample Input:
# 5
# 11
# Sample Output:
# 2

n = int(input())
k = int(input())
print(k // n)
