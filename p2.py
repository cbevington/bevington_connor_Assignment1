import numpy as np
import matplotlib.pyplot as plt
""" PART A """

print "PART A"

# first define factorial function
def fact(n):
	if type(n) == int and n >= 0: # check a non-negative int supplied
		res = 1 # default value if n=0 or n=1
		while n >= 2: # in recursion multiplying by 1 is trivial
			# multiply by given integer, decrease by 1, repeat
			res *= n
			n -= 1
		return res
	else:
		# alert user if an incorrect number is supplied
		raise ValueError("n and k need to be non-negative integers")

# define binomial function
def binomial(n, k):
	res = fact(n) / (fact(k) * fact(n-k))
	return int(res) # return an integer

# test for k=0 case
for loop in range(4):
	print ["n=%i" % loop, "k=0"], "=", binomial(loop,0) 

""" PART B """

print "\nPART B"

# print out the first 20 rows of Pascal's triangle
for n in range(20):
	row = [ ]
	for k in range(20):
		if n >= k:
			row.append(binomial(n,k))
	print(row)

""" PART C """

print "\nPART C"

# flip the coin with p=0.65 bias towards heads 20 times and hope to get at least 12 heads
n, p = 20, 0.65

result = 0
for loop in range(12,21):
	result += binomial(n,loop) * p**loop * (1-p)**(n-loop)

print "At least 12 heads in 20 flips occurs with a probability of %5.4f " % result

""" PART D """

# run the experiment N times for N in {10,10000}
N = np.logspace(1,4,100)
prob = np.zeros(len(N))

# define a biased coin-flipping function
def flipper(n_flips, p):
	count = 0
	for loop in range(n_flips):
		if np.random.rand() <= p: # determine if heads
			count += 1.
	return count # return the total number of heads
		

for loop in range(len(N)):
	count = 0
	for loop2 in range(int(N[loop])): # run the experiment N_i times for N_i in N
		if flipper(n,p) >= 12: # want at least 12 heads
			count += 1.
	prob[loop] = count / int(N[loop]) # store the fraction of successful experiments

# plot the residuals from the experiments and the theoretical probability
plt.semilogx(N,prob-result,linestyle='',marker='.')
plt.axhline(y=0, color='k')
plt.xlabel('N')
plt.ylabel(r'P$_{exp}$ - P$_{theory}$')
plt.title('Part D')
plt.show()g



