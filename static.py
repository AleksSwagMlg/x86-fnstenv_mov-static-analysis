#!/usr/bin/env python3
from pwn import *
context.arch = 'i386'

for f in sys.argv[1:]:
    d = read(f)
    print(d.hex())

    # Get key
    key = d[0xd:0x11]
    
    result = xor(d[0x22:], key[:])
    print(result)