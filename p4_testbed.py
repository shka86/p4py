#!/usr/bin/python3
# -*- coding: utf-8 -*-

import subprocess

# ##################################

print("====================")
cmd = "p4 info"
print(cmd)
subprocess.run(cmd.split())

print("====================")
cmd = "p4 -V"
print(cmd)
subprocess.run(cmd.split())

print("====================")
cmd = "p4 user"
print(cmd)
# subprocess.run(cmd.split())

print("====================")
cmd = "p4 login"
print(cmd)
subprocess.run(cmd.split())

print("====================")
cmd = "p4 sync"
print(cmd)
subprocess.run(cmd.split())

print("====================")
cmd = "p4 logout"
print(cmd)
subprocess.run(cmd.split())


