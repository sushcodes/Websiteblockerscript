import time
from datetime import datetime as dt
import os
cwd = os.getcwd()
cwd=cwd.replace("\\","/")
ip_localmachine="127.0.0.1"
website_list=[]

sites=cwd+"/FILES/BlockSites.txt"
print(sites)
with open(sites,"r+") as file:
    linelist=file.readlines()
    for element in linelist:
        element=element.strip()
        li = list(element.split(" "))
        website_list=website_list+li
print(website_list)

hosts_path="C:/Windows/System32/drivers/etc/hosts"
#hosts_path=cwd+"/FILES/textfile.txt"
with open(hosts_path,"r+") as file:
    file.seek(0)
    file.truncate()

#ABOVE LINE HAS BEEN ADDED TO DIRECTLY MODIFY THE VALUES!

with open(hosts_path,"r+") as file:
    content=file.read()
    #content.strip()
    #file.seek(0)
    #file.truncate()
    file.seek(0)
    #file.write(content)
    for website in website_list:
        if website in content:
            pass
        else:
            file.write("\n"+ip_localmachine+" "+website)
quit()
