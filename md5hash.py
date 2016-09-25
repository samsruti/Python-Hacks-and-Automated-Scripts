#!/usr/bin/env python
# -*- coding: utf-8 -*-
# MD5 Hash Encryption and Decryption 

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

import urllib
import urllib2
from lxml import html
import requests
import BeautifulSoup

url = 'http://md5decrypt.net/en/'

def parserHTML(values):
  data = urllib.urlencode(values)
  req = urllib2.Request(url, data)
  response = urllib2.urlopen(req)
  page = response.read()
  soup = BeautifulSoup.BeautifulSoup(page)
  answer = ''
  for i in soup.findAll('fieldset'):
    for j in i.findAll('b'):
      answer =  j.text
  return answer

def encryption(string):
  values = { 'hash': string,'crypt': 'Encrypt' }
  md5hash = parserHTML(values)
  print "Encrypted MD5 Hash: ", md5hash
  
def decryption(string):
  values = { 'hash': string,'decrypt': 'Decrypt' }
  resultString = parserHTML(values)
  print "Decrypted MD5 Hash: ", resultString

ans=True
print "\t\tPython script: MD5 Decryption and Encryption"
print "Written By: Samsruti Dash"
while ans:
    print ''' 
1.Encryption
2.Decryption
3.Exit(Terminate)
    '''
    ans=raw_input("Enter your Choice (1/2/3): ") 
    if ans=="1": 
      string = raw_input('Enter the string for encryption: ')
      encryption(string) 
      break
    elif ans=="2":
      string = raw_input('Enter the string for decryption: ')
      decryption(string)
      break
    elif ans=="3":
      break
    elif ans !="":
      print("\n Invalid Choice!! Try again") 
print "Thank you for using this script !!"