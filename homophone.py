import string

def read_dictionary(filename='c06d'):
    """read (filename) and build a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def make_word_list():
    """read the words in words.txt and return a dictionary
    that contains the words as keys"""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = word

    return d

def is_onesyll(word):
	flag = True
	for letter in word:
		if letter == ' ':
			flag = False
			return flag
		else:
			flag = True
	return flag
print is_onesyll("give me")
d = dict()
d = read_dictionary()
wordlist = dict()
wordlist = make_word_list()
for w in wordlist:
	if (len(w) == 5): 
		word1 = w[1:]
		word2 = w[0] + w[2:]
                if d.has_key(word1) and d.has_key(word2) and d.has_key(w):
			if d[word1] == d[w] and d[word2] == d[w]:
				print w
print "cant beleive program ended without the statement recursion depth exceeded"
