#! /usr/bin/python

import urllib2
import string

def alice(url):
    mainurl = url.split("=")[0]+"="
    while True:
        data = urllib2.urlopen(urllib2.Request(url)).read()
        print '.',
        if "and the next nothing is" not in data:
            print '!',
            print '\n'+data
        url = mainurl+''.join([x for x in data if x in string.digits])

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
print "Following the rabbit down the hole"
alice(url)
