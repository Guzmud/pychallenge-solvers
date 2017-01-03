#! /usr/bin/python

import urllib2
import pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
data = urllib2.urlopen(urllib2.Request(url)).read()

for x in pickle.loads(data):
    l = ""
    for y in x:
        k = ""
        if y[0] == "#":
            k = "*"
        else:
            k = "."
        l += k*int(y[1])
    print l
