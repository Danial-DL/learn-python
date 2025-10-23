# Adaline Regressor for Boston Housing Price Prediction

This project implements a simple **Linear Regression** model, dubbed `AdalineRegressor`, using the **Normal Equation** (also known as the Ordinary Least Squares method) to predict house prices (`medv`) based on two features: **Age** (`age`) and **Tax** (`tax`) from the Boston Housing dataset.

The model is trained to find the optimal weights that minimize the squared error between the predicted and actual prices. The results are then visualized using a **3D scatter plot** showing the actual data points, the predicted data points, and the fitted **regression plane**.

## 🛠️ Project Structure and Implementation

### 1. Data Preparation

* **Dataset:** The code reads the data from a CSV file named `BostonHousing.csv`.
* **Target Variable ($Y$):** The median value of owner-occupied homes (`medv`) is used as the target.
* **Feature Variables ($X$):** The features selected for the regression are `age` and `tax`.
* **Numpy Conversion:** The Pandas Series/DataFrame are converted to NumPy arrays (`Y_train_b`, `X_train_b`) for efficient matrix operations.

### 2. AdalineRegressor Class

The `AdalineRegressor` class encapsulates the core logic:

#### `fit(self, X_train, Y_train)`

This method calculates the optimal weight vector ($\mathbf{w}$) using the **Normal Equation**:
$$\mathbf{w} = (\mathbf{X}^T \mathbf{X})^{-1} \mathbf{X}^T \mathbf{Y}$$
* **$\mathbf{X}$**: The feature matrix (input data).
* **$\mathbf{Y}$**: The target vector (actual prices).
* The `numpy.linalg.inv` and `numpy.matmul` functions are used to perform the matrix inverse and multiplication.

#### `predict(self, X_train)`

This method computes the predicted values ($\hat{\mathbf{Y}}$) using the formula:
$$\hat{\mathbf{Y}} = \mathbf{X} \mathbf{w}$$
* The weight vector $\mathbf{w}$ found during the `fit` stage is multiplied by the feature matrix $\mathbf{X}$.

#### `evaluate(self, X_test, Y_test)`

This method calculates the **Mean Absolute Error (MAE)** to assess the model's performance on the test data (though in the provided code, it's called with the training data for demonstration).

### 3. Visualization

The results are plotted in a 3D space:

* **Axes:** The x-axis represents 'Age', the y-axis represents 'Tax', and the z-axis represents 'Price' (both actual and predicted).
* **Scatter Points:**
    * **Red 'x' markers:** Actual prices.
    * **Blue 'o' markers:** Predicted prices.
* **Regression Plane:** A semi-transparent **green** plane is plotted, representing the surface defined by the linear model:
    $$\text{Price} = \mathbf{w}_0 \cdot \text{Age} + \mathbf{w}_1 \cdot \text{Tax}$$
    This plane visually demonstrates how the model attempts to fit the data in three dimensions.

## 💻 Dependencies

To run this code, you need the following Python libraries:

* `pandas`
* `numpy`
* `matplotlib`
* `mpl_toolkits.mplot3d` (for 3D plotting)

You can install them using pip:

```bash
pip install pandas numpy matplotlib
