from collections import Counter
import sys
import time

with open('wordList.txt', 'r') as f:
    dictionary = f.read()
    dictionary = [x.lower() for  x in dictionary.split('\n')]
    print(len(dictionary))


