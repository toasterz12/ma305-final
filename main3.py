import numpy as np
import matplotlib.pyplot as plt

def f(z):
	return z**2+complex(-0.4,-0.6)

def main():
	x_coords = np.linspace(-1.5,1.5,100)
	y_coords = x_coords
	julia = np.zeros((len(y_coords),len(x_coords)))
	for i, x in np.ndenumerate(x_coords):
		for j, y in np.ndenumerate(y_coords):
			z = complex(x,y)
			n = 0
			while n <=500 and abs(z) < 10:
				z = f(z)
				n += 1
			if abs(z) >= 10:
				julia[j,i] = n
	plt.imshow(julia/500*255,cmap='magma')
	plt.colorbar()
	plt.savefig('fig.png')

if __name__ == "__main__":
	main()
