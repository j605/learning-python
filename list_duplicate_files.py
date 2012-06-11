#! /usr/bin/python2.7

import os
import os.path
from sys import argv
import collections

script, extension, root_path = argv

files_extension = []

def confirm(arg, directory, files):
    for File in files:
        if len(File.split('.')) == 2:
            if File.split('.')[1] == extension:
                files_extension.append(os.path.join(directory, File))

os.path.walk(root_path, confirm, None)
cmd = 'md5sum'
md5sums = []
for song in files_extension:
    c = list(song)
    c.insert(0,'"')
    c.append('"')
    c = ''.join(c)
    try:
        fp = os.popen(cmd + ' ' + c)
        md5sums.append(fp.read())
    except:
        print "error"
        
parsed_hash = {}
md5_list = list()
for item in md5sums:
    md, path = item.split(' ',1)
    if md in parsed_hash:
        parsed_hash[md].append(path.strip())
    else:
        parsed_hash[md] = [path.strip()]
    md5_list.append(md)

y = collections.Counter(md5_list)
md5_duplicates = [i for i in y if y[i] > 1]

if len(md5_duplicates) == 0:
	print "No duplicates found"
else:
	print 'Duplicates are: '
	for item in md5_duplicates:
		print parsed_hash[item]
