import socket 
def retBanner(ip,port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        banner = s.recv(1024)
        return banner
    except:
        return  

def checkVulns(banner):
        if "FreeFloat Ftp Server(Version 1.00)
