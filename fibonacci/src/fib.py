# a simple script to calculate the F(n), being n a number given and F(x) the fibonacci series.  

def fib(a):
	n=int(a)
	a = 0
	b = 1 
	if n < 2: 
		return n
	else:
		return fib(n-1) + fib(n-2)



x = input("Fibonacci Recursivo: \n Ingrese número:")
print('Calculando F({0})'.format(x))
print('F{0}={1}'.format(x,fib(x)))

for y in range(0,int(x)): #just for testing, this is not optimal 
	print('Calculando F({0})'.format(y))
	print('F{0}={1}'.format(y,fib(y)))

