#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import random
import sys

N_MAX_ATTEMPTS = 6

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def get_word_by_len(len_array):
	while True:
		index = random.randint(0, len(words))
		word = words[index]
		if len(word) in len_array:
			return word


def get_color_string(string, color):
	return color + string + bcolors.ENDC


def get_printable_attempt(attempt, word):
	output = ""
	for i in range(0, len(attempt)):
		if attempt[i] == word[i]:
			output = output + get_color_string(attempt[i], bcolors.OKGREEN) + " "
		elif attempt[i] in word:
			output = output + get_color_string(attempt[i], bcolors.WARNING) + " "
		else:
			output = output + "_" + " "

	return output


def print_blank(word):
	blank = ""
	for i in range(0, len(word)):
		blank = blank + get_color_string("_ ", bcolors.OKBLUE)
	print(blank)

def print_eliminated(attempts, word):
	elim = ""
	avail = ""
	for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		for attempt in attempts:
			if c in attempt and c not in word:
				elim += c + " "
				break
		else:
			avail += c + " "
			
	if elim:
		print(f"Eliminated: {elim}")
	if avail:
		print(f"Available: {avail}")


def print_table(attempts, word):
	for attempt in attempts:
		print(get_printable_attempt(attempt, word))

def print_error(msg):
	print(get_color_string(msg, bcolors.FAIL))


def play():
	attempts = []
	print("==================================================================================\n")
	word = get_word_by_len(word_lens)
	word = word.upper()
	while True:
		print_blank(word)
		print_eliminated(attempts, word)

		try:
			guess = input("Your guess: ")
		except:
			print(f"\nWord is: {word}")
			sys.exit(0)

		if guess not in words:
			print_error("Not a word I know")
			print_table(attempts, word)
			continue

		guess = guess.upper()

		if len(guess) != len(word):
			print(get_color_string("Word length didn't match", bcolors.WARNING))
			continue

		attempts.append(guess)
		print_table(attempts, word)
		if guess == word:
			return
		elif len(attempts) == N_MAX_ATTEMPTS:
			print_error("No more attempts")
			print(f"Word is: {word}")
			return

# Default is 5 letter words
word_lens = [5]
if len(sys.argv) > 1:
	word_lens = []
	for arg in sys.argv[1:]:
		word_lens.append(int(arg))


words = []
with open('words.txt', 'r') as fd:
	while True:
		word = fd.readline()
		if not word:
			break
		word = word.strip()
		words.append(word)

while True:
	play()
