import hashlib
import os
from functools import reduce

table = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_'

def munged_class_name(path, name):
    h = hashlib.md5((path + '+' + name).encode('utf-8')).digest()
    i = reduce(lambda x, y: x * 256 + y, reversed(h), 0)
    s = ''
    while i > 0:
        s = table[i % 64] + s
        i //= 64
 
    return (
        os.path.splitext(os.path.basename(path))[0] + '__' +
        name + '___' +
        s[:5]
    )
