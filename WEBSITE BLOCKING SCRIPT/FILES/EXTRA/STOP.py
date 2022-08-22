import time
from datetime import datetime as dt
import os
cwd = os.getcwd()
cwd=cwd.replace("\\","/")

website_list=[]
hosts_path="C:/Windows/System32/drivers/etc/hosts"
sites=cwd+"/FILES/BlockSites.txt"


with open(sites,"r+") as file:
    linelist=file.readlines()
    for element in linelist:
        element=element.strip()
        li = list(element.split(" "))
        website_list=website_list+li


with open(hosts_path,"r+") as file:
    content=file.read().strip()
    print(content)
    file.seek(0)
    file.truncate()
    file.seek(0)
    file.write(content)
    file.seek(0)
    ListLine=file.readlines()
    file.seek(0)
    for eachLine in ListLine:
        eachLine=eachLine.strip()
        print(eachLine)
        li = list(eachLine.split(" "))
        print(li)
        var=False
        for eachweb in website_list:
            for eachword in li:
                if eachweb==eachword:
                    var=True
                    break
            if var==True:
                break
        if var==False :
            file.write(eachLine +'\n')

    file.truncate()
    file.seek(0)
    content=file.read().strip()
    file.seek(0)
    file.truncate()
    file.seek(0)
    file.write(content)
    file.seek(0)
quit()
