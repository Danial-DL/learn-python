import numpy as np
import matplotlib.pyplot as plt

N = 200

def data_generator(N):
    X = np.random.uniform(0,40,200)
    Y = X*2 +np.random.normal(0,2,N)

    X = X.reshape(-1,1)
    Y = Y.reshape(-1,1)

    # print(X.shape)
    # print(Y.shape)

    return X , Y

# data_generator(N)
X_Train , Y_Train = data_generator(N)
# print(X_Train)
# print('==========')
# print(Y_Train)

print("X_Train : " , X_Train)
print("Y_Train : " , Y_Train)
w = np.random.rand(1,1)

# print(w)
lr = 0.0001

fig,ax = plt.subplots()

for i in range(N):
    print(X_Train[i])
    print(w)
    Y_pred = np.matmul(X_Train[i],w)
    e = Y_Train[i] - Y_pred # formol find error
    print("e : ",e)
    w = w + e * lr * X_Train[i] # formol 
    print("w : " , w)
    Y_Predic = np.matmul(X_Train,w)
    # print("Y_Predic : " , Y_Predic)
    ax.clear()

    plt.scatter(X_Train,Y_Train,c='red')
    # plt.plot(X_Train,Y_Predic,lw=2)
    ax.plot(X_Train,Y_Predic , lw=2)
    # plt.show()
    plt.pause(0.1)
print(w)

