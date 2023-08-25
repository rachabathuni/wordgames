#!/usr/bin/python3

from collections import defaultdict


def default_value():
	return 0


def count_letters(top, word):
	total = 0
	letters = {}
	for letter in word:
		letters[letter] = None

	for letter in letters.keys():
		if letter in top:
			total += 1

	return total

letters = defaultdict(default_value)

five_letter_words = []

with open('words.txt', 'r') as fd:
	while True:
		word = fd.readline()
		if not word:
			break
		word = word.strip()
		if len(word) == 5:
			five_letter_words.append(word)


top = "esarolitnducpmy"

for i in range(len(five_letter_words)):
	if count_letters(top, five_letter_words[i]) < 3:
		continue
	print("Word 1: %s" % five_letter_words[i])

	for j in range(len(five_letter_words)):
		if i == j:
			continue

		if count_letters(top, five_letter_words[i] + five_letter_words[j]) < 8:
			continue

		print("Word 1: %s, Word 2: %s" % (five_letter_words[i], five_letter_words[j]))

		for k in range(len(five_letter_words)):
			if k == i or k == j:
				continue
			total = count_letters(top, five_letter_words[i] + five_letter_words[2] + five_letter_words[k])
			if total > 11:
				print("%d: %s, %s, %s" % (total, five_letter_words[i], five_letter_words[j], five_letter_words[k]))
