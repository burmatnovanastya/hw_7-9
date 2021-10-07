def check(a, b, c):
    if a < b and b < c:
        print('a < b < c')
    elif a > b and b > c:
        print('a > b > c')
    elif a == b and b == c:
        print('Ни одно из двух неравенств не выполняется')
    else:
        print('Ни одно из двух неравенств не выполняется')

try:
	a = float(input('Введите a: '))
	b = float(input('Введите b: '))
	c = float(input('Введите c: '))
	check(a, b, c)
except ValueError :
	print('Ошибка. Введите число.')