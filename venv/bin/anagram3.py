from collections import Counter
import sys
import time

with open('wordList.txt', 'r') as f:
    dictionary = f.read()
    dictionary = [x.lower() for  x in dictionary.split('\n')]
    print(len(dictionary))


def return_anagrams(letters : str) ->:
    letters = letters.lower()
    anagrams = set()
    for word in dictionary:
        if not set(word) - set(letters)
        