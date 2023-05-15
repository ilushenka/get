import numpy as np
import matplotlib.pyplot as plt

from matplotlib.pyplot import (axes,axis,title,legend,figure,
                               xlabel,ylabel,xticks,yticks,
                               xscale,yscale,text,grid,
                               plot,scatter,errorbar,hist,polar,
                               contour,contourf,colorbar,clabel,
                               imshow)

with open('settings.txt', "r") as settings:
    step = [float(i) for i in settings.read().split("\n")]
    print(step)

data_array = np.loadtxt('data.txt', dtype = int)

step_time = step[0]
voltage = step[1]

data_voltage = data_array * voltage
time_array = np.arange(0, data_array.size * step_time, step_time)

chargetime = time_array[np.where(data_array == data_array.max())[0][0]]

dischargetime = time_array.max() - chargetime

print(chargetime, dischargetime)

max_x = time_array.max()

plt.figure(figsize=(17, 10))
plt.axis([0, max_x, 0, 3.5])

plt.plot(time_array, data_voltage, 'o', ls='-', linewidth = 1, markersize = 6, markevery = 20, label=r"$U(t) = \varepsilon \cdot (1 - e^\frac{-t}{RC})$", c='b', mew = 1)

#plt.plot(time, data_voltage, 'o', ls='-', ms=4, markevery=20)

plt.text(9, 2.6, r'$Время \; зарядки \approx 5.1 \;с  $', fontsize=18)
plt.text(9, 2.4, r'$Время \; разрядки \approx 6.9 \;с$', fontsize=18)

plt.xlabel(r'$t, \; с$', fontsize = 18)
plt.ylabel(r"$U, \; В$", fontsize = 18)
title("Процесс заряда и разряда конденсатора в RC-цепи",fontsize=20)

plt.minorticks_on()

plt.grid(which='major',
        color = 'grey', 
        linewidth = 2)

plt.grid(which='minor', 
        color = 'k', 
        linestyle = ':')

plt.legend(fontsize = 20)


plt.savefig("test.png")

