import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.ndimage.filters import convolve

""" PART A """

# integrand of the definition of the Bessel fn
def integrand(m,x,theta):
    return np.cos(m*theta - x*np.sin(theta))

# numerical trapezoid rule iteration to calculate the integral
def bessel(m,x,num_slices):
    delta_theta = np.pi / num_slices # length of interval slice
    theta = np.linspace(0,np.pi,num_slices) # integration range
    result = 0
    for loop in range (num_slices-1):
        first = integrand(m,x,theta[loop]) # f(x)
        second = integrand(m,x,theta[loop+1]) #f(x+delta)
        delta_y = second - first
        result += delta_theta*(first + 0.5*delta_y) # base area plus trapezoid
    return result / np.pi
    
N = 100
x = np.linspace(0,20,N)
m = np.arange(4)
y = np.zeros((len(m),N))

# plot the function on x in [0,20] for a few values of m
for loop in range(len(m)):
    y[loop] = bessel(m[loop],x,N)
    plt.plot(x,y[loop],label='m={}'.format(m[loop]))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=0)
plt.show()

""" PART B """

# point-spread function: normalize I0 to 1, f/# of 2, lambda=0.5 m
def psf(q, I0=1, f=2.,wvlen=0.5):
    x = np.pi*q/(f*wvlen)
    return I0*(2*bessel(1,x,N)/x)**2
arr = np.linspace(-5,5,500)
X, Y = np.meshgrid(arr,arr)

Z = psf(np.sqrt(X**2+Y**2)) # psf is only radially dependent

# plot the psf, with vmin and vmax close together to improve contrast
plt.imshow(Z, vmin=0, vmax=0.05, cmap=plt.cm.Blues, extent=[-5,5,-5,5])
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.title(r'PSF (f/#=2 m$^{-1}$, wvlen=0.5 m)')
plt.show()

""" PART C """

# 3600x3600 NASA image of the Cat's Eye Nebula
# calling list(get_data)
cats_eye = Image.open('264202main_catseye_full.jpg')
plt.imshow(cats_eye, cmap=plt.cm.hsv)
plt.title('Original NASA image')
plt.show()

resolution = np.linspace(-10,10,50) # define the resolution of the PSF kernel
x_pix, y_pix = np.meshgrid(resolution, resolution)
psf_conv = np.zeros((50,50,3)) # PSF needs to handle the three pixel colours
# convolve only the first of three pixel colours, set the others to zero
psf_conv[:,:,0] = psf(np.sqrt(x_pix**2 + y_pix**2), I0=0.5)
plt.imshow(psf_conv[:,:,0], vmin=0, vmax=0.05, cmap=plt.cm.Blues, extent=[-5,5,-5,5])
plt.title('PSF kernel')
plt.show()

# convolve the image with the PSF kernel
cats_eye_telescope = convolve(cats_eye, psf_conv)

# plot result
plt.imshow(cats_eye_telescope, cmap=plt.cm.hsv)
plt.title('Convolved image')

