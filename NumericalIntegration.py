import numpy as np
import matplotlib.pyplot as plt

# h = 0.25 # Original Step size

# making step size smaller will give better approximation 
# because the error is proportional to the step size and 
# to the second derivative of the function.
h = 0.10 # Step size

t = np.arange(0, 1 + h, h) # Numerical grid
s0 = -1 # Initial Condition

s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t) - 1):
    s[i + 1] = s[i] + h* np.exp(-t[i])

plt.figure(figsize = (12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

# Which h integration scheme was used in the code (Forward Euler or the midpoint method)? 
# The integration scheme used in the code is the Forward Euler method. s[i + 1] = s[i] + h * np.exp(-t[i])
# in the midpoint method: s[i + 1] = s[i] + h * np.exp(-t[i] + h/2)
