#! /usr/bin/python2.7

def signature(s):
    t = list(s)
    t.sort()
    t = ''.join(t)
    return t

def all_anagrams(filename):
    d = {}
    for line in open(filename):
        word = line.strip().lower()
        t = signature(word)
        if t not in d:
            d[t] = [word]
        else:
            d[t].append(word)
            
    return d

def list_anagrams(d):
    l = d.values()
    l.sort()
    print l

def for_scrabble(d):
    l = d.values()
    ctr = []
    for w in l:
        if len(w[0]) == 8:
            ctr.append(len(w))
    maximum = max(ctr)
    for w in l:
        if len(w[0]) == 8 and len(w) == maximum:
            print w

def count(s1,s2):
    ctr = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            ctr += 1
    if ctr == 2:
        return True
    return False        

def compare(words):
    s = []
    for s1 in words:
        for s2 in words:
            if count(s1,s2):
                if [s2,s1] not in s:
                    s.append([s1,s2])
    if len(s) > 1:
        print s            
    
def meta_pair(d):
    l = d.values()
    for words in l:
        if len(words) > 1:
            compare(words)
d = all_anagrams('words.txt')
#list_anagrams(d)
#for_scrabble(d)
meta_pair(d)
