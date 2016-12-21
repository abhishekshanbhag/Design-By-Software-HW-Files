# AUTHOR G Siva Perumal siva@bu.edu
# AUTHOR Sivaramakrishnan sankarapandian sivark@bu.edu
# AUTHOR Anand Shivalkar anshival@bu.edu

from collections import Counter
from math import factorial
from itertools import permutations
import sys

lis4 = []
result = []
words_dict = {}
with open(sys.argv[1]) as f:
    for line in f:
        for word in line.split():
            if len(word) not in words_dict:
                words_dict[len(word)] = []
        words_dict[len(word)].append(word)
while True:
    string, number = input().split()
    no_of_perm = (factorial(len(string)) / factorial(len(string)-int(number)))
    if(string != 'exit'):
        lis1 = words_dict[int(number)]
        if(no_of_perm > 3000000000):
            for words in lis1:
                nl = 0
                o = 0
                lis3 = list(string)
                cis = Counter(lis3)
                lis2 = list(words)
                for o in range(0, int(number)):
                    c = lis2[o]
                    if c in cis:
                        if(cis[c] > 0):
                            cis[c] -= 1
                            nl = nl + 1
                        else:
                            break
                    else:
                        break
                if(nl == int(number)):
                    result.append(words)
            for words in sorted(result):
                print(words)
            print(".")
            result = []
        else:
            perms = set([''.join(p) for p in
                        permutations(string, int(number))])
            lis4 = list(set(lis1).intersection(perms))
            for words in sorted(lis4):
                print(words)
            print(".")
    else:
        sys.exit()
