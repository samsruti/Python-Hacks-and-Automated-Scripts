#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Encryption and Decryption of a file and delete the file after a time interval

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

# You need to have the 'background_fileProtector.py' and 'fileProtector.py' in the same directory
import os, random, struct
from Crypto.Cipher import AES
from random import shuffle
import subprocess
from multiprocessing import Process

def join_2_files(filename1,filename2,output_filename):
    filenames = [filename1,filename2]
    with open(output_filename, 'w') as outfile:
        for fname in filenames:
            with open(fname) as infile:
                content = infile.read().replace('\n', '')
                outfile.write(content)

def split_file_into_2_parts(input_filename, output_filename1, output_filename2):
    with open(input_filename, 'r') as f:
        lines = f.readlines()
    
    lines[-1] = lines[-1].rstrip('\n') + '\n'
    shuffle(lines)

    with open(output_filename1, 'w') as f:
        f.writelines(lines[:len(lines) // 2])
    with open(output_filename2, 'w') as f:
        f.writelines(lines[len(lines) // 2:])

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

def main():  
    filename = raw_input("Enter the file name (with extension): ")
    fileextension = os.path.splitext(os.path.basename(filename))[1]
    filenameWithoutExtension =  os.path.splitext(os.path.basename(filename))[0]

    random1 = "1!q312qwrefawrqrdfs"+fileextension
    random2 = "2$q5325235231231231"+fileextension

    split_file_into_2_parts(filename,random1, random2)
    print "File got broke into 2 parts: "+random1+" and "+random2

    menu = {}
    menu['1']="Encrypt a File." 
    menu['2']="Decrypt a File."
    menu['3']="Exit"

    while True: 
      choice=menu.keys()
      choice.sort()
      for sub_menu in choice: 
        print sub_menu, menu[sub_menu]
      selection=raw_input("Please Select:") 
      if selection =='1': 
        password_input_for_encryption = raw_input("Enter the password to encrypt the file (16/24/32 size long) :")
        time = raw_input("Enter the time period you want to save the file (in minutes) : ")
        while True:
            try:
                encryptedName = filenameWithoutExtension+'.enc'
                encrypt_file(password_input_for_encryption,filename,encryptedName)
                print "encrytion done !!!"
                break
            except ValueError:
                print "Oops!  Wrong Password!!!"
           
        os.remove(filename)
     
      elif selection == '2': 
        password_input_for_decryption = raw_input("Enter the password to decrypt (16/24/32 size long) :")
        while True:
            try:
                decrypt_file(password_input_for_decryption,encryptedName,filename)
                print"File is decrypted. "
                print "File will be deleted after "+ time + " minutes"  
                join_2_files(random1,random2,filename)
                os.remove(random1)
                os.remove(random2)
                os.remove(encryptedName)
                deleteFileCommand='nohup python backgroundProcess_delete.py '+filenameWithoutExtension+' '+ fileextension+ ' '+time+ ' &'
                subprocess.Popen(deleteFileCommand,shell=True, executable='/bin/bash')
                break
            except ValueError:
                print "Oops!  Wrong Password!!!"
            break
      elif selection == '3': 
        break
      else: 
        print "Invalid Option selected :("
    

    #sleep(60*time)
main()