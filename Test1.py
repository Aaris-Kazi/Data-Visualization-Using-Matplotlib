import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def anime(t):
    test_data = pd.read_csv(r'C:\Users\aaris\Downloads\Data-Visualization-Using-Matplotlib-master\Test.csv')
    
    i = test_data[test_data.Name == 'Afif plaavkar']
    xs, ys = [], []
    
    for line in i:
        x , y = line.split('i.Attendance','i.Subject')
        
        xs.append(y)
        ys.append(x)
    ax.clear()
    ax.plot(xs,ys)

ani = FuncAnimation(fig, anime, interval = 30, blit = True)

plt.grid(True)
plt.show()