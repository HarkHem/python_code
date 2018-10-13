import sys
import hashlib
a = raw_input()
while 1:
    m = hashlib.md5(a)
    m = m.hexdigest()
    if (len(a) > 32):
        print(m)
        break
    a=m
