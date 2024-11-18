import numpy as np
import matplotlib.pyplot as plt

def f(z):
	return z**3-1

def f_prime(z):
	return 3*z**2

def outside_r(z,r,z_tgt):
	dist = np.sqrt((z.real-z_tgt.real)**2+(z.imag-z_tgt.imag)**2)
	if dist <= r:
		return False
	else:
		return True

def fractals(m,r,n_max,a,b,c,d,z_tgt):
	x_coords = np.linspace(a,b,m)
	y_coords = np.linspace(c,d,m)
	working_guess = []

	for x in x_coords:
		for y in y_coords:
			n = 0
			z_n = complex(x,y)
			z_n_plus_1 = z_n - f(z_n)/f_prime(z_n)
			while outside_r(z_n_plus_1,r,z_tgt) and n <= n_max:
				n += 1
				z_n = z_n_plus_1
				z_n_plus_1 = z_n - f(z_n)/f_prime(z_n)
			if not outside_r(z_n_plus_1,r,z_tgt):
				working_guess.append(complex(x,y))
	return working_guess

def plot_fractals(z,color):
	x = []
	y = []
	for coords in z:
		x.append(coords.real)
		y.append(coords.imag)
	plt.scatter(x,y,s=1,c=color)

def main():
	root1_coords = fractals(400,0.2,20,-1.75,1.75,-1.75,1.75,complex(1,0))
	root2_coords = fractals(400,0.2,20,-1.75,1.75,-1.75,1.75,complex(-0.5,np.sqrt(3)))
	root3_coords = fractals(400,0.2,20,-1.75,1.75,-1.75,1.75,complex(-0.5,-np.sqrt(3)))
	plot_fractals(root1_coords,'b')
	plot_fractals(root2_coords,'g')
	plot_fractals(root3_coords,'r')
	plt.savefig('fig.png')
	

if __name__ == "__main__":
	main()
