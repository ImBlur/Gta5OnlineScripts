"""===GTA V SOLO PUBLIC SESSION===
        *Author = Blur#6421*
"""

import psutil
import time

def findProcess(processname):
    listofprocesses = []

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name'])
            if processname.lower() in pinfo['name'].lower():
                listofprocesses.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return listofprocesses

listofprocessid = findProcess('gta5')

if len(listofprocessid) == 1:
    print('ProcessExists | PID and other details:')
    print (listofprocessid)
    for elem in listofprocessid:
        pid = elem['pid']
        pName = elem['name']

    process = psutil.Process(pid)

    print("Creating session...")

    process.suspend()
    time.sleep(10)

    print("Session created.")

    process.resume()

else:
    print("No process found")