# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd

# df = pd.read_csv('/home/danial/project/learning_python/Assagnment_19/BostonHousing.csv')

# df.isnull().sum()
# df.dropna(inplace=True)
# df.isnull().sum()

# print(df.head())

# y_train = df['medv']

# # print(y_train)
# # print(y_train.shape)

# x_train = df['rm']

# # print(x_train)
# # print(x_train.shape)

# y_train = np.array(y_train)
# x_train = np.array(x_train)

# x_train = x_train.reshape(501,1)
# y_train = y_train.reshape(501,1)

# # print(x_train)
# # print(y_train)

# # print(x_train.shape)
# # print(y_train.shape)

# w = np.random.rand(1,1)
# b = np.random.rand(1,1)

# lr = 0.0001
# fig,(ax1,ax2) = plt.subplots(1,2,figsize=(12,6))
# # print(len(x_train))
# # print(len(y_train))

# errors = [] # list Errors
# epochs = 3 # Number of learning iterations

# for j in range(epochs):
#     for i in range(len(x_train)):
#         # print(x_train[i])
#         # print(w)

#         Y_pred = np.matmul(x_train[i],w) + b
#         e = y_train[i] - Y_pred # formol find error
#         # print("e : ",e)
#         w = w + e * lr * x_train[i] # formol 
#         b = b + lr*e # formol
#         # print("w : " , w)
#         Y_Predic = np.matmul(x_train,w) + b
#         error = np.mean(y_train-Y_Predic)
#         errors.append(error)


#         # print("Y_Predic : " , Y_Predic)

#         # plot data 
#         ax1.clear()
#         ax1.set_title("Data")
#         ax1.set_xlabel("Average Number of Rooms (rm)")
#         ax1.set_ylabel("Median Value (medv)")
#         ax1.scatter(x_train,y_train,s=1 ,c='#ff0000')
#         # plt.plot(X_Train,Y_Predic,lw=2)
#         ax1.plot(x_train ,Y_Predic , "-c",lw=2)
#         ax1.set_ylim(bottom=-1)

#         # plot Error
#         ax2.clear()
#         ax2.set_title("Loss (Mean Absolute Error)")
#         ax2.plot(errors , '-b' , lw=1)
 

#         plt.pause(0.1)
#     plt.show()


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

# --- 1. بارگذاری، پاکسازی و حذف داده‌های پرت ---
df = pd.read_csv('/home/danial/project/learning_python/Assagnment_19/BostonHousing.csv')
df.dropna(inplace=True)

# حذف داده‌های پرت (Outlier Removal)
Q1 = df['medv'].quantile(0.25)
Q3 = df['medv'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df_filtered = df[(df['medv'] >= lower_bound) & (df['medv'] <= upper_bound)]

# --- 2. آماده‌سازی و استانداردسازی داده‌ها ---
y_data = df_filtered['medv'].values.reshape(-1, 1) # medv
x_data = df_filtered['rm'].values.reshape(-1, 1)  # rm

# استانداردسازی
scaler_x = StandardScaler()
scaler_y = StandardScaler()

x_train_scaled = scaler_x.fit_transform(x_data)
y_train_scaled = scaler_y.fit_transform(y_data)

# ذخیره داده‌های اصلی برای رسم نمودار قابل فهم
X_orig = x_data
Y_orig = y_data

m = len(x_train_scaled) # تعداد نمونه‌ها

# --- 3. پیاده‌سازی و نمایش گرادیان کاهشی با پارامترهای شروع خاص ---

# **تغییر کلیدی:** تنظیم w و b به صورت دستی برای شروع از پایین نمودار
w = np.array([[0.5]])  # یک شیب مثبت کوچک اما منطقی
b = np.array([[-5.0]]) # **بایاس منفی بزرگ** برای شروع خط از پایین

lr = 0.01      # نرخ یادگیری
epochs = 100000   # تعداد اپوک‌ها

errors = [] # لیست خطاها (Loss)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

for j in range(epochs):
    # الف. محاسبه پیش‌بینی
    Y_pred_scaled = np.matmul(x_train_scaled, w) + b

    # ب. محاسبه خطا (Mean Squared Error - MSE)
    cost = np.mean((Y_pred_scaled - y_train_scaled)**2)
    errors.append(cost)

    # ج. محاسبه گرادیان‌ها
    # dJ/dw = (1/m) * Σ(Y_pred - y) * x
    dw = (1/m) * np.sum((Y_pred_scaled - y_train_scaled) * x_train_scaled)
    # dJ/db = (1/m) * Σ(Y_pred - y)
    db = (1/m) * np.sum(Y_pred_scaled - y_train_scaled)

    # د. به‌روزرسانی پارامترها
    w = w - lr * dw
    b = b - lr * db

    # ه. به‌روزرسانی نمودارها
    if j % 5 == 0 or j == epochs - 1: # هر 5 اپوک و در انتها نمایش داده شود
        
        # ۱. تبدیل پیش‌بینی‌های scaled به مقیاس اصلی برای رسم خط
        Y_pred_orig = scaler_y.inverse_transform(Y_pred_scaled)
        
        # ۲. مرتب‌سازی برای رسم خط صاف
        sort_axis = np.argsort(X_orig.flatten())
        X_sorted = X_orig[sort_axis]
        Y_pred_sorted = Y_pred_orig[sort_axis]

        # --- به‌روزرسانی نمودار داده‌ها و خط رگرسیون (محور اول) ---
        ax1.clear()
        ax1.set_title(f"Epoch {j}: Line Moving Up", fontsize=14)
        ax1.set_xlabel("Average Number of Rooms (rm)")
        ax1.set_ylabel("Median Value (medv)")
        ax1.scatter(X_orig, Y_orig, s=10, c='#ff0000', label='Actual Data')
        ax1.plot(X_sorted, Y_pred_sorted, "-b", lw=2, label=f'Line (Loss: {cost:.2f})')
        # تنظیم Y-limit برای بهتر دیدن حرکت
        ax1.set_ylim(bottom=-10, top=50) 
        ax1.legend()

        # --- به‌روزرسانی نمودار تابع هزینه (محور دوم) ---
        ax2.clear()
        ax2.set_title("Loss over Epochs", fontsize=14)
        ax2.plot(errors, '-g', lw=2)
        ax2.set_xlabel("Epochs")
        ax2.set_ylabel("Mean Squared Error (MSE)")

        plt.pause(0.05) # مکث کوتاه برای نمایش حرکت

plt.show()