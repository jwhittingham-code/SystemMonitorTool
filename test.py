import os 
import psutil
import sys
cpuCount = psutil.cpu_count(logical=True)
print(cpuCount)
time = psutil.cpu_times()
print(time)
test = psutil.cpu_percent(interval=0.01, percpu= True)
print(test)
temp = psutil.sensors_temperatures()
print(temp)