#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import random
import sys
import requests
import dictionaryapi

def get_easy_mode_display(guess, word):
	if len(guess) != len(word):
		return "[Number of letters didn't match]"

	ret = "["
	for i in range(0, len(guess)):
		if guess[i] == word[i]:
			ret += guess[i]
		else:
			ret += "_"
	
	ret += "]"

	return ret


def question(word, definition):
	revealed = 0
	guessed = False
	print("%d letter word" % len(word))
	easy_mode = False

	while True:
		guess = input("Your guess (.h=hint, .g=give up): ")
		if guess == ".h":
			revealed += 1
			if revealed == len(word):
				break
			print(word[0:revealed])
			continue

		if guess == ".g":
			guessed = False
			break

		if guess == ".e":
			if easy_mode:
				print("Easy mode turned OFF")
				easy_mode = False
			else:
				print("Easy mode turned ON")
				easy_mode = True
			continue

		if guess == word:
			guessed = True
			break
		else:
			print("❌ Incorrect")
			if easy_mode:
				print(get_easy_mode_display(guess, word))
			continue

	if guessed:
		print("✅ Correct")
	else:
		print(f"The word is: ［{word}］")


words = []
with open('words.txt', 'r') as fd:
	while True:
		word = fd.readline()
		if not word:
			break
		word = word.strip()
		words.append(word)

while True:
	index = random.randint(0, len(words))
	word = words[index]
	if word[-1] == 's':
		continue
	if word.endswith("ing"):
		continue
	if word.endswith("ed"):
		continue

	definition = dictionaryapi.get_definition(word)
	if definition:
		bleep = "*" * len(word)
		definition = definition.replace(word, bleep)
		print(definition)
		question(word, definition)
		print("===================")


