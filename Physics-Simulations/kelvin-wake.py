import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

## Our example item will be travelling to the left, ##
## but we will maintain its reference frame.        ##

nx, ny = 250,250
x_grid, y_grid = np.linspace(0,100,nx), np.linspace(-50,50,ny)
X, Y = np.meshgrid(x_grid, y_grid)
z = np.empty((ny,nx)) # wake height will be calculated into here

def trig(theta, rho, phi):
    return np.cos(rho * np.cos(theta-phi) / np.cos(theta)**2)
# print(z.shape)
for j,x in enumerate(x_grid):
    for i, y in enumerate(y_grid):
        rho = np.linalg.norm((x,y))
        phi=np.arctan2(y,x)
        z[i,j] = quad(trig, -np.pi/2, np.pi/2, args=(rho,phi))[0]
    print(f"{j}")

plt.imshow(z, interpolation="bicubic")
plt.savefig("Physics-Simulations/kelvin-wake.png")