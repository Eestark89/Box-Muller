#Box-Mueller Algorithm:
#Z_0 = R*cos(theta) = sqrt(-2ln(U1)) * cos(2*pi*U2) 
#Z_1 = R*sin(theta) = sqrt(-2ln(U1)) * sin(2*pi*U2) 
#This algorithm can be used to generate AWGN to a 2D signal or you can use one channel by itself 
#the U1 and U2 are uniform random variables, but this transform maps the uniform random variables to a Gaussian.
#The purpose of this code is to analyze the results of this transform with a taylor series expansion of -ln(x).

import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
import cmath


low = 0     #min value of uniform array
high = 1 #max value of unifomr array
size = 50000

var = 1  #variance of the gaussian distriution to control the power
var1 = 10  #since var1 is two times the value of var the awgn power will be twice

U1 = np.random.uniform(low, high, size)  #uniform RV 1
U2 = np.random.uniform(low, high, size)  #uniform RV2

x = np.linspace(0, 20, size)
nat_log = -1 *(U1-1) + ((U1-1)**2 / 2) - ((U1-1)**3 /3) + ((U1-1)**4 /4) - ((U1-1)**5 /5) + ((U1-1)**6 /6) - ((U1-1)**7 /7) + ((U1-1)**8 /8) - ((U1-1)**9 /9)      #9th order polynomial taylor series expansion
#real_ln = -1*np.log(x)
y = np.cos(2*np.pi * U2)
#mag = [cmath.sqrt(i) for i in nat_log]
#Z_0 = mag * y * 1j
Z_0 = var * np.sqrt(2*nat_log) * y 
Z_1 = var1 * np.sqrt(2*nat_log) * y


i1 = np.sin(x*10) + Z_0      #a sine wave with noise
I1_no_shift = np.fft.fft(i1)        #frequency domain of our tone with noise
I1 = np.fft.fftshift(I1_no_shift)


i2 = np.sin(x) + Z_1
I2_no_shift = np.fft.fft(i2)     
I2 = np.fft.fftshift(I2_no_shift)


plt.figure()
plt.plot(x , i1)
plt.plot(x , i2)

plt.figure()
plt.plot(x, abs(10*np.log10(I1)))
plt.plot(x, abs(10*np.log10(I2)))

#

plt.figure()
bins = np.linspace(-5, 5, 100)
plt.hist(Z_0, bins, alpha = 0.5)
plt.hist(Z_1, bins, alpha = 0.5)

plt.show()