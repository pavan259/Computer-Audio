'''
Basic implementation of Cooley-Tukey FFT algorithm in Python
 
Reference:
https://en.wikipedia.org/wiki/Fast_Fourier_transform

Creator:LUKIC DARKOO, Retrived From https://gist.github.com/lukicdarkoo/1ab6a9a7b24025cb428a
'''

import numpy as np                 #Used for multidimentional array support
import matplotlib.pyplot as plt    #including library for plotting waveform
 
SAMPLE_RATE = 8192                 #Setting up sampling rate for getting proper precise waveform
N = 128                            # Usisng the Windowing function to reduce the leakage
 
def fft(f):
    F = list()
    for k in range(0, N):
        window = 1 # np.sin(np.pi * (k+0.5)/N)**2
        F.append(np.complex(f[k] * window, 0)) #adding complex values in list
 
    fft_rec(F)
    return F
 
def fft_rec(F):
    N = len(F)           #Getting current list capacity for checking the minimum size of list and for diving them in odd and even
 
    if N <= 1:           #checking up minimum threshold value required for equation that is greater then 1  
        return
 
    even = np.array(F[0:N:2])   #Sorting the value on base of odd and even values of N
    odd = np.array(F[1:N:2])
 
    fft_rec(even)      #recursive calling method fft_rec for sorting the next value
    fft_rec(odd)
 
    for k in range(0, N//2):              #doing N/2 operations as data is divided in 2 parts odd and even
        t = np.exp(np.complex(0, -2 * np.pi * k / N)) * odd[k] 
        F[k] = even[k] + t
        F[N//2 + k] = even[k] - t
 
f_values = np.arange(0, N, 1)
f = np.sin((2*np.pi*f_values / 4.0)) # 4 - 2048Hz
f += np.sin((2*np.pi*f_values / 32.0)) # 32 - 256Hz
F = fft(f)
 
# Plotting 
_, plots = plt.subplots(2)
 
## Plot in time domain
plots[0].plot(f)
 
## Plot in frequency domain
powers_all = np.abs(np.divide(F, N//2))
powers = powers_all[0:N//2]
frequencies = np.divide(np.multiply(SAMPLE_RATE, np.arange(0, N//2)), N)
plots[1].plot(frequencies, powers)
 
plt.show() #will provide plot of result
"""
Spyder Editor
This is a temporary script file.
"""