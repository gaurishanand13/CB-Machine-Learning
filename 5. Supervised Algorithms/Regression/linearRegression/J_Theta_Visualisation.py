import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

# myTheta = np.load('./FinalData/myTheta.npy')


ThetaList = np.load('./FinalData/ThetaList.npy')
X = pd.read_csv('./Training Data/Linear_X_Train.csv')
Y = pd.read_csv('./Training Data/Linear_Y_Train.csv')

def hypothesis(x,theta):
    y_ = theta[0] + theta[1]*x
    return y_

def error(X,Y,theta):
    m = X.shape[0]
    total_error = 0.0
    for i in range(m):
        y_ = hypothesis(X[i],theta)
        total_error += (y_ - Y[i])**2
        
    return (total_error/m)
   
error_list = []
for i in range(len(ThetaList)):
	error_list.append(error(X,Y,ThetaList[i]))



T0 = np.arange(-40,40,1)  
T1 = np.arange(40,120,1) 
T0,T1 = np.meshgrid(T0,T1)





plt.style.use('seaborn')
figure = plt.figure()
axes = figure.gca(projection='3d')

axes.scatter( ThetaList[:,0] , ThetaList[:,1] , error_list,color = 'black')
plt.show()


