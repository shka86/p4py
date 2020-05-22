#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess
import datetime
import time

# ##################################

while True:

    print("====================")
    cmd = "p4 sync"
    subprocess.run(cmd.split())

    dt = datetime.datetime.now()
    print("--------------------------------")
    print("Last sync @ " + dt.strftime('%Y/%m/%d-%H:%M:%S'))

    time.sleep(15)
