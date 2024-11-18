import numpy

def newton():
	def f(x):
		return x**3 - 2*x - 5

	def f_prime(x):
		return 3*x**2 - 2

	x_n = float(input('Enter an initial guess for the root: '))
	tol = float(input('Enter a tolerance: '))
	n = 0
	x_n_plus_1 = x_n - f(x_n)/f_prime(x_n)
	while abs(1-x_n_plus_1/x_n) > tol and abs(f(x_n)) > tol:
		n += 1
		x_n = x_n_plus_1
		x_n_plus_1 = x_n - f(x_n)/f_prime(x_n)
		print(n, x_n, f(x_n))

