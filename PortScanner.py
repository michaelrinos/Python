import socket
from datetime import datetime

def main():

    server = str(input("Enter a server to check its ports: "))
    serverIp = socket.gethostbyname(server) #DNS lookup to convert google.com to ip adress 
    print("Starting the scan!")
    for port in range(1,1025):
        sock = socket(socket.AF_INET, socket.SOCK_STREAM)
        if sock.connect_ex(serverIp, port) == 0:
            print("The port %d: is Open"% (port,))
        sock.close()
main()
