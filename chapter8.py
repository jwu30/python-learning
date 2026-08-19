def fun(a,b):
	print(b)
	print(a)

fun(5,6)

a = ''
if not a:
	print(3)

def fun1(*b):
	for i in b:
		print(i)

fun1('a','b','c')

def fun2(**b):
	for i in b.values():
		print(i)

fun2(a='d',b='e',c='f')