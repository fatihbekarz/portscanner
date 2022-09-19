#//make a port scanner
import os
import sys
import time
import socket
import threading
import subprocess
from queue import Queue
from datetime import datetime
from termcolor import colored
from colorama import init
init()
# Define our target
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()
# Add a pretty banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)
# Check what time the scan started
t1 = datetime.now()
# Using the range function to specify ports (here it will scans all ports between 1 and 65535)
# We also put in some error handling for catching errors
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        # Returns an error indicator
        result = s.connect_ex((target,port))
        # Check if the port is open
        if result ==0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("Exiting program.")
    sys.exit()
except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()
except socket.error:
    print("Couldn't connect to server")
    sys.exit()
# Checking the time again
t2 = datetime.now()
# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1
# Printing the information to screen
print('Scanning Completed in: ', total)
