import matplotlib.pyplot as plt
import numpy as np

lp = np.loadtxt('lp_2_3.txt')
lpcc = np.loadtxt('lpcc_2_3.txt')
mfcc = np.loadtxt('mfcc_2_3.txt')

plt.figure()

plt.subplot(311)
plt.scatter(lp[:,0], lp[:,1], marker=".")
plt.grid()
plt.title('LP')


plt.subplot(312)
plt.scatter(lpcc[:,0], lpcc[:,1], marker=".")
plt.grid()
plt.title('LPCC')

plt.subplot(313)
plt.scatter(mfcc[:,0], mfcc[:,1], marker=".")
plt.grid()
plt.title('MFCC')


plt.show()