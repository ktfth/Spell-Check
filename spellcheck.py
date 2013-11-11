import re, collections, sys
from misspell import Misspell
# re - Python Library for Regular Expressions
# collections - Python Library for High Performance Container Datatypes

# Spell Check program using algorithm originally
# summarized by Dr. Peter Norvig.
# 	src: http://norvig.com/spell-correct.html
# 	additional src: http://goo.gl/uaJ6DQ (Google)

# The algorithm used has 3 parts:
# 	-The probability of the typed word being correctly typed by the user
# 	-The offset probability of the user typing word, x, but initially meant word, y
# 	-Iteration of all possible outputs, and choosing a word which has the best probability


# Returning the words in a list as lower case and defining a word as a list of alphabetic character
# Works because the singular version of a word is more probably than the possessive notation (dog, dog's)
def words(text): 
	return re.findall('[a-z]+', text.lower()) 

#Returning dictionary = {'a':{abbey:1, abbreviated:2}, 'b':{},...,'z':{}}
#Instead of iterating through the whole dictionary, iteration happens based on first letter
def train(words):
	occurences = {}
	for l in alphabet:
		occurences[l] = collections.defaultdict(lambda: 1) #Sets default values in a dictionary, less iteration to check if element is a part of the dictionary
	for w in words:
		occurences[w[0]][w] += 1 #Incrementing occurence of word
	return occurences

#Edits can be deletion (deletes), swapping adajent letters (transposes), alteration (replaces), or inserting a letter (inserts)
#Returns a set of of all words one edit away from correct word
def edits1(word):
	splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
	deletes = [a + b[1:] for a, b in splits if b]
	transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
	replaces = [a + c + b[1:] for a, b in splits for c in alphabet if b]
	inserts = [a + c + b     for a, b in splits for c in alphabet]
	return set(deletes + transposes + replaces + inserts)

#Returns a set of words with the possible edits
def known_edits2(word, wDict):
	return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in wDict)

#A known word is most likely to be a word that has a vowel mistyped rather than 2 consonants, probable correct first letter, edit distances of around 1 or 2
def known(word, wDict): 
	return set(w for w in word if w in wDict)

# Highest Level Method
# Returns the possible word
def correct(word, wDict):
	candidates = known([word], wDict[word[0]]) or known(edits1(word), wDict[word[0]]) or known_edits2(word, wDict[word[0]]) or [word] # gets a set of words with the shortest edit distance from the typed word.
	return max(candidates, key=wDict.get) # returning the element of the set with the highest probability of being the correct word

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def main():
	lWords = words(file('/usr/share/dict/words').read())
	try:
		if sys.argv[1] == '0':
			lWords = train(lWords)
			while True:
				word = raw_input('>')
				if not word.isalpha():
					continue
				spellchk = correct(word.lower(), lWords)
				if spellchk == word and spellchk not in lWords[word[0]]:
					print 'NO SUGGESTION'
				else:
					print spellchk
				print #'\n'
		elif sys.argv[1] == '1':
			misspell = Misspell(lWords)
			lWords = train(lWords)
			while True:
				word = misspell.genWord()
				print 'Incorrect -', word
				spellchk = correct(word, lWords)
				if spellchk == word and spellchk not in lWords[word[0]]:
					print 'NO SUGGESTION'
				else:
					print 'Correct   -',spellchk
				print #'\n'
				newWord = raw_input('<enter>\n') #Enter to continue
	except KeyboardInterrupt: 
		#Cleaner way to exit program without a crash
		'exit'
	except EOFError:
		'exit'

if __name__ == "__main__":
	main()