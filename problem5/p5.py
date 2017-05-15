import numpy as np
import matplotlib.pyplot as plt

# define function whose derivative will be approximated
def f(x):
    return x*(x-1)

delta = np.logspace(-4,-14,21) # span of delta values used

# define derivative approximation
def deriv(f,h,x=1.):
    return (f(x+h)-f(x))/h

derivatives = deriv(f,delta) # apply approxiation for all delta values

# semilog plot of the results
plt.semilogx(delta,derivatives,marker='.',linestyle='',label='approximation')
plt.axhline(y=1,color='k',label='exact value')
plt.xlabel(r'$\delta$')
plt.ylabel(r"$f'(1)$")
plt.legend(loc=0)
plt.show()

""" COMMENTS: delta=1e-4 is slightly erroneous, but after decreasing delta 
further the approximation quickly converges to the true value (f'(1)=1). 
However, roundoff errors are present after delta=1e-11 to delta=1e-14, 
demonstrating the pitfalls of float-point number storage """
