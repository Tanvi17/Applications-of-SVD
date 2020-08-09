##NOTE: uncomment to plot the images in ipynb

import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np
import os
plt.rcParams['figure.figsize'] = [16,8]

A = imread('rabbit.jpeg')
X = np.mean(A, -1); #Convert RGB to grayscale

# img = plt.imshow(256-X)
# img.set_cmap('gray')
# plt.axis('off')
# plt.show()

# create economy SVD
U, S, Vt = np.linalg.svd(X, full_matrices=False)
S = np.diag(S)

j = 0 
fig = plt.figure(figsize=(15, 8))

for r in (5, 20, 100, 200):
    #Construct approximate image
    Xapprox = U[:,:r] @ S[0:r,:r] @ Vt[:r,:]
    plt.figure(j+1)
    j += 1
    
#     img = plt.imshow(256-Xapprox)
#     img.set_cmap('gray')
#     plt.axis('off')
#     plt.title('r = ' + str(r))
#     plt.show()


# plt.semilogy(np.diag(S))
# plt.title('Log Singular Values')
# plt.show()

# plt.plot(np.cumsum(np.diag(S)/np.sum(np.diag(S))))
# plt.title('Singular Values: Cumulative Sum (Cumulative Energy in the Singular Values)')
# plt.show()
