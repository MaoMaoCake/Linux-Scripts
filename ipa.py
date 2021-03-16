#! /usr/bin/python3

import json
import subprocess
bashCommand = "ip -j a"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
ip_json = json.loads(output)
for i in ip_json:
    for j in i.items():
        if str(j[0]) == "addr_info":
            for k in j[1][0].items():
                print(str(k[0]) + ": " + str(k[1]))
        else:
            print(str(j[0]) + ": " + str(j[1]))
    print("------------------------------------------------------------")
