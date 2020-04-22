import numpy as np
import matplotlib.pyplot as plt

# initialization
x = 0
y = 0                                   
v0 = 20       
angle = 60     
angle_rad = (angle/360) * (2 * np.pi)   
g = -9.8                                
t = 0                                   
dt = 0.02                              

# initialization array
x_arr = [x]
y_arr = [y]
t_arr = [t]

# velocity for x and y axis
vx = v0 * np.cos(angle_rad)
vy = v0 * np.sin(angle_rad)

# Update
while y >= 0:
    vy += g*dt
    y += vy*dt
    x += vx*dt
    t += dt
    if y < 0:
        break
    # store
    x_arr.append(x)
    y_arr.append(y)
    t_arr.append(t)


t_tot_num = t_arr[-1]

# Range
range_num = x_arr[-1]

# Max Height
h_max_num = np.max(y_arr)

# Analytic
x_ex_arr = [0]
y_ex_arr = [0]
for t in t_arr:
    x_ex = v0 * np.cos(angle_rad) * t
    y_ex = (0.5 * g * t**2) + (v0 * np.sin(angle_rad) * t)
    x_ex_arr = [x_ex]
    y_ex_arr = [y_ex]
#numeric
# Total Time
t_tot_ex = (2 * v0 * np.sin(angle_rad)) / -g

# Range
range_ex = v0 * np.cos(angle_rad) * t_tot_ex

# Max Height
h_max_ex = (v0**2 * np.sin(angle_rad)**2) / (-2 * g)

fig=plt.figure()
ax=fig.add_subplot(1,1,1)


# Compare
print("Numerik vs Analitik")
print("Total Time (s): %.2f vs %.2f" % (t_tot_num, t_tot_ex))
print("Range (m): %.2f vs %.2f" % (range_num, range_ex))
print("Max Height (m): %.2f vs %.2f" % (h_max_num, h_max_ex))

# Plot for Animation
plt.rcParams.update({'figure.max_open_warning': 0})
for i in range(len(y_arr)):
    plt.scatter(x_arr[i], y_arr[i], marker='o', c='b')
    plt.text(32, 14, '{:.2f} s'.format(t_arr[i]))
    plt.plot(x_arr, y_arr, c='b', label='Numerik')
    plt.plot(x_ex_arr, y_ex_arr, c='r', label='Analysis')
    plt.axhline(c='black')
    plt.axvline(c='black')
    plt.legend()
    plt.draw()
    plt.pause(0.1)
    ax.clear()
    
plt.show()