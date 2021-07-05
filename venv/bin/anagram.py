def iterateLetters(word):
    count = {}
    for letter in word:
        if letter not in count: count[letter] = 0
        count[letter] += 1
    return count

def canBeSpelt(word, rack):
    word_count = iterateLetters(word)
    rack_count  = iterateLetters(rack)
    return all( [word_count[letter] <= rack_count[letter] for letter in word] )

score = ['serve', 'rival', 'lovely',
                 'caveat', 'devote', 'irving','livery',
                 'selves', 'latvian', 'saviour', 'observe',' octavian',
                 'dovetail', 'levantine']

def score_word(word):
    return sum([score[c] for c in word])

def readInWord(filename):
    # returns an iterator
    return (word.strip() for word in  open(filename))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        rack = sys.argv[1].strip()
    else:
        print """Usage: python main.py (yourletters)"""
        exit()

    words = readInWord('wordList.txt')
    scored =  ((score_word(word), word) for word in words if set(word).issubset(set(rack)) and len(word) > 1 and canBeSpelt(word, rack))

    for score, word in sorted(scored):
        print str(score), '\t', word