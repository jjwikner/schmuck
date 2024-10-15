#!/usr/bin/python3
import re, os, random, copy

def get_word_list():
    filename = 'five_words.html'
    # wget  http://meaningpedia.com/5-letter-words?show=all
    # save to file and massage
    pattern = re.compile(r'<span itemprop="name">(\w+)</span>')
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            the_text = ' '.join(f.readlines())
            word_list = pattern.findall(the_text)
            word_list = [word.lower() for word in word_list]
            return word_list
    return []

def check_yact(word="hello", yact='*****'):
    for n,c in enumerate(yact):
        if c=="*":
            continue
        if n > len(word)-1:
            continue
        if c == word[n]:
            return False
    return True

def check_xact(word="hello", xact='*****'):
    for n,c in enumerate(xact):
        if c=="*":
            continue
        if n > len(word)-1:
            continue
        if c != word[n]:
            return False
    return True

def check_does(word="hello", does='abcdefghijklmnopqrstuvwxyz'):
    for do in does:
        if not do in word:
            return False
    return True

def check_dont(word="hello", dont=''):
    for do in dont:
        if do in word:
            return False
    return True

def check_word(word="hello", does='abcdefghijklmnopqrstuvwxyz', dont='', xact='*****', yact='*****'):
    return check_does(word=word, does=does) and check_dont(word=word, dont=dont) and check_xact(word=word, xact=xact) and check_yact(word=word, yact=yact)

def shorten_list(word_list=[], does='abcdefghijklmnopqrstuvwxyz', dont='', xact='*****', yact='*****'):
    # This is just a reduction of the list of possible options.
    return [word for word in word_list if check_word(word, does=does, dont=dont, xact=xact, yact=yact)]

def find_likely_words(word_list=[]):
    # This will find the most likely words with respect to the most common letters left.
    # We can look at their frequency in general
    # Most common bigrams

    bigrams = ["th", "he", "in", "en", "nt", "re", "er", "an", "ti",
               "es", "on", "at", "se", "nd", "or", "ar", "al", "te",
               "co", "de", "to", "ra", "et", "ed", "it", "sa", "em", "ro"]
    BIG = len(bigrams)

    # This can be done once with the input words, instead
    # to generate the bigram weight list.
    weighted_words = []
    for word in word_list:
        s = 0
        for n,bigram in enumerate(bigrams):
            if bigram in word:
                s = s + BIG-n
        weighted_words.append([word, s])
    mm = sorted(weighted_words, key = lambda x:x[1], reverse=True)
    print(mm[0:(min([20, len(mm)]))])
    does = ''
    # Probably better to pick the words with the heighest weight somehow.
    # Use trigrams, bigrams and most common character
    
    words = copy.deepcopy([x[0] for x in mm[0:(min([110, len(mm)]))]])
    
    for m in range(5):
        stats = dict()
        for word in words:
            for char in word:
                if char in stats:
                    stats[char] = stats[char] + 1
                else:
                    stats[char] = 1

        for do in does:
            stats[do] = 0
        try:
            letter = max(zip(stats.values(), stats.keys()))[-1]
        except:
            letter = ''
        does = does + letter
        words = shorten_list(word_list=words, does=does)

    print(words)
    return words

def main():
    word_list = get_word_list()
    words = word_list
    print(len(words))
    # Can be refined further, by adding also where letters cannot be (orange). To do
    # Add stats on most common letters
    does = ''       # Orange
    dont = ''       # Black
    xact = '*****'  # Green
    yact = '*****'  #
    word = random.choice(find_likely_words(word_list=word_list))
    for run in range(8):
        print(f"Number of options: {len(words)}.")
        if len(words) == 1:
            print(f"The solution is {word.upper()}.")
            break
        else:
            print(f"Try with {word.upper()}.")
        xact_ = input('Placed letters,    eg., ***a*: ').rstrip().lower()
        yact_ = input('Misplaced letters, eg., ***b*: ').rstrip().lower() 
        # From here, derive the valid letters instead
        # to save some interaction and questions
        if xact_ == "":
            xact_ = "*****"
        if yact_ == "":
            yact_ = "*****"
        union_ = set([x for x in xact_] + [y for y in yact_])
        union_.remove("*")       
        lettuce = ''.join(union_)
        nonlett = ''
        trials = set([x.lower() for x in word])
        # Try difference function instead
        for lett in lettuce:
            if lett in trials:
                trials.remove(lett)
        dont_  = ''.join(list(trials))
        if len(dont_) > 0:
            print(f"Invalid letters: {dont_.upper()}.")
        does = does + lettuce # does_
        dont = dont + dont_
        xact = xact_
        yact = yact_
        words = shorten_list(word_list=words, does=does, dont=dont, xact=xact, yact=yact)
        word = random.choice(find_likely_words(word_list=words))

# ------
if __name__ == "__main__":
    main()
