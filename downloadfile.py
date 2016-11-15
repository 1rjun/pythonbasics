__author__ = 'Arjun Singh'
from urllib import request
import os
text_loc='http://www.textfiles.com/fun/10code.txt'
def text_download(loc):
    get_from_internet=request.urlopen(loc) #this will take the data from internet and store in variable
    text_file=get_from_internet.read() #read the file and save it in variable
    text_filestr =str(text_file) #convert it into str
    dest=r'code.txt'
    fw=open('code.txt','w')
    fw.write(text_filestr)
    fw.close()



text_download(text_loc)




