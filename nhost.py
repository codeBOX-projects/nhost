#!/bin/env python3

import socket, termcolor, subprocess, time


def tryEnquiryIP():
    subprocess.run("clear")
    info = """
    █▀▀▄ █░░█ █▀▀█ █▀▀ ▀▀█▀▀ 
    █░░█ █▀▀█ █░░█ ▀▀█ ░░█░░ 
    ▀░░▀ ▀░░▀ ▀▀▀▀ ▀▀▀ ░░▀░░
    
    [*] NHost name locater - vol 1.0
    [*] [code]Box | Andrei A.Abd - 2022.
    [*] Source : https://github.com/codeBOX-projects
    
    [?] Usage : 
        for example type > www.google.com
        for exit press (ctl+z) or (ctl+c)
    """
    print(info)
    host_enquiry = str(input("\n> Enter Host Name: "))
    host_ip = socket.gethostbyname(host_enquiry)
    print("> Result Host IP : "+ termcolor.colored("[ " + host_ip + " ]", 'green'))
if __name__ == '__main__':
    try:
        tryEnquiryIP()
        while True:
            ask = str(input(termcolor.colored("\n[?] Do you want search another Host name? y/n: ", 'green')))
            if ask == "y" or ask == "Y" or ask == "yes" or ask == "Yes" or ask == "YES":
                tryEnquiryIP()
            elif ask == "n" or ask == "N" or ask == "no" or ask == "NO":
                break
            else:
                print(termcolor.colored("[!] Erorr: please type correct answer!", 'red'))
                continue
    except:
        print(termcolor.colored("> Error Host Name: [ the Hostname is undefined ]", 'red'))
        time.sleep(1.5)

