#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function called is_abecedarian that returns True if the letters in a
# word appear in alphabetical order (double letters are ok).
#   - write is_abecedarian
# (2)
# How many abecedarian words are there?
#   - write function(s) to assist you
#   - number of abecedarian words: 596
##############################################################################
# Imports

# Body
def is_abecedarian(word):
	index = 0
	word = word.lower() 			# check everything in lowercase only for simplicity
	for char in word:
		if ord(char) >= index: 		# >= handles double letter case
			index = ord(char)
		else:
			return False
	return True

def is_abecedarian_file():
	count = 0
	with open('words.txt') as f:
		for word in f:
			if is_abecedarian(word.strip()) == True: 	# eliminate newline chars
				count += 1
		return count


##############################################################################
def main():
    print is_abecedarian("wordy")
    print is_abecedarian_file()

if __name__ == '__main__':
    main()
