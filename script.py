import requests
import json
import subprocess
import re
import sys

destination_ip = sys.argv[1]

traceroute_command = ['traceroute', destination_ip]
output = subprocess.check_output(traceroute_command, universal_newlines=True)
result = re.findall(r'\((.*?)\)', output)
del result[0]
print("Traceroute path: ",result)

for ip in result:
    getstring = "https://ipinfo.io/"+ip+"?token=9962a0d1ce1e35"
    data = requests.get(getstring)
    if data.status_code == requests.codes.ok:
        try:
            datajson = data.json()
            print(ip, " ", datajson["city"],", ",datajson["region"] )
        except:
            print(ip," is a fake ip")
    else:
        print("it didn't work")
