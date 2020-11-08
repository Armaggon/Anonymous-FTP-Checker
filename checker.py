#!/usr/bin/python3
import ftplib
import sys


# This tool is quite pointless all by itself, I made this purely as a fun small project when I had spare time.
# It only takes 1min to test a target for ftp anonymous login so this is tool is best to implement/ utilize with another tool.

# If you encounter the following error... "[Errno -2] Name or service not known"
# That simply means that either the host you entered is bad, or port 21 is not open.

def anonymous(ip):
    try:
        ftp=ftplib.FTP(ip)
        ftp.login('anonymous','anonymous')
        print("\n[+] "+str(ip)+": Anonymous login successful. \n[!] Target is vulnerable.")
        ftp.quit()
        return True
    except Exception as e:
        print("\n[-] Failed to login. \n[-] Could not login..."+str(e))
        return False

if len(sys.argv) < 2:
    print("[!!] Not enough arguments \n[*] Usage: " + __file__ + " <Target_IP>")
    exit()

else:
    ip=sys.argv[1]
    anonymous(ip)
