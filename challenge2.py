#! /usr/bin/python

import urllib2
import string

def datanalysis(data):
    tdict = {}
    
    for i in data:
        if i not in tdict:
            tdict[i] = data.count(i)
            
    return tdict

def find_ascii_letters(data):
    return ''.join([x for x in data if x in string.ascii_letters])

url = "http://www.pythonchallenge.com/pc/def/ocr.html"

print "loading the data"
data = urllib2.urlopen(urllib2.Request(url)).read()
data = data.split("<!--")[-1].split("-->")[0]

print
print "analysis"
print datanalysis(data)

print
print find_ascii_letters(data)
