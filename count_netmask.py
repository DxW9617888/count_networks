#!/usr/bin/env python3
import sys
try:
  import ipaddress
except Exception as e:
  exit(-1)

def count_networks(netmask):
    count = 2 << (32 - int(netmask) - 1)
    print('ip address count:', count)
    n = 0
    while n < 255:
        yield n
        n += count

def hosts(network):
    for x in network.hosts():
        yield int(str(x).split('.')[-1])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        nmk = sys.argv[1]
    else:
        print('Usage: %s <netmask(ex: 24)>' %sys.argv[0])
        exit(-1)
    try:
        int(nmk)
    except TypeError:
        print('Specify netmask(%s) is TypeError!' %(nmk))
        exit(-1)
    
    exIP = '192.168.1'
    num = 1
    for n in count_networks(nmk):
        fromIP = "%s.%s" %(exIP,n)
        print('network-ec:', fromIP.split('.')[-1], end=' / ')
        try:
            nets = ipaddress.ip_network("%s/%d" %(fromIP,int(nmk)))
        except ValueError:
            print ("value error!")
            exit(-1)        
#        if n == 0:
#            print([x for x in hosts(nets)])
        _min, _max = (min(hosts(nets)), max(hosts(nets)))
        print('range of %d: (%s~%s)' %(num, _min, _max), end=' / ')
        print('mask-ec:', str(nets.netmask).split('.')[-1], end=' / ')
        print('broadcast-ec:', str(nets.broadcast_address).split('.')[-1])
        num += 1
    
