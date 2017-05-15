import numpy as np
import matplotlib.pyplot as plt

# define the initial -2 < x,y < 2 range, as well as a zommed in region
# to observe the fractal behaviour of the Mandelbrot set
vals = [[-2.,2.,-2.,2.],[-0.2,0.3,0.5,1.0]]

for outer_loop in range(len(vals)):
    N = 100 # resolution of image is NxN
    x = np.linspace(vals[outer_loop][0],vals[outer_loop][1],N)
    y = np.linspace(vals[outer_loop][2],vals[outer_loop][3],N)
    res = np.zeros((N,N))
    
    max_iters = 1000 # define number of iters before concluding convergence
    
    for loopx in range(N):
        for loopy in range(N):
            z = 0 # initial condition
            for loop in range(max_iters):
                c = x[loopx] + y[loopy]*1j
                z = z**2 + c # calculate z+1
                if np.isnan(z):
                    res[loopx][loopy] = 1 # array set to 1 if divergence occurs
                    break
    
    # plot the result
    plt.imshow(res, extent=[vals[outer_loop][0],vals[outer_loop][1],\
                            vals[outer_loop][2],vals[outer_loop][3]])
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()          