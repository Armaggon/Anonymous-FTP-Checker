#!/usr/bin/python3
import ftplib
import sys

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
