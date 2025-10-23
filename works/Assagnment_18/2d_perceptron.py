import pandas as pd
import numpy as np
from numpy.linalg import inv
df = pd.read_csv('/home/danial/project/learning_python/Assagnment_18/BostonHousing.csv')
df.head()

Y_train=df['medv']

X_train=df[['age','tax']]

Y_train_b = np.array(Y_train)
X_train_b = np.array(X_train)

class AdalineRegressor:
    def __init__(self):
        pass
    def fit(self, X_train,Y_train):
        #w = (X_train.T*X_train)^-1*X_train.T*Y_train
        self.w = np.matmul(inv(np.matmul(X_train.T, X_train)), np.matmul(X_train.T,Y_train))
        return self.w
    def predict(self, X_train):

        # self.w=self.w.reshape(1,2)
        y_pred = np.matmul(self.w.T, X_train.T)
        return y_pred
    def evaluate(self, X_test, Y_test):
        y_pred = np.matmul(X_test, self.w)
        subtract = np.abs(np.subtract(Y_test, y_pred))
        MAE = np.mean(subtract)
        return MAE
    
model = AdalineRegressor()
w = model.fit(X_train_b, Y_train_b)
print(w)

Y_pred = model.predict(X_train_b)
Y_pred = Y_pred.T

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x_feature_1 = X_train_b[:, 0]
y_feature_2 = X_train_b[:, 1]

# Create the 3D axes
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the scatter points
# X-axis: First feature (e.g., Rooms)
# Y-axis: Second feature (e.g., Age)
# Z-axis: Predicted Price
ax.scatter(x_feature_1, y_feature_2, Y_pred, c='blue', marker='o', label='Predicted Price')
ax.scatter(x_feature_1, y_feature_2, Y_train_b, c='red', marker='x', label='Actual Price')

# Plot the regression plane
x_surf, y_surf = np.meshgrid(np.linspace(x_feature_1.min(), x_feature_1.max(), 100), np.linspace(y_feature_2.min(), y_feature_2.max(), 100))
z_surf = w[0] * x_surf + w[1] * y_surf
ax.plot_surface(x_surf, y_surf, z_surf, color='green', alpha=0.5)


# Set labels for each axis
ax.set_xlabel('Age')
ax.set_ylabel('Tax')
ax.set_zlabel('Price')

# Set a title for the plot
ax.set_title('3D Plot of Predicted vs Actual House Prices with Regression Plane')

ax.legend()
plt.show()