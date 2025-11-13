import os
import psutil
import time

def updateValues():
    global cpuCount
    cpuCount = psutil.cpu_count(logical=True)
    global cpuPercent
    cpuPercent = psutil.cpu_percent(interval=0.1, percpu= True)
    global coretemp
    coretemp = psutil.sensors_temperatures()['coretemp']
    #=======================================================================
    global ram
    ram = psutil.virtual_memory()
    global ramTotal
    ramTotal = round(ram.total/1024/1024/1024,2)
    global ramUsed
    ramUsed = round(ram.used/1024/1024/1024,2)
    global ramFree
    ramFree = round(ram.available/1024/1024/1024,2) 

def cpuCores():
    coredict = {}
    for i in range(cpuCount + 1):
       core = coretemp[i][0]
       currenttemp = coretemp[i][1]
       maxtemp = coretemp[i][2]
       coreusage = cpuPercent[i-1] 
       coredict[i] = {"core" : core,"currenttemp": currenttemp,"maxtemp" : maxtemp,"coreusage" : coreusage}
    return coredict


while True:
    
    updateValues()
    coredict = cpuCores()

    os.system('clear')
    print("==================")
    print("| System Monitor |")
    print("==================") 
    print("CPU Usage\n")  
    for i in coredict:
        if coredict[i]["core"] != 'Package id 0':
            print(f"{coredict[i]['core']}:\t {coredict[i]['coreusage']}%\nCurrent temp: {coredict[i]['currenttemp']} | Max temp: {coredict[i]['maxtemp']}\n")
        else:
            print(f"TotalUsage: {coredict[i]['coreusage']}%\nCurrent temp: {coredict[i]['currenttemp']}")
            print("-------------------\n")
    print("==========================================")
    print("RAM Usage\n")
    print(f"Total RAM: {ramTotal}GB\nRAM percent used: {ram.percent}%\nRAM used: {ramUsed}GB | RAM free: {ramFree}GB\n")
    print("==========================================")
    time.sleep(0.5)