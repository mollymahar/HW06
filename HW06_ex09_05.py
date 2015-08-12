#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou: 598
#   - # of words that use all aeiouy: 42
##############################################################################
# Imports

# Body
def uses_all(word, s):
	word = word.lower()
	s = s.lower()
	all_s = True
	for char in s:
		if word.find(char) == -1:
			all_s = False
	return all_s

def uses_all_file(s):
	with open('words.txt') as f:
		count = 0
		for word in f:
			if uses_all(word, s) == True:
				count += 1
		print str(count) + " words use " + s



##############################################################################
def main():
    print uses_all("super duper", "spud")
    uses_all_file("aeiou")
    uses_all_file("aeiouy")

if __name__ == '__main__':
    main()
