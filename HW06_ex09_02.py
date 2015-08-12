#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True

def list_has_no_e():
	words_with_e = 0
	words_without_e = 0
	with open('words.txt') as f:
		for word in f:
			if word.find('e') != -1: 		# .find returns the index value if True
				words_with_e += 1
			elif word.find('E') != -1:
				words_with_e += 1
			else:
				words_without_e += 1
				print word, 				# comma eliminates extra newline from the loop
		percentage = 100 * words_without_e / (words_with_e + words_without_e)
		# I'm ok using floor division here instead of having a long decimal
		print str(percentage) + "% of the words do not have an 'e' in them."



##############################################################################
def main():
    # has_no_e()
    list_has_no_e()


if __name__ == '__main__':
    main()
