#!/usr/bin/python3

words = {}

def read_words():
	with open("words.txt", "r") as fd:
		while True:
			word = fd.readline()
			if not word:
				break
			words[word.strip()] = False

def is_reducible(word):
	#print("Word: %s" % word)
	if word not in words:
		#print("NOT reducible: %s" % word)
		return False

	if len(word) == 1:
		#print("Reducible: %s" % word)
		words[word] = True
		return True

	if words[word]:
		return True

	for i in range(len(word)):
		new_word = word[:i] + word[i+1:]
		#print("new_word: %s" % new_word)
		if is_reducible(new_word):
			#print("Reducible: %s" % word)
			words[word] = True
			return True
	#print("NOT reducible: %s" % word)
	return False
		

read_words()

max_len = 0
max_word = None

for word in words.keys():
	if is_reducible(word):
		if len(word) > max_len:
			max_len = len(word)
			max_word = word

print(max_word)

