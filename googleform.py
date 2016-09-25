#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A bot which can fill the Google this Form automatically. Bot Attack is possible using this script.


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

import requests
import json 
##############################################
#DANGER: DONT TRY TO EDIT THIS
field1 = "entry.1014245086" #name
field2 = "entry.1542863080" #email-id
field3 = "entry.413373567" #kfs-id
field4 = "entry.863934741" #team-id
field5 = "entry.26092531" #contact number
##############################################
print "SAMSRUTI's BOT : A bot which can fill the Google this Form automatically :) "
teamid = "TK-0" # Enter your Team ID
'''
team_details = {
    "<name of the student1>": {
    				"email_id": "<email_id of the Student1>",
    				"kf_id": "<Kiit Fest ID of the Student1>",
    				"contact_number": "<contact_number of the Student1>"
    				 },

    "<name of the student2>": {
    				"email_id": "<email_id of the Student2>",
    				"kf_id": "<Kiit Fest ID of the Student2>",
    				"contact_number": "<contact_number of the Student2>"
    				 },
    			}


'''
team_details = {
    "Samsruti Dash": {
    				"email_id": "sam.sipun@gmail.com",
    				"kf_id": "KF02074",
    				"contact_number": "8763722872"
    				 },
}
for student in team_details:
	#print team_details[student]['email_id']
	post_data = {
					field1:student,
					field2:team_details[student]['email_id'],
					field3:team_details[student]['kf_id'],
					field4:teamid,
					field5:team_details[student]['contact_number'],
				}
	#print post_data
	url = "https://docs.google.com/forms/d/183dzmpSe9V_ixCLuT_6bd36jHaEK_I--Kj12GJ1IdyU/formResponse"
	r = requests.post(url, post_data)
	if r.status_code == 200 :
		print "Your response has been recorded."
	else:
		print "Please submit the form again. So that we can record your response. Thanks !"
	