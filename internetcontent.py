__author__ = 'Arjun Singh'
import urllib.request  #handles the url stuff from internet
data =urllib.request.urlopen('http://www.google.com').readlines(200)
for lines in data:
    print (lines)
