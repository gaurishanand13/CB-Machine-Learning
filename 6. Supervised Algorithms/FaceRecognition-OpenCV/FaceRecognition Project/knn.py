import numpy as np

def distance(X1,X2):
    diff = X1-X2
    squared = diff**2
    sum = np.sum(squared)
    return np.sqrt(sum)

def knn(Xtrain,Ytrain,XQuery,k=5):
    vals = []

    for i in range(Xtrain.shape[0]):
        d = distance(Xtrain[i],XQuery)
        vals.append([d,Ytrain[i]])


    vals = sorted(vals)
    vals = vals[:k]
    vals = np.array(vals)

    output = np.unique(vals[:,1],return_counts=True)

    index = output[1].argmax()
    return output[0][index]
