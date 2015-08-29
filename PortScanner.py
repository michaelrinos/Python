import socket


def main():

    server = input("Enter a server to check its ports: ")
    serverIp = socket.gethostbyname(server) #DNS lookup to convert google.com to ip adress 
    print("Starting the scan!")
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        response = sock.connect_ex((serverIp,port)) 
        if response == 0:
            print("The port %d: is Open"% (port,))
        sock.close()
main()
