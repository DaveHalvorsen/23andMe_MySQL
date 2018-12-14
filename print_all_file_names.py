#!/usr/bin/python

# print all file names from directory
import os
# current directory
# list = os.listdir("/media/david/Linux/23andMe_MySQL/")
# 400 file directory
# /media/david/Terabyte/2018-06-13_DOWNLOAD_PGP
list = os.listdir("/media/david/Terabyte/2018-06-13_DOWNLOAD_PGP")
# print(list)

twentythree_counter = 0

for file in list:
    #print "the current file name is: "
    #print file

    #print "the full path is: "
    full_path = "/media/david/Terabyte/2018-06-13_DOWNLOAD_PGP/" + file
    #print full_path

    file_data = open(full_path, "r")
    # this breaks up into individual lines
    lines = file_data.readlines()
    #print "the first line is: "
    #print lines[0]

    if "23andMe" not in lines[0]:
        print "wacky file is: "
        print file
        print lines[0]
        continue
    else:
        twentythree_counter += 1
print "twenty three and me files counter is: "
print twentythree_counter
