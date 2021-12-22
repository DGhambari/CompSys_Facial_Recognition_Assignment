#!/usr/bin/env python3
#coding=utf-8

import subprocess
import logging

# Returns the list of known devices found on the network
def find_devices():

    devices = [{"name":"Brian", "mac":"34:79:16:CF:8C:E8"},
                {"name":"Darren", "mac":"48:26:2C:96:0A:67"},
                {"name":"Host PC", "mac":"04:D4:C4:48:0F:08"}]

    output = subprocess.check_output("sudo nmap -sn 192.168.0.200/24 | grep MAC", shell=True)
    devices_found=[]
    for dev in devices:   
        if dev["mac"].lower() in str(output).lower():
            # Returns a list of the names of the people currently on the network 
            devices_found.append(dev["name"])

    return(devices_found)
