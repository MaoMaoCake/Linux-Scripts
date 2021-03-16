#! /usr/bin/python3

import os
import sys

class WrongModeError(Exception):
    pass

class HelpError(Exception):
    pass

def set_core(mode,start_core, core_count,passed="no"):
    if passed == "yes":
        pass
    else:
        for i in range(start_core,core_count):
            with open("/sys/devices/system/cpu/cpu{0}/cpufreq/scaling_governor".format(i), "w") as f:
                f.write(str(mode))
        print("set core mode to {0} for cpu cores {1} to {2}".format(mode,start_core, core_count))


try:
    core_mode = sys.argv[1]
    if core_mode not in ["performance", "ondemand", "powersave","conservative","help"]:
        print('please enter: "performance","ondemand","powersave"')
        raise WrongModeError
    if core_mode == "help":
        print("How to use: ./powerswap.py mode_name max_core start_core")
        #raise HelpError
        skip = "yes"
    else:
        skip = "no"
    try:
        start_core = sys.argv[3]
    except IndexError:
        start_core = 0
    try:
        core_count = sys.argv[2]
    except IndexError:
        core_count = 8

    set_core(core_mode, int(start_core),int(core_count),skip)
except IndexError:
    print("please set core mode")
