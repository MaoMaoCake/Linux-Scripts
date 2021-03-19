#! /usr/bin/python3

try:
    # tabulate is used to generate tables from the data
    from tabulate import tabulate
    import json
    import subprocess

    bashCommand = "ip -j a"  # this is the command that returns the data in json form
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)  # executes the cmd command
    output, error = process.communicate()  # get the data from the terminal instance
    ip_json = json.loads(output)  # load the data into a dictionary
    table = []  # initialise the table variable

    # start iterating through the data
    for i in ip_json:
        for j in i.items():
            # addr_info is another layer in so we need another loop
            if str(j[0]) == "addr_info":
                try:
                    for k in j[1][0].items():
                        table.append((str(k[0]), str(k[1])))
                # sometimes the data will be blank therefore we can place no info into the list
                except IndexError:
                    table.append((j[0], "No Info Found"))
            # write the interface name before tabulate gets called
            elif str(j[0]) == "ifname":
                table.append((str(j[0]), str(j[1])))
                print(f"Interface: {j[1]}")
            else:
                # if the conditions are not met we can just append it normally
                table.append((str(j[0]), str(j[1])))
        # print out the data that we have created
        print(tabulate(table))
        # reset the table after every interface
        table = []
# catch people without tabulate and tell them to install
except ImportError:
    print("Please Install tabulate using: \n sudo pip3 install tabulate")
# catch any other exception
except Exception as e:
    print(e)
