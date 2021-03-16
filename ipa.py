#! /usr/bin/python3

try:
    from tabulate import tabulate
    import json
    import subprocess

    bashCommand = "ip -j a"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    ip_json = json.loads(output)
    table = []
    for i in ip_json:
        for j in i.items():
            if str(j[0]) == "addr_info":
                for k in j[1][0].items():
                    table.append((str(k[0]), str(k[1])))
            elif str(j[0]) == "ifname":
                table.append((str(j[0]), str(j[1])))
                print(f"Interface: {j[1]}")
            else:
                table.append((str(j[0]), str(j[1])))
        print(tabulate(table))
        table = []
except Exception:
    print("Please Install tabulate using: \n sudo pip3 install tabulate")
