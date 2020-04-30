'''
MD5-Crack is a (relatively) fast MD5 hash cracker written in Python 3
Current version: 1.0
Made by Louis Ware
'''

import sys
from os import system, name
import time
from cracker import MD5Crack
from datetime import datetime

legal_arguments = ["-h", "-H", "-v", "-w", "-help"]
error_msg_nohash = "Error -- please specify hash or hash file"
error_msg_nowordlist = "Error -- please specify a wordlist"
error_msg_listargs = "For list of arguments, -help"
error_msg_notvalidwordlist = "Error -- invalid wordlist specified"
error_msg_notvalidhashfile = "Error -- invalid hash file specified"

def main():
	if ((len(sys.argv) - 1) == 0):
		print("Usage: python3 MD5-CrackV1.0.py <arguments>"); print(error_msg_listargs)
		return
	for i in range(1, len(sys.argv)):
		if (sys.argv[i] in legal_arguments):
			continue
		else:
			if ("-" not in str(sys.argv[i])):
				continue
			print('"' + str(sys.argv[i]) + '"', "is not a recognised argument"); print(error_msg_listargs)
			return
	if (sys.argv[1] == "-help"):
		print("MD5-Crack -- Help page"); print("MD5-Crack is a (relatively) fast MD5 hash cracker written in Python 3"); print("Arguments:")
		print("")
		print("-h :	specify MD5 hash to crack"); print("-H :	specify list of hashes to crack (/directory/directory/MD5hashes.txt)")
		print("-w :	specify wordlist (/directory/directory/wordlist.txt)")	
		print("-c :	(to be added in V1.1) crunch mode - no wordlist is used, instead crunch is used to generate words (coming V1.1)")
		print("-v :	verbose mode")
		print("-help :	displays help page")
		print("")
		return


	print("--MD5-Cracker V1.0--"); print("--Made by Louis Ware--")

	# got this loading animation from Y4suyuki on Github: https://github.com/Y4suyuki  (yes I was too lazy to make my own)
	animation = "|/-\\"
	for k in range(30):
		time.sleep(0.1)
		sys.stdout.write("\r" + "Starting " + animation[k % len(animation)])
		sys.stdout.flush()
	print("")
	
	for j in range(1, len(sys.argv)):
		if (sys.argv[j] == "-help"):
			print("Only specify the -help argument without any other arguments")
			return
		if (sys.argv[j] == "-w"):
			try:
				path_wordlist = str(sys.argv[j + 1])
			except IndexError:
				print(error_msg_nowordlist)
				return
			try:
				wordlist = open(path_wordlist, 'r')
			except:
				print(error_msg_notvalidwordlist)
				return
			wordlist_data = wordlist.read().split()
		if (sys.argv[j] == "-h"):
			try:
				hash_tocrack = sys.argv[j + 1]
			except IndexError:
				print(error_msg_nohash)
				return
			if (len(hash_tocrack) == 32):
				TCOLOUR = '\033[32m'
				valid_text = "VALID"
				ready_text = "READY"
			else:
				TCOLOUR = '\033[31m'
				valid_text = "NOT VALID"
				ready_text = "NOT READY"
		if (sys.argv[j] == "-H"):
			hash_file = True
			try:
				path_hashes = str(sys.argv[j + 1])
			except IndexError:
				print(error_msg_nohash)
				return
			try:
				hashes = open(path_hashes, 'r')
			except:
				print(error_msg_notvalidhashfile)
				return
			hashes_data = hashes.read().split()
			if (len(hashes_data[0]) == 32):
				TCOLOUR = '\033[32m'
				valid_text = "VALID"
				ready_text = "READY"
			else:
				TCOLOUR = '\033[31m'
				valid_test = "NOT VALID"
				ready_text = "NOT READY"
			hash_tocrack = str(path_hashes) + " (number of hashes: " + str(len(hashes_data)) + ")" 
		if (sys.argv[j] == "-v"):
			verbose_mode = True

	print("")
	try:
		print("Hash or Hash file:", hash_tocrack, "(" + (TCOLOUR + valid_text + '\033[m') + ")")
	except UnboundLocalError:
		print(error_msg_nohash)
		return
	try:
		print("Wordlist:", path_wordlist," (number of words:", str(len(wordlist_data)) + ")")
	except UnboundLocalError:
		print(error_msg_nowordlist)
		return
	print("Status:", TCOLOUR + ready_text, '\033[m')
	print("")
	if (ready_text == "NOT READY"):
		print("Hash is most likely not a valid MD5 Hash, please check it")
		input("(press enter to continue)")
		return
	print("Press enter to start...")
	input()
	if (name == 'nt'): # for windows
		system('cls')
	else:		   # for linux and mac
		system('clear')

	try:
		if (verbose_mode):
			try:
				if (hash_file):
					now = datetime.now()
					time_started = now.strftime("%H:%M:%S")
					crack = MD5Crack(wordlist_data, hashes_data, True)
					crack.hash_file_verbose()
					now2 = datetime.now()
					time_ended = now2.strftime("%H:%M:%S")
					print("Started at:", time_started)
					print("Ended at:", time_ended)
			except UnboundLocalError:
				now = datetime.now()
				time_started = now.strftime("%H:%M:%S")

				crack = MD5Crack(wordlist_data, hash_tocrack, True)
				crack.single_hash_verbose()

				now2 = datetime.now()
				time_ended = now2.strftime("%H:%M:%S")
				
				print("Started at:", time_started)
				print("Ended at:", time_ended)
				return
	except UnboundLocalError:
		try:
			if (hash_file):
				now = datetime.now()
				time_started = now.strftime("%H:%M:%S")
				crack = MD5Crack(wordlist_data, hashes_data, False)
				crack.hash_file()
				now2 = datetime.now()
				time_ended = now2.strftime("%H:%M:%S")
				print("Started at:", time_started)
				print("Ended at:", time_ended)
		except UnboundLocalError:
			now = datetime.now()
			time_started = now.strftime("%H:%M:%S")

			crack = MD5Crack(wordlist_data, hash_tocrack, False)
			crack.single_hash()

			now2 = datetime.now()
			time_ended = now2.strftime("%H:%M:%S")
			
			print("Started at:", time_started)
			print("Ended at:", time_ended)
			return	
	
		

if (__name__ == '__main__'):
	main()
	
