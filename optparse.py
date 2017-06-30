#coding = utf-8
import optparse
parser= optparse.OptionParser('usage %prog -H <target host> -p <targer port>')
parser.add_option ('-H',dest = 'tgtHost',type='string',help='speify target host')
parser.add_option('-p',dest='tgtPort',type='int',help='specify target port')
(option,args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgePort
if (tgtHost == None) | (tgtPort == None):
     print(parser.usage)
     exit(0)
else:
    print(tgtHost)
    print(tgtPort)
                        
