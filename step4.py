import numpy as np
from sklearn.decomposition import PCA
from sklearn import datasets

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(111,projection = '3d')
X = np.genfromtxt('Matrix1.csv',delimiter = ',')
pca = PCA(n_components=3)
pca.fit(X)
X_trans = pca.transform(X)
Eastgreenland = ax.scatter(X_trans.T[0,0:2],X_trans.T[1,0:2],X_trans.T[2,0:2])
ax.scatter(X_trans.T[0,4:10],X_trans.T[1,4:10],X_trans.T[2,4:10])
ax.scatter(X_trans.T[0,12:14],X_trans.T[1,12:14],X_trans.T[2,12:14])
ax.scatter(X_trans.T[0,20:22],X_trans.T[1,20:22],X_trans.T[2,20:22])
Westgreenland = ax.scatter(X_trans.T[0,2:4],X_trans.T[1,2:4],X_trans.T[2,2:4], marker = "^", color = "red")
ax.scatter(X_trans.T[0,10:12],X_trans.T[1,10:12],X_trans.T[2,10:12], marker = "^", color = "red")
ax.scatter(X_trans.T[0,14:20],X_trans.T[1,14:20],X_trans.T[2,14:20], marker = "^", color = "red")
ax.scatter(X_trans.T[0,22:],X_trans.T[1,22:],X_trans.T[2,22:], marker = "^", color = "red")
ax.legend([Eastgreenland,Westgreenland],["Eastgreenland","Westgreenland"])

print(X_trans.shape)
plt.show()
