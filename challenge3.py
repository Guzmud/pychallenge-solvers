#! /usr/bin/python

import urllib2
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
data = urllib2.urlopen(urllib2.Request(url)).read()
data = data.split("<!--")[-1].split("-->")[0]

pattern = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')
print ''.join([x[1:-1][3] for x in pattern.findall(data)]) 
