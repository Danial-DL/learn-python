import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ایجاد شکل و محور سه‌بعدی
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# داده‌های نقاط سه‌بعدی
x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 6, 2, 3, 13])
z = np.array([2, 3, 3, 3, 5])

# رسم نقاط سه‌بعدی
ax.scatter(x, y, z, color='r')

# تعریف بردار نرمال صفحه و یک نقطه روی صفحه
point = np.array([1, 2, 3])
normal = np.array([1, 1, 1])

# معادله صفحه ax + by + cz + d = 0
d = -point.dot(normal)

# ساخت شبکه‌ای برای x و y جهت رسم صفحه
xx, yy = np.meshgrid(range(0, 6), range(0, 15))

# محاسبه z روی صفحه
zz = (-normal[0] * xx - normal[1] * yy - d) / normal[2]

# رسم صفحه با کمی شفافیت
ax.plot_surface(xx, yy, zz, alpha=0.5)

# نمایش نمودار
plt.show()