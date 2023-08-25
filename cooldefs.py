import random
import time
import sys

import dictionaryapi
import colorprint

# min and max delay in millisecond
def random_delay(mindelay, maxdelay):
    delay = random.randint(0, (maxdelay-mindelay)) + mindelay
    time.sleep(delay/1000)


def animate_def(word, defi):
    colorprint.cprint(word, colorprint.RED)
    random_delay(500, 1000)
    count = 0
    for w in defi:
        sys.stdout.write(f"{w}")
        sys.stdout.flush()
        random_delay(50, 300)
        count += 1
        if count%80 == 0:
            print("")
    print("\n\n")
        
    
def start_display(words):
   random.shuffle(words)
   for word in words:
        if len(word) > 5:
            definition = dictionaryapi.get_definition(word)
            if not definition:
                continue
            animate_def(word, definition)



def load_words():
    words = []
    with open('words.txt', 'r') as fd:
        while True:
            word = fd.readline()
            if not word:
                break
            word = word.strip()
            words.append(word)
    return words

w = load_words()
start_display(w)
