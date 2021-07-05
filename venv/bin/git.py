def main():
    f = open('wordList.txt', 'r')
    wordlist = f.readlines()
    final = []
    for i in wordlist:
        stripped = i.strip()
        final.append(stripped)
        final.sort(key=len)
    f.close()

    anagramList = [
        'serve',
        'rival',
        'lovely',
        'caveat',
        'devote',
        'irving',
        'livery',
        'selves',
        'latvian',
        'saviour',
        'observe',
        ' octavian',
        'dovetail',
        'levantine'
    ]

    word1 = ''
    for j in anagramList:
        for k in final:
            if checkLength(j) == checkLength(k):
                word = list(k)
                if tori(j, word):
                    print(k)


def checkLength(j):
    length = len(j)
    return length


def tori(j, word):
    for v in j:
        if v not in word:
            return False
        else:
            word.remove(v)
    return True


main()
