#! /usr/bin/python

import urllib2
import io
import zipfile
import string

url = 'http://www.pythonchallenge.com/pc/def/channel.zip'
zipdata = urllib2.urlopen(urllib2.Request(url)).read()

zipdatafile = io.BytesIO(zipdata) # thanks to Jason R. Coombs and Stackoverflow
print "Is the .zip ready: "+str(zipfile.is_zipfile(zipdatafile))
zf = zipfile.ZipFile(zipdatafile)

for x in zf.infolist():
    tstr = zf.read(x.filename)
    print '.',
    if "Next nothing is" not in tstr:
        print '!',
        print '\n'+tstr
        print ""

step = "90052"
ext = ".txt"

print
print "Collecting comments, starting from "+step+ext

while step != "":
    print zf.getinfo(step+ext).comment,
    step = ''.join(x for x in zf.read(step+ext) if x in string.digits)
