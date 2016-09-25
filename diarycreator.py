#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Diary Creator is a script that will help to create your diary automatically everyday.

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

import time
import os
import getpass
import platform
import datetime as dt
from sys import platform as your_os
import errno


flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY
now = time.strftime("%c")
today = dt.date.today()
tdate=today.strftime("%d %b %Y")
user=getpass.getuser()
month =today.strftime("%b")
if your_os == "linux" or your_os == "linux2":
	location = "/home/"+user+"/Desktop/My Diary/"+month+"/"
elif your_os == "win64" or your_os == "win32":
	location = "C:/"+user+"/Desktop/My Diary/"+month+"/"
if not os.path.isdir(location):
   os.makedirs(location)

name = location+tdate+".txt"

line1="Date : "+tdate
line2="\nTime : "+today.strftime("%A")
try:
    file_handle = os.open(name, flags)
except OSError as e:
    if e.errno == errno.EEXIST:
    	pass
    else: 
        raise
else:  
    with os.fdopen(file_handle, 'w') as f:
        f.write(line1)
        f.write(line2)
        f.close()

os.system("chmod +x diary.py"	)