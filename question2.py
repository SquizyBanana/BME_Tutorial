import matplotlib.pyplot as plt
import pandas as pd
import numpy
import scipy.signal as signal

var_names = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z'] # Initiate variable names
df = pd.read_csv(r'data_q2.csv', names=var_names) # Load the data
time = numpy.linspace(0,300/60, num = 301)

x_vel = numpy.cumsum((df['acc_x']*0.86)/60)
y_vel = numpy.cumsum(df['acc_y']/60)
z_vel = numpy.cumsum(df['acc_z']/60)

x_pos = numpy.cumsum(x_vel)
y_pos = numpy.cumsum(y_vel)
z_pos = numpy.cumsum(z_vel)

fig, ax = plt.subplots()
ax.plot(time,x_pos, label = "x")
ax.plot(time,y_pos, label = "y")
#ax.plot(time,z_pos, label = "z")
ax.plot(time,x_vel, label = "v x")
ax.plot(time,y_vel, label = "v y")
#ax.plot(time,z_vel, label = "v z")


ax.legend()
plt.show()