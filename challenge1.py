#! /usr/bin/python

import string

def rot(data,delta,minbase,maxbase):
    temp = ""
    
    for i in data:
        if ord(i)<maxbase+1 and ord(i)>minbase-1:
            temp += chr((((ord(i)+delta)-minbase)%(maxbase-minbase+1))+minbase)
        else:
            temp += i
            
    return temp

delta = ord('G')-ord('E')
minbase = ord('a')
maxbase = ord('z')

data = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"

for x in (data,url):
    print x
    print rot(x,delta,minbase,maxbase)
    print
