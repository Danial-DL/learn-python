import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# ایجاد شکل و محور سه‌بعدی
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# داده‌های نمونه نقاط
x = np.array([1, 2, 3, 4])
y = np.array([4, 3, 2, 1])
z = np.array([10, 15, 13, 12])

# رسم نقاط سه‌بعدی
ax.scatter(x, y, z, color='red')  # نقاط قرمز روی نمودار

# تعریف صفحه ساده: برای سادگی یک صفحه ثابت در z=11 رسم می‌کنیم
xx, yy = np.meshgrid(range(5), range(5))
zz = 11 * np.ones_like(xx)  # صفحه صاف و ثابت در ارتفاع 11

# رسم صفحه
ax.plot_surface(xx, yy, zz, alpha=0.5, color='blue')

# گذاشتن عنوان محورهای xyz
ax.set_xlabel('محور X')
ax.set_ylabel('محور Y')
ax.set_zlabel('محور Z')

# عنوان کلی نمودار
ax.set_title('نمودار سه‌بعدی با نقاط و صفحه')

plt.show()