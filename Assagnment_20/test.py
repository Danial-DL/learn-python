import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/home/danial/project/learning_python/Assagnment_20/BostonHousing.csv')

df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum()

print(df.head())

y_train = df['medv']

# print(y_train)
# print(y_train.shape)

x_train = df['rm', 'age', 'dis']

# print(x_train)
# print(x_train.shape)

y_train = np.array(y_train)
x_train = np.array(x_train)

x_train = x_train.reshape(501,1)
y_train = y_train.reshape(501,1)

# print(x_train)
# print(y_train)

# print(x_train.shape)
# print(y_train.shape)

w = np.random.rand(1,1)
b = np.random.rand(1,1)

lr = 0.001
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,6))
# print(len(x_train))
# print(len(y_train))
def relu(x):
    return np.maximum(0,x)

errors = [] # list Errors
epochs = 3 # Number of learning iterations

for j in range(epochs):
    for i in range(len(x_train)):
        # print(x_train[i])
        # print(w)

        Y_pred = relu(np.matmul(x_train[i],w) + b)
        e = y_train[i] - Y_pred # formol find error
        # print("e : ",e)
        w = w + e * lr * x_train[i] # formol 
        b = b + lr*e # formol
        # print("w : " , w)
        Y_Predic = np.matmul(x_train,w) + b
        error = np.mean(y_train-Y_Predic)
        errors.append(error)


        # print("Y_Predic : " , Y_Predic)

        # plot data 
        ax1.clear()
        ax1.set_title("Data")
        ax1.set_xlabel("Average Number of Rooms (rm)")
        ax1.set_ylabel("Median Value (medv)")
        ax1.scatter(x_train,y_train,s=1 ,c='#ff0000')
        # plt.plot(X_Train,Y_Predic,lw=2)
        ax1.plot(x_train ,Y_Predic , "-c",lw=2)
        ax1.set_ylim(bottom=-1)

        # plot Error
        ax2.clear()
        ax2.set_title("Loss (Mean Absolute Error)")
        ax2.plot(errors , '-b' , lw=1)
 

        plt.pause(0.1)
    plt.show()