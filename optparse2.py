import optparse
import socket
def connScan(tgtHost,tgtPort):
        try:
            connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            connSkt.connect((tgtHost,tgtPort))
            print('[+]%d/tcp open' % tgtPort)
            connSkt.close()
        except:
            print('[-]%d/tcp closed' % tgtPort)
def portScan(tgtHost,tgtPort):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-] Connot resolve '%s': Unknown host" % tgtHost)
        return  
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n [+] Scan Results for : ' + tgtName[0])
    except:                                                                                                                                        print('\n [+] Scan Results for :' + tgtIP)
    socket.setdefaulttimeout(1)
    
    for tgtPort in tgtports:
        print('Scaning port ' + str(tgtPort))
        connScan(tgtHost,int(tgtPort))
#test
portScan('www.baidu.com',[80,443,3389,1433,23,445])
