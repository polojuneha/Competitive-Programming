class Morse(object):
   def uniqueMorseCodeWords(self, words):
       MORSE = [".-","-...","-.-.","-..",".","..-.","--.",
                "....","..",".---","-.-",".-..","--","-.",
                "---",".--.","--.-",".-.","...","-","..-",
                "...-",".--","-..-","-.--","--.."]

       k = {"".join(MORSE[ord(c) - ord('a')] for c in word)
               for word in words}

       return len(k)
l=["a", "z", "g", "m"]
m = ["gin", "zen", "gig", "msg"]
n = ["bhi", "vsv", "sgh", "vbi"]
h = ["a", "b", "c", "d"]
f = ["hig", "sip", "pot"]
x=Morse()
print(x.uniqueMorseCodeWords(l))
print(x.uniqueMorseCodeWords(m))
print(x.uniqueMorseCodeWords(n))
print(x.uniqueMorseCodeWords(h))
print(x.uniqueMorseCodeWords(f))


