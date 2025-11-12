import os
import psutil
import time


while True:
    
    cpuCount = psutil.cpu_count(logical=True)
    cpuPercent = psutil.cpu_percent(interval=0.1, percpu= True)
    coretemp = psutil.sensors_temperatures()['coretemp']
    #print(f"cpuCount: {cpuCount}\n cpuPercent: {cpuPercent} \n temp: {coretemp}")
    
    os.system('clear')

    for i in range(cpuCount+1):
        core = coretemp[i][0]
        currenttemp = coretemp[i][1]
        maxtemp = coretemp[i][2]
        coreusage = cpuPercent[i-1]
        if core != 'Package id 0':
            print(f"cpu: {core} \n{coreusage}%\nCurrent temp: {currenttemp} | Max temp: {maxtemp}\n")
    
    time.sleep(0.5)