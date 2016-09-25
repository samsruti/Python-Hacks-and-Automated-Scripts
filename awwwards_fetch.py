#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Script to seach a particular category in Awwwards and export all the urls to a text file.

# Copyright (C) 2015 Samsruti Dash <sam.sipun@gmail.com>

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

from BeautifulSoup import BeautifulSoup
import requests
keyword = raw_input("Enter the search category: ")

url = 'http://www.awwwards.com/search-websites/?text='+keyword+'&submit=&search-section=on'
r  = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
url_list = []
pages_count = 1
while (pages_count>0):
	if soup.findAll("div", {"class": "no-results"}):
		break
	page_url = url+"&page="+str(pages_count)
	r  = requests.get(page_url)
	data = r.text
	soup = BeautifulSoup(data)
	#print "\n\n Page = "+str(pages_count)
	for h3 in soup.findAll("figure", {"class": "rollover site"}):
	  for a in h3.findAll("a", {"target":"_blank" ,"class":"bt-url", "href": True}):
	  	url_list.append(a["href"])	   
	pages_count+=1
	i = 0
filename = raw_input("\nEnter the file name you want to save the URLs: ")
with open(filename+".txt", 'wb') as f:
    for s in url_list:
    	i+=1
        f.write(str(i)+". "+s + '\n')
print "  Thank you for using this script :)\n   Please open the Output text file in the current directory to check the URL Lists."
