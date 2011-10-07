letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z']
def rotate_word(word,n):
        l = ""
        for letter in word:
                rot = ord(letter) + n
                if rot > ord('z'):
                        rot = rot % ord('a') - 27
                       
                elif rot < ord('a'):
                        rot = rot % ord('a') - 97
                       
                else:
                        rot = rot % ord('a')
 
 
                #print rot
                l = l + letters[(+rot)%26]
                rot = 0
        return l
#print letters[ord('m') % 97]
print rotate_word("ceaser",13)
