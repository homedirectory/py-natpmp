#!/usr/bin/env python
# Yiming Liu
# A NAT-PMP client implementation using NATPMP.py 

import getopt, sys
try:
    import natpmp as NATPMP
except ImportError:
    import NATPMP

USAGE="usage: natpmp-client.py [-u] [-l lifetime] [-g gateway_addr] public_port private_port"

def main():
    if len(sys.argv) < 3:
        print(USAGE)
        sys.exit(-1)

    opts, args = getopt.getopt(sys.argv[1:], "ul:g:")    

    if len(args) < 2:
        print(USAGE)
        sys.exit(-1)

    public_port = int(args[0])
    private_port = int(args[1])

    protocol = NATPMP.NATPMP_PROTOCOL_TCP
    lifetime = 3600
    gateway = None
    
    for name, val in opts:
        if name == "-u":
            protocol = NATPMP.NATPMP_PROTOCOL_UDP
        elif name == "-l":
            lifetime = int(val)
        elif name == "-g":
            gateway = val

    if not gateway:
        gateway = NATPMP.get_gateway_addr()

    print(NATPMP.map_port(protocol, public_port, private_port, lifetime, gateway_ip=gateway))

if __name__=="__main__":
    main()
    
    
