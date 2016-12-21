# AUTHOR Abhishek Shanbhag anshan@bu.edu
# AUTHOR hari chhari@bu.edu
# AUTHOR ameya apastamb ameyama@bu.edu
# AUTHOR Shreyas joshi svmjoshi@bu.edu
import sys
from itertools import combinations
x = sys.argv


def cl(ip):
    l = [0]*26
    for i in ip:
        l[ord(i)-97] += 1
    return l


def bel(ip, l):
    for i in ip:
        l[ord(i) - 97] -= 1
        if(l[ord(i) - 97] < 0):
            return False
    return True


if (len(x) == 2):
    f = open(x[1])
    ls = f.read()
    l = ls.split()
    s_dt = {}
    lnt = [len(w) for w in l]
    for i in lnt:
        if not(i in s_dt):
            s_dt.update({i: {}})
    for w in l:
        ln = len(w)
        k = ''.join(sorted(w))
        if k in s_dt[ln]:
            s_dt[ln][k].append(w)
            s_dt[ln][k] = sorted(s_dt[ln][k])
        else:
            s_dt[ln].update({k: [w]})
    while(1):
        ip = (input()).split(' ')
        iw = ''.join(sorted(ip[0]))
        k = int(ip[1])
        if(not(k)):
            break
        w_l = []
        if(k < 9):
            clist = set(combinations(iw, k))
            cos = [''.join(c) for c in clist]
            for c in cos:
                if(c in s_dt[k]):
                    w_l.extend(s_dt[k][c])
        else:
            l = cl(ip[0])
            for w in s_dt[k]:
                if(bel(w, l.copy())):
                    w_l.extend(s_dt[k][w])
        for w in sorted(w_l):
            print(w)
        print('.')