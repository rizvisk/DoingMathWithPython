'''
Plot the daily temperatures of Austin and San Diego
on the same graph
Data from weather.com for Fri Feb 12, 2021
'''

import matplotlib.pyplot as plt

time = ['12am', '2am', '4am', '6am', '8am', '10am', '12pm', '2pm', '4pm', '6pm', '8pm', '10pm']
austin = [34, 33, 33, 33, 31, 32, 35, 37, 37, 36, 34, 34]
sandiego = [55, 57, 58, 57, 58, 60, 61, 61, 61, 59, 57, 55]

plt.plot(time, austin, time, sandiego, marker='o')
plt.xlabel('Time')
plt.ylabel('Temperature (F)')
plt.title('Daily Temp on Feb 12, 2021')
plt.legend(['Austin', 'San Diego'])
plt.show()
