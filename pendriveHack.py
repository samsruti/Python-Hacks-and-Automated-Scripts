#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Used to Copy all files from one directory to another without notifying the user

# Copyright (C) 2016 Samsruti Dash <sam.sipun@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os.path import expanduser
import os, shutil
import sys

def CopyFile(src, dest,f):
    f.write('\nFile Name: '+src)
    try:
        shutil.copy(src, dest)
    	f.write('\nCopied Successfully!')

    except shutil.Error as er:
        f.write('\nOops Error: %s' % er)
    
    except IOError as er:
        f.write('\nOops Error: %s' % er.strerror)


def main():
	name = 'log.txt'
	file = open(name,'a')  
	home = expanduser("~")
 	BASE_PATH =  home+'\\Desktop\\Python Game\\gui\\test2\\'
 	DES_PATH_NAME = os.path.dirname(os.path.abspath(__file__))
 	DES_PATH = os.path.join(DES_PATH_NAME,'NEW FOLDER')
 	if not os.path.exists(DES_PATH):
 		folderName = 'New Folder'
 	else:
 		folderName = 'New folder1'
 	
 	DES_PATH = os.path.join(DES_PATH_NAME,folderName)
 	os.makedirs(os.path.join(DES_PATH))
 	os.system('attrib +s +h "%s"' % folderName)	
 	#Folder is Hidden Completely
 	#To Unhide Run "attrib -s -h "New Folder""
 	listdir = os.listdir(BASE_PATH)    
   	for file_name in listdir:
   		full_file = os.path.join(BASE_PATH, file_name)
   		CopyFile(full_file, DES_PATH,file)
   	file.close()
   	os.system('attrib +s +h "log.txt"')	
   	os.system('explorer .')
    #When the copy is done, we can get a pop up notification by opening the same folder and hiding the required files/folders :P

if __name__ == "__main__":
    main()