import matplotlib.pyplot as plt
import pandas as pd
import numpy
import scipy.signal as signal

var_names = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z'] # Initiate variable names
df = pd.read_csv(r'data_q1.csv', names=var_names) # Load the data
time = numpy.linspace(0,1024/60, num = 1025)

fs = 60  # Sampling frequency of the sensor
fc = 0.2  # Cut-off frequency of the filter
w = (2 * fc / fs)  # Normalize the frequency
b, a = signal.butter(2, w, 'low')  # Create filter parameters
acc_y_filtered = signal.lfilter(b, a, df['acc_y'])

x_rot_acc = numpy.arctan(df['acc_y']/pow(pow(df['acc_z'],2) + pow(df['acc_x'],2), 1/2))*57.35
x_rot_gyr = numpy.cumsum(df['gyr_x']/60)

xa_fs = 60  # Sampling frequency of the sensor
xa_fc = 5  # Cut-off frequency of the filter
xa_w = (2 * xa_fc / xa_fs)  # Normalize the frequency
xa_b, xa_a = signal.butter(2, xa_w, 'low')  # Create filter parameters
x_rot_acc_filtered = signal.lfilter(xa_b, xa_a, x_rot_acc)

xg_fs = 60  # Sampling frequency of the sensor
xg_fc = 0.2  # Cut-off frequency of the filter
xg_w = (2 * xg_fc / xg_fs)  # Normalize the frequency
xg_b, xg_a = signal.butter(2, xg_w, 'high')  # Create filter parameters
x_rot_gyr_filtered = signal.lfilter(xg_b, xg_a, x_rot_gyr)

#df.plot(x= time ,y=df.acc_x, kind='line')
fig, ax = plt.subplots()

#ax.plot(time,acc_y_filtered)
#ax.plot(time, df, label=var_names)


ax.plot(time, x_rot_acc, label = 'accelerometer')
ax.plot(time, x_rot_gyr, label = 'gyroscope')
#ax.plot(time, x_rot_acc_filtered, label='acc_f')
#ax.plot(time, x_rot_gyr_filtered, label='gyr_f')
ax.plot(time,(x_rot_acc*0.2 + x_rot_gyr*0.8), label='comp')

ax.legend()
plt.show()

