# /usr/bin/python

import urllib2
import bz2

url = "http://www.pythonchallenge.com/pc/def/integrity.html"

data = urllib2.urlopen(urllib2.Request(url)).read().split("<!--\n")[1].split("\n-->")[0].split("\n")
data = [(x.split(":")[0],x.split(":")[1].split("'")[1]) for x in data]

print [(x[0],bz2.decompress(x[1].decode("string_escape"))) for x in data]
