#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A script which will fetch the Weather Updates, Live News, Cricket Scores

# Copyright (C) 2016 Samsruti Dash <sam.sipun@gmail.com>

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

import json
import urllib2,urllib
from prettytable import PrettyTable
from lxml import html
import requests
import BeautifulSoup
from bs4 import BeautifulSoup
import os
from time import sleep
import lxml.etree
import json
import re
from time import gmtime, strftime

def xmlParse(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text,'lxml')
  count = 1
  for news in soup.find_all('item',limit=5):
    title = news.find("title").text
    print '\n'+str(count) + '. ' + str(title)
    count = count+1

def WeatherInput():
  print 'Today\'s weather\n '
  cityname = raw_input('Enter the city name: ')
  return cityname

def WeatherUpdates(cityname):
    
    api_key = '205fa0fe8e0455c92089ae97d508aaa7'
    url = 'http://api.openweathermap.org/data/2.5/weather?'
    values = {'q':cityname,'apikey': api_key ,'units':'metric'}
    params = urllib.urlencode(values)
    url = url + params
    response = urllib.urlopen(url)
    data = json.loads(response.read())

    t = PrettyTable([' ', ''])
    t.add_row(['City Name', data['name']])
    t.add_row(['Weather',data["weather"][0]["main"]])
    t.add_row(['Description',data["weather"][0]["description"]])
    t.add_row(['Temperature',str(data["main"]["temp"]) + ' C'])
    t.add_row(['Pressure',str(data["main"]["pressure"]) + ' hpa'])
    t.add_row(['Humidity',str(data["main"]["humidity"]) + ' %' ])
    print t

def xmlParseNews(url):
  r = requests.get(url)
  soup = BeautifulSoup(r.text,'lxml')
  for news in soup.find_all('item',limit=1):
    print news.find("title").text
    break

def NewsUpdates():
  url = 'http://feeds.feedburner.com/NdtvNews-TopStories?format=xml'
  print '\nTop Stories: '
  xmlParseNews(url)

  url = 'http://feeds.feedburner.com/ndtv/TqgX?format=xml'
  print "\nInternational News: "
  xmlParseNews(url)

  url = 'http://feeds.feedburner.com/ndtv/Lsgd?format=xml'
  print "\nNational News: "
  xmlParseNews(url)

  url = 'http://feeds.feedburner.com/NDTV-Sports?format=xml'
  print "\nSports news: "
  xmlParseNews(url)

  url = 'http://feeds.feedburner.com/NDTV-Business?format=xml'
  print "\nBusiness News: "
  xmlParseNews(url)

  url = 'http://feeds.feedburner.com/NDTV-Tech?format=xml'
  print "\nTechnology News: "
  xmlParseNews(url)


def CricketNews():
  url = "http://static.cricinfo.com/rss/livescores.xml"
  xmlParse(url)
        

def menu():
  print "\t\tPython script: Windows Widgets"
  print "Written By: Samsruti Dash"
  print ''' 
1.Weather Updates
2.News Updates
3.Cricket News
4.Exit
        '''
  ans=raw_input("Enter your Choice (1/2/3/4): ") 
  
  return ans
  
def main():
    ans = menu()
    if ans=="1": 
      q = WeatherInput()
      
    while True:
      os.system('clear')
      print 'Date: '+ strftime("%d, %B %Y")
      print 'Day: '+ strftime("%A")
      print"Time: "+strftime("%H:%M:%S", gmtime())
     
      if ans=="1": 
        WeatherUpdates(q)
      elif ans=="2":
        NewsUpdates()
      elif ans=="3":
        CricketNews()
      elif ans=='4':
        break
      else:
        print("\n Invalid Choice!! Try again")
        break
      sleep(60)
      print 'Updated Results'
      os.system('clear')
    print 'Thank you for using the script :)'
if __name__ == "__main__":
    main()