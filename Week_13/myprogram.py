#!/usr/bin/python
# AUTHOR hari chhari@bu.edu
import sys
import collections
import numpy as np
import itertools
from itertools import *
from collections import Counter
import json


class TrieNode:
    def __init__(self, parent, value):
        self.parent = parent
        self.children = [None] * 26
        self.isWord = False
        if parent is not None:
            parent.children[ord(value) - 97] = self


def MakeTrie(dictfile):
    dict = open(dictfile)
    root = TrieNode(None, '')
    for word in dict:
        curNode = root
        for letter in word.lower():
            if 97 <= ord(letter) < 123:
                nextNode = curNode.children[ord(letter) - 97]
                if nextNode is None:
                    nextNode = TrieNode(curNode, letter)
                curNode = nextNode
        curNode.isWord = True
    return root

def BoggleWords(grid, dict, length_list, level, word_list, letter_bank, temp_sol_list, solns):
    
    rows = len(grid)
    cols = len(grid[0])
    queue = []
    grid2 = copy.deepcopy(grid)
    for y in range(cols):
        for x in range(rows):
            c = grid[y][x]
            if(c != '$'):
                node = dict.children[ord(c) - 97]
                if node is not None:
                    queue.append((x, y, c, node))
    while queue:
        x, y, s, node = queue[0]
        
        del queue[0]
        for dx, dy in ((1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)):
            x2, y2 = x + dx, y + dy
            if 0 <= x2 < cols and 0 <= y2 < rows:
                if(grid[y2][x2] != '$'):
                    s2 = s + grid[y2][x2]
                    grid2[y2][x2] = '$'
                    node2 = node.children[ord(grid[y2][x2]) - 97]
                    if node2 is not None:
                        if (node2.isWord) and len(s2) == length_list[level] and belongs(s2, letter_bank):
                            
                        queue.append((x2, y2, s2, node2))
                        print(queue)
    for word in word_list
        temp_sol_list[level] = word
        if(level+1 == len(length_list)):
            if(''.join(sorted(''.join(solns))) == letter_bank):
                solns.append(temp_sol_list)
        else:
            adj_grid = grid_adj(grid)

def belongs(word, fin_list):
    lens = Counter(fin_list)
    for i in word:
        lens[i] -= 1
        if lens[i] < 0:
            return False
    return True

def remove_unwanted(fin_list, a):
    x = []
    for i in a:
        if belongs(i, fin_list):
            x.append(i)
    return x

def main():
    d1 = MakeTrie('small_word_list.txt')
    d2 = MakeTrie('large_word_list.txt')
    x = input()
    while(x):
        words = []
        solns = []
        level = 0
        input_dict = json.JSONDecoder().decode(x)
        print(input_dict)
        temp_sol_list = ['']*len(input_dict['lengths'])
        grid = input_dict['grid']
        letter_bank = ''.join(sorted(''.join(grid)))
        BoggleWords(copy.deepcopy(grid), d2, input_dict['lengths'], level, words, letter_bank, temp_sol_list, solns)
        for i in soln:
            print(i)
        exit()
        x = input()
        
if __name__ == '__main__':
    main()
