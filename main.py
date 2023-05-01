import matplotlib.pyplot as plt
import pandas as pd
import numpy
name = "main"

class Main:
    def main(self):
        var_names = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z'] # Initiate variable names
        df = pd.read_csv(r'data_q1.csv', names=var_names) # Load the data
        time = numpy.linspace(0,1024/60, num = 1025)
        print(time)
        #df = pd.DataFrame.insert(6, 'time', time)
        print(df)
        df = df.cumsum()
        df.to_numpy()

        #df.plot(x= time ,y=df.acc_x, kind='line')
        fig, ax = plt.subplots()
        ax.plot(time, df)
        plt.show()

if name == "main":
    main = Main()
    main.main()
    #while True:
    #    main.main()
