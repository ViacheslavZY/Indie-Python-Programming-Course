# Известно, что на обработку одного квадратного метра панели требуется
# 1г сульфида. Всего необходимо обработать N прямоугольных панелей
# размером A на B метров. Вам необходимо подсчитать, сколько всего сульфида
# необходимо на обработку всех панелей. И не забудьте, что панели требуют
# обработки с обеих сторон.
# На вход программе подаются 3 положительных целых числа N,A,B в одну строку
# PS: в этой задаче обратите внимание на формат ввода. Числа вводятся в одну
# строку, поэтому вы уже не можете их так считать:
#
# n = int(input())
# a = int(input())
# b = int(input())
# Возникнет ошибка! Чтобы считать три значения, которые поступают через пробел в
# одной строке пользуйтесь следующей инструкцией
#
# n, a, b = map(int, input().split())
# Обращайте внимание на формат ввода!

n, a, b = map(int, input().split())
d = 2 * n * a * b
print(d)