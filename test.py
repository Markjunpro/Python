#-*-coding :utf-8 -*-

from optparse import OptionParser
import socket
import threading

screenLock = threading.Semaphore(value=1)
def connScan(tgtHost,tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print ('[+]%d/tcp open' % tgtPort)
        print ('[+]' + str(results))
    except:
        screenLock.acquire()
        print ('[-]%d/tcp close' % tgtPort())
    finally:
        screenLock.release()
        connSkt.close()

def portScan(thtHost,tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s':Unknown host" % tgtHost
        return 
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print ('\n[+] Scan Result for:'+ tgtName[0])
    except:
        print ('\n[+] Scan Result for:'+ tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print ('Scanning port' + str(tgtPort))
        t = threading.Thread(tgrget=connScan,agrs = (tgtHost,int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('usage %prog -H <tgrget> -p <tgrget port>')
    parser.add_option('-H',dest = 'tgtHost',type='string',help='specify target port')
    parser.add_option('-p',dest = 'tgtPort',type='int',help='specify targe port')
    (options,args) = parser.parse_args()
    tgtHost= options.tgtHost
    tgtPort=options.tgtPort
    args.append(tgtPort)
    if (tgtHost == None) | (tgtPort == None):
        print ('[-]You must specify a target host and port[s]!')
        exit(0)
    portScan(tgtHost,args)
if __name__ == '__main__':
    main()

        

