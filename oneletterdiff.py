#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

with open('words.txt', 'r') as fd:
	while True:
		word = fd.readline()
		if not word:
			break
		word = word.strip()
		words[word] = None






