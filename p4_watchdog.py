#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys
# import textwrap
# import shutil
import subprocess
# import json
# from pathlib import Path as p
# from distutils import dir_util as du
import datetime
# from pprint import pprint as pp
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
