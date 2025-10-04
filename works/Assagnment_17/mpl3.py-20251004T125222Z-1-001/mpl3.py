import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# نقاط نمونه
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
z = np.array([7, 8, 9])

ax.scatter(x, y, z, color='red')

# ساخت شبکه دوبعدی برای صفحه
X, Y = np.meshgrid(np.linspace(min(x), max(x), 10),
                   np.linspace(min(y), max(y), 10))

# صفحه صاف در ارتفاع میانگین z
Z = np.full(X.shape, np.mean(z))

# رسم صفحه
ax.plot_surface(X, Y, Z, alpha=0.5, color='blue')

# عناوین محور
ax.set_xlabel('age')
ax.set_ylabel('medv')
ax.set_zlabel('rm')

plt.show()