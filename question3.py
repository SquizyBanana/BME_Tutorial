import matplotlib.pyplot as plt
import pandas as pd
import numpy
import scipy.signal as signal


# Load data
var_names = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z', 'norm'] # Initiate variable names
df_head = pd.read_csv(r'data_q3_head.csv', names= var_names) # Load the data
df_tibia = pd.read_csv(r'data_q3_tibia.csv', names= var_names) # Load the data
df_tibia['norm'] = numpy.sqrt(df_tibia['acc_x']*df_tibia['acc_x'] + df_tibia['acc_y']*df_tibia['acc_y'] + df_tibia['acc_z']*df_tibia['acc_z'])
df_head['norm'] = numpy.sqrt(df_head['acc_x']*df_head['acc_x'] + df_head['acc_y']*df_head['acc_y'] + df_head['acc_z']*df_head['acc_z'])

fs = 512
time = numpy.linspace(0,30720/fs, num = 30721)


fig, ax = plt.subplots()
ax.plot(time, df_head, label=var_names)
ax.plot(time, df_tibia, label=var_names)

#find peaks
peaks_l = signal.find_peaks(df_tibia['norm'],1, distance=300)
peaks_h = signal.find_peaks(df_head['norm'],1, distance=150)

#seperate data for calculation
peak_h_indecies, peak_h_values = peaks_h
peak_h_values = peak_h_values["peak_heights"]
peak_l_indecies, peak_l_values = peaks_l
peak_l_values = peak_l_values["peak_heights"]
peaks_h_corrected = []
peaks_l_corrected = []

#filter head peaks
for h in range(len(peak_h_values)):
    for l in range(len(peak_l_values)):
        if 0 < (peak_h_indecies[h] - peak_l_indecies[l]) < 150:
            peaks_h_corrected.append(peak_h_values[h])
            peaks_l_corrected.append(peak_l_values[l])
            break

norms_t = peaks_l_corrected
norms_h = peaks_h_corrected
print(numpy.mean(numpy.array(norms_t) - numpy.array(norms_h)))

ax.legend()
plt.show()


