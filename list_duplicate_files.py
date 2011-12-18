#! /usr/bin/python2.7

import os
import os.path
from sys import argv

extension = 'mp3'
mp3 = []

def confirm(arg, directory, files):
    for File in files:
        if len(File.split('.')) == 2:
            if File.split('.')[1] == extension:
                mp3.append(os.path.join(directory, File))

os.path.walk('/media/E', confirm, None)
cmd = 'md5sum'
md5sums = []
for song in mp3:
    c = list(song)
    c.insert(0,'"')
    c.append('"')
    c = ''.join(c)
    try:
        fp = os.popen(cmd + ' ' + c)
        md5sums.append(fp.read())
    except:
        print "error"
        
print len(md5sums), '   ', len(mp3)
