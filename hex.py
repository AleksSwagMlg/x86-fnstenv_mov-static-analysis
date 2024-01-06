#!/usr/bin/env python3
from pwn import *
context.arch = 'i386' 
for f in sys.argv[1:]:
    print(f"Analizing {f}\n")
    d = read(f)
    print(d.hex())
