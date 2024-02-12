import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


fig, ax = plt.subplots()
line, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line2, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line3, = ax.plot([], [], 'g--')     # A tuple unpacking to unpack the only plot
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 1.1)

x_main = np.linspace(0, 3, 300)
y_main = np.zeros(300)
y_main[120:180,] = 1

results_x = []
results_y = []

def calc_func(frame_num):
    x = np.linspace(frame_num/100, 1+frame_num/100, 100)
    y = (x - frame_num/100) * 2
    y[50:] = 2 - y[50:]
    return x, y

def animate(frame_num):
    global results_x, results_y
    if frame_num == 0:
        results_x = []
        results_y = []
    line.set_data(x_main, y_main)
    x, y = calc_func(frame_num)
    line2.set_data(x, y)
    results_x.append(frame_num/100)
    results_y.append(np.dot(y, y_main[frame_num:frame_num+100])/50)
    line3.set_data(results_x, results_y)
    return line

anim = FuncAnimation(fig, animate, frames=200, interval=10)
plt.show()

# ---------------------
fig, ax = plt.subplots()
line, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line2, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line3, = ax.plot([], [], 'g--')     # A tuple unpacking to unpack the only plot
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 1.1)

results_x = []
results_y = []
x_main = np.linspace(0, 3, 300)
y_main = np.zeros(300)
y_main[120:150,] = (x_main[120:150,] - 1.2) * 3
y_main[150:180,] = (1.5 - x_main[120:150,]) * 3

def calc_func(frame_num):
    x = np.linspace(frame_num/100, 1+frame_num/100, 100)
    y = np.ones(100)
    y[0] = y[-1] = 0
    return x, y

anim = FuncAnimation(fig, animate, frames=200, interval=10)
plt.show()

# ---------------------
fig, ax = plt.subplots()
line, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line2, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line3, = ax.plot([], [], 'g--')     # A tuple unpacking to unpack the only plot
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 2.1)

x_main = np.linspace(0, 3, 300)
y_main = np.zeros(300)
y_main[120:180,] = 1

results_x = []
results_y = []

def calc_func(frame_num):
    x = np.linspace(frame_num/100, 1+frame_num/100, 100)
    y = np.ones(100)
    y[0] = y[-1] = 0
    return x, y

anim = FuncAnimation(fig, animate, frames=200, interval=10)
plt.show()

# ---------------------
fig, ax = plt.subplots()
line, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line2, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line3, = ax.plot([], [], 'g--')     # A tuple unpacking to unpack the only plot
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 1.1)

results_x = []
results_y = []
x_main = np.linspace(0, 3, 300)
y_main = np.zeros(300)
y_main[100:120,] = (x_main[100:120,] - 1.) * 3
y_main[120:150,] = y_main[119]
y_main[150:170,] = (1.7 - x_main[150:170,]) * 3

def calc_func(frame_num):
    x = np.linspace(frame_num/100, 1+frame_num/100, 100)
    y = np.ones(100) * 0.5
    y[0] = y[-1] = 0
    return x, y

anim = FuncAnimation(fig, animate, frames=200, interval=10)
plt.show()

# ---------------------
fig, ax = plt.subplots()
line, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line2, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line3, = ax.plot([], [], 'g--')     # A tuple unpacking to unpack the only plot
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 1.1)

results_x = []
results_y = []
x_main = np.linspace(0, 3, 300)
y_main = np.zeros(300)
y_main[120:150,] = (x_main[120:150,] - 1.2) * 3
y_main[150:180,] = (1.5 - x_main[120:150,]) * 3

def calc_func(frame_num):
    x = np.linspace(frame_num/100, 1+frame_num/100, 100)
    y = np.zeros(100)
    y[30:60] = 0.5
    return x, y

anim = FuncAnimation(fig, animate, frames=200, interval=10)
plt.show()

# ---------------------
fig, ax = plt.subplots()
line, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line2, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line3, = ax.plot([], [], 'g--')     # A tuple unpacking to unpack the only plot
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 1.1)

results_x = []
results_y = []
x_main = np.linspace(0, 3, 300)
y_main = np.zeros(300)
y_main[120:150,] = (x_main[120:150,] - 1.2) * 3
y_main[150:180,] = (1.5 - x_main[120:150,]) * 3

anim = FuncAnimation(fig, animate, frames=200, interval=10)
plt.show()

# ---------------------

fig, ax = plt.subplots()
line, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line2, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line3, = ax.plot([], [], 'g--')     # A tuple unpacking to unpack the only plot
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 1.1)

results_x = []
results_y = []
x_main = np.linspace(0, 3, 300)
y_main = np.zeros(300)
y_main[100:130,] = (x_main[100:130,] - 1) * 3
y_main[130:190,] = (1.6 - x_main[130:190,]) * 3

anim = FuncAnimation(fig, animate, frames=200, interval=10)
plt.show()

# ---------------------
fig, ax = plt.subplots()
line, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line2, = ax.plot([], [])     # A tuple unpacking to unpack the only plot
line3, = ax.plot([], [], 'g--')     # A tuple unpacking to unpack the only plot
ax.set_xlim(0, 3)
ax.set_ylim(-1.1, 1.1)

results_x = []
results_y = []
x_main = np.linspace(0, 3, 300)
y_main = np.zeros(300)
y_main[100:130,] = (x_main[100:130,] - 1) * 3
y_main[130:160,] = (1.6 - x_main[130:160,]) * 3
y_main[160:190,] = (1.6 - x_main[160:190,])

anim = FuncAnimation(fig, animate, frames=200, interval=10)
plt.show()

# ---------------------
