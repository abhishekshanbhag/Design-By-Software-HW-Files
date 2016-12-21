#!/usr/bin/python
# AUTHOR Abhishek Shanbhag anshan@bu.edu
# AUTHOR hari chhari@bu.edu
# AUTHOR ameya apastamb ameyama@bu.edu
# AUTHOR Shreyas joshi svmjoshi@bu.edu
import sys
import collections
import numpy as np
import itertools
from itertools import *
import json
from copy import deepcopy as dc


class TrieNode:
    def __init__(self, pt, val):
        self.pt = pt
        self.ch = [None] * 26
        self.isWord = False
        if pt is not None:
            pt.ch[ord(val) - 97] = self


def MakeTrie(dictfile):
    dict = open(dictfile)
    root = TrieNode(None, '')
    for word in dict:
        curNode = root
        for letter in word.lower():
            if 97 <= ord(letter) < 123:
                nextNode = curNode.ch[ord(letter) - 97]
                if nextNode is None:
                    nextNode = TrieNode(curNode, letter)
                curNode = nextNode
        curNode.isWord = True
    return root


class BN:
    def __init__(self, pt, val, cv, grd_s, loc, pth, lv):
        self.pt = pt
        self.ch = [[None]] * 26
        self.isWord = False
        self.cv = cv + val
        self.grd_s = grd_s
        self.loc = loc
        self.pth = pth
        self.pth.append(loc)
        self.lv = lv
        if pt is not None:
            if(len(pt.ch[ord(val) - 97])):
                pt.ch[ord(val) - 97].append([self])
            else:
                pt.ch[ord(val) - 97][0] = self


def is_a_word(word, d):
    curr_node = d
    for i in word:
        next_node = curr_node.ch[ord(i) - 97]
        if next_node is None:
            return False
        else:
            curr_node = next_node
    if(curr_node.isWord):
        return True
    return False


def word_not_in_list(w, w_l):
    for i in w_l:
        if(w == i[0]):
            return False
    return True


def MakeBogTrie(root, w_l, d):
    if(root.lv != 0):
        cl = len(root.grd_s)
        rw = len(root.grd_s)
        combs = [(1, 0), (1, -1), (0, -1), (-1, -1)]
        combs_ext = [(-1, 0), (-1, 1), (0, 1), (1, 1)]
        combs.extend(combs_ext)
        for dx, dy in combs:
            nx, ny = root.loc[0] + dx, root.loc[1] + dy
            if 0 <= nx < cl and 0 <= ny < rw:
                nlet = root.grd_s[nx][ny]
                if(nlet != '$'):
                    ncv = root.cv
                    ngrd_s = dc(root.grd_s)
                    ngrd_s[root.loc[0]][root.loc[1]] = '$'
                    nloc = [nx, ny]
                    npth = dc(root.pth)
                    nlv = root.lv - 1
                    nnd = BN(root, nlet, ncv, ngrd_s, nloc, npth, nlv)
                    MakeBogTrie(nnd, w_l, d)
    else:
        w = root.cv
        if is_a_word(w, d):
            if(word_not_in_list(w, w_l)):
                # print(w + ' is a word')
                w_l.append([w, root.pth])


def clean_and_push_grid(grd, pth):
    for x, y in pth:
        grd[x][y] = '$'
    for i in range(len(grd)):
        for j in range(len(grd)-1, -1, -1):
            if(grd[i][j] != '$'):
                c = j
                while(c+1 < len(grd) and grd[i][c+1] == '$'):
                    grd[i][c+1] = grd[i][c]
                    grd[i][c] = '$'
                    c += 1
    return grd


def not_in_sol(tsol, sol):
    for s in sol:
        if(''.join(sorted(''.join(s))) == ''.join(sorted(''.join(tsol))))
            return False
    return True


def solve_bog(grd_s, w_lns, sol, tsol, tpl, w_tr, lv):
    jsol = ''.join(tsol)
    if(len(jsol) == len(grd_s)*len(grd_s)):
        if((''.join(sorted(jsol)) == tpl) and not_in_sol(tsol, sol)):
            sol.append(dc(tsol))
            # print('Added ' + str(tsol) + ' to solns')
            # input()
    else:
        # print('Entering level ' + str(lv))
        # print('Looking for ' + str(w_lns[lv]) + ' letter word')
        if len(tsol) <= lv:
            tsol.append('')
        for i in range(len(grd_s)):
            for j in range(len(grd_s)):
                lt = grd_s[i][j]
                if(lt != '$'):
                    r = BN(None, lt, '', dc(grd_s), [i, j], [], w_lns[lv] - 1)
                    w_l = []
                    MakeBogTrie(r, w_l, w_tr)
                    # print(word_list)
                    for w in w_l:
                        tsol[lv] = w[0]
                        ngrd = clean_and_push_grid(dc(grd_s), w[1])
                        solve_bog(ngrd, w_lns, sol, dc(tsol), tpl, w_tr, lv+1)


def alternate_soln():
    pass


def write_to_file(sol):
    for i in sol:
        s = ''
        for word in sorted(i):
            s += word + ' '
        print(s[:len(s) - 1])
    print('.')


def main():
    d_s = MakeTrie(sys.argv[1])
    d_l = MakeTrie(sys.argv[2])
    x = input()
    while(x):
        ipd = json.JSONDecoder().decode(x)
        k = ipd['grid']
        lbk = ''.join(sorted(''.join(k)))
        grd_s = []
        for i in range(len(k)):
            grd_s.append([])
            for j in k[i]:
                grd_s[i].append(j)
        w_lns = ipd['lengths']
        sol = []
        size = ipd['size']
        if(size <= 5):
            solve_bog(dc(grd_s), dc(w_lns), sol, [], lbk, d_s, 0)
            if not len(sol):
                solve_bog(dc(grd_s), dc(w_lns), sol, [], lbk, d_l, 0)
        else:
            alternate_soln()
        write_to_file(sol)
        x = input()
if __name__ == '__main__':
    main()
