#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import random
import sys
import requests


DICT_BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def get_definition(word):
    url = DICT_BASE_URL + word
    r = requests.get(url)
    if r.status_code != 200:
        print(f"Failed to get definition for word {word}")
        return None

    body = r.json()
    if len(body) > 0 and 'meanings' in body[0] and len(body[0]['meanings'])>0 and \
    'definitions' in body[0]['meanings'][0] and len(body[0]['meanings'][0]['definitions'])>0 and \
    'definition' in body[0]['meanings'][0]['definitions'][0]:
        return body[0]['meanings'][0]['definitions'][0]['definition']
    else:
        print(f"Definition not found for {word}")
        return None


def jumble(word):
    letters = list(word)
    random.shuffle(letters)
    return "".join(letters)


def get_word_by_len(len_array):
    while True:
        index = random.randint(0, len(words))
        word = words[index]
        if len(word) in len_array:
            return word


def get_caps(word):
    caps = ""
    for c in word.upper():
        caps += c
        caps += " "

    return caps


# Default is 5 or 6 letter words
word_lens = [5, 6]
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
    print("==================================================================================\n")
    word = get_word_by_len(word_lens)
    scrambled = jumble(word)
    caps = get_caps(scrambled)

    while True:
        print(f"{caps}\n")
        guess = input("What's the word: ")
        if guess == ".h":
            definition = get_definition(word)
            print(definition)
        else:
            break

    if guess == word:
        print("✅ Correct")
    else:
        word_caps = get_caps(word)
        if len(guess) == len(word) and guess in words:
            g = sorted(guess)
            w = sorted(word)
            for i in range(0, len(g)):
                if g[i] != w[i]:
                    break
            else:
                print(f"🎖️ The word was {word_caps} but this works too")
                continue

        print(f"❌ Wrong: {word_caps}")
        print(f"https://www.dictionary.com/browse/{word}")



