import hashlib

class MD5Crack():
	def __init__(self, wordlist, hash_, vbmode):
		self.wordlist = wordlist
		self.hash = hash_
		self.vbmode = vbmode

	def unsuccessful_page(self):
		print("[" + '\033[31m' + "UNSUCCSESSFULL" + '\033[m' + "]", "no valid hash found")
		print("")
		print("No valid hashes were matched with the hash/hash file given. Possible reasons:")
		print("-Not in the wordlist provided, in which case try a different wordlist")
		print("-The MD5 hash/hashes provided were not valid")
		print("--quitting--")
		print("")
	
	def single_hash_verbose(self):
		correct_hash = ""
		hash_found = False
		for i in range(0, len(self.wordlist)):		
			current_word = self.wordlist[i]
			print("[" + '\033[33m' + "ATTEMPT" + '\033[m' + "]", "trying MD5 hash of", '\033[31m' + current_word + '\033[m', "against", "[" + '\033[36m' + str(self.hash) + '\033[m' + "]")
			hash_word = (hashlib.md5(current_word.encode())).hexdigest()
			if (hash_word == self.hash):
				hash_found = True
				correct_hash = current_word
				break
		
		if (hash_found):
			print("[" + '\033[32m' + "SUCCESS" + '\033[m' + "]", "valid hash found!!")
			print("")
			print("(" + '\033[32m' + (str(self.hash)) + '\033[m' + ")", "  ", correct_hash)
			print("")
		else:
			temp = MD5Crack(3, 3, 3)
			temp.unsuccessful_page()

	def single_hash(self):
		print("[" + '\033[33m' + "STATUS" + '\033[m' + "]", "started program")
		correct_hash = ""
		hash_found = False
		for i in range(0, len(self.wordlist)):		
			current_word = self.wordlist[i]
			hash_word = (hashlib.md5(current_word.encode())).hexdigest()
			if (hash_word == self.hash):
				hash_found = True
				correct_hash = current_word
				break				
		
		if (hash_found):
			print("[" + '\033[32m' + "SUCCESS" + '\033[m' + "]", "valid hash found!!")
			print("")
			print("(" + '\033[32m' + (str(self.hash)) + '\033[m' + ")", "  ", correct_hash)
			print("")
		else:
			temp = MD5Crack(3, 3, 3)
			temp.unsuccessful_page()

	def hash_file_verbose(self):
		correct_hashes = []
		hashes_for_words = []
		hashes_found = False
		for i in range(0, len(self.wordlist)):
			if (len(self.hash) == 0):
				break
			current_word = self.wordlist[i]
			hash_word = (hashlib.md5(current_word.encode())).hexdigest()
			j = 0
			while (j < len(self.hash)):
				print("[" + '\033[33m' + "ATTEMPT" + '\033[m' + "]", "trying MD5 hash of", '\033[31m' + current_word + '\033[m', "against", "[" + '\033[36m' + str(self.hash[j]) + '\033[m' + "]")
				if (hash_word == self.hash[j]):
					hashes_found = True
					correct_hashes.append(current_word)
					hashes_for_words.append(self.hash[j])
					self.hash.remove(self.hash[j])
				j += 1
			
		if (hashes_found):
			print("[" + '\033[32m' + "SUCCESS" + '\033[m' + "]", len(correct_hashes), "valid hash(es) found!!")
			print("")
			for k in range(0, len(correct_hashes)):
				print("(" + '\033[32m' + str(hashes_for_words[k]) + '\033[m' + ")", "  ", str(correct_hashes[k]))

			print("")
			if (len(self.hash) != 0):
				print("--unsuccessful--")
			for a in range(0, len(self.hash)):
				print("(" + '\033[31m' + str(self.hash[a]) + '\033[m' + ")", "   ----")
			print("")
				
		else:
			temp = MD5Crack(3, 3, 3)
			temp.unsuccsessful_page()

	def hash_file(self):
		correct_hashes = []
		hashes_for_words = []
		hashes_found = False
		for i in range(0, len(self.wordlist)):
			if (len(self.hash) == 0):
				break
			current_word = self.wordlist[i]
			hash_word = (hashlib.md5(current_word.encode())).hexdigest()
			j = 0
			while (j < len(self.hash)):
				if (hash_word == self.hash[j]):
					hashes_found = True
					correct_hashes.append(current_word)
					hashes_for_words.append(self.hash[j])
					self.hash.remove(self.hash[j])
				j += 1
			
		if (hashes_found):
			print("[" + '\033[32m' + "SUCCESS" + '\033[m' + "]", len(correct_hashes), "valid hash(es) found!!")
			print("")
			for k in range(0, len(correct_hashes)):
				print("(" + '\033[32m' + str(hashes_for_words[k]) + '\033[m' + ")", "  ", str(correct_hashes[k]))

			print("")
			if (len(self.hash) != 0):
				print("--unsuccessful--")
			for a in range(0, len(self.hash)):
				print("(" + '\033[31m' + str(self.hash[a]) + '\033[m' + ")", "   ----")
			print("")
				
		else:
			temp = MD5Crack(3, 3, 3)
			temp.unsuccsessful_page()





