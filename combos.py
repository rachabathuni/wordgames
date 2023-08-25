#!/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

import random
import sys

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

class WordMetrics:
    def __init__(self, word):
        self.word = word
        self.index = self._get_index(word)
        self.counts = self._get_counts(word)

    def _get_index(self, word):
        idx = 0
        for x in range(0, 26):
            c = chr(x + 97)
            if c in word:
                idx = idx | 0x01
            if x != 25:
                idx = idx << 1
        return idx

    def _get_counts(self, word):
        counts = [0 for i in range(0,26)]
        for c in word:
            x = ord(c) - 97
            if x < 0 or x > 25:
                continue
            counts[x] += 1
        return counts

    def _letters_subset_of(self, word_metrics):
        xor = self.index ^ word_metrics.index
        anded = xor & self.index
        return anded == 0

    def is_contained_in(self, word_metrics):
        if not self._letters_subset_of(word_metrics):
            return False

        for i in range(0, 26):
            if self.counts[i] > word_metrics.counts[i]:
                return False
        return True

    def contains_letter(self, s):
        val = ord(s[0]) - 97
        mask = 0x02000000 >> val
        return self.index & mask != 0


def get_word_by_len(wbl, len_array):
    index = random.randint(0, len(len_array)-1)
    word_list = wbl[len_array[index]]
    word_idx = random.randint(0, len(word_list)-1)
    return word_list[word_idx]

def get_color_string(string, color):
    return color + string + bcolors.ENDC


def print_error(msg):
    print(get_color_string(msg, bcolors.FAIL))

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

def preprocess_words(words):
    words_by_len = [[] for x in range(0, 60)]
    metrics = {}
    for w in words:
        if len(w) < 3:
            continue
        m = WordMetrics(w)
        words_by_len[len(w)].append(m)
        metrics[w] = m
    return metrics, words_by_len


def get_total_subwords(word, wbl):
    total = 0
    for wlist in wbl[3:len(word.word)+1]:
        for wm in wlist:
            if wm.is_contained_in(word):
                print(f"{wm.word}/{word.word}")
                total += 1
    return total

def play(metrics, wbl, word_lens):
    word = get_word_by_len(wbl, word_lens)
    total = get_total_subwords(word, wbl)
    print(f"WORD: {word.word} ({total})")
    guess = input("")
    gm = WordMetrics(guess)


def main():
    word_lens = [6, 7, 8, 9, 10]
    if len(sys.argv) > 1:
	    word_lens = []
	    for arg in sys.argv[1:]:
		    word_lens.append(int(arg))
    
    words = load_words()
    metrics, wbl = preprocess_words(words)

    while True:
        play(metrics, wbl, word_lens)
    

if __name__ == '__main__':
    main()


