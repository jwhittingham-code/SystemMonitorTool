import os
import psutil
import time



while True:
    
    cpuCount = psutil.cpu_count(logical=True)
    cpuPercent = psutil.cpu_percent(interval=0.1, percpu= True)
    coretemp = psutil.sensors_temperatures()['coretemp']
    #=======================================================================
    ram = psutil.virtual_memory()
    ramTotal = round(ram.total/1024/1024/1024,2)
    ramUsed = round(ram.used/1024/1024/1024,2)
    ramFree = round(ram.available/1024/1024/1024,2) 

    os.system('clear')
    print("==================")
    print("| System Monitor |")
    print("==================") 
    print("CPU Usage\n")  
    for i in range(cpuCount+1):
        core = coretemp[i][0]
        currenttemp = coretemp[i][1]
        maxtemp = coretemp[i][2]
        coreusage = cpuPercent[i-1]
        if core != 'Package id 0':
            print(f"{core}:\t {coreusage}%\nCurrent temp: {currenttemp} | Max temp: {maxtemp}\n")
        else:
            print(f"TotalUsage: {coreusage}%\nCurrent temp: {currenttemp}")
            print("-------------------\n")
    print("==========================================")
    print("RAM Usage\n")
    print(f"Total RAM: {ramTotal}GB\nRAM percent used: {ram.percent}%\nRAM used: {ramUsed}GB | RAM free: {ramFree}GB\n")
    print("==========================================")
    time.sleep(0.5)