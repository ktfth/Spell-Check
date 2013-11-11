Spell-Check
===========

Spell Checker in Python

Algorithm
---------
Spell Check program using algorithm originally
summarized by Dr. Peter Norvig.
	src: <a href="http://norvig.com/spell-correct.html">How to Write a Spelling Corrector</a>
	additional src: <a href="http://goo.gl/uaJ6DQ">Google Algorithm Paper</a>

The algorithm used has 3 parts:
	+ The probability of the typed word being correctly typed by the user
	+ The offset probability of the user typing word, x, but initially meant word, y
	+ Iteration of all possible outputs, and choosing a word which has the best probability


Main Challenge
--------------

Write a program that reads a large list of English words (e.g. from /usr/share/dict/words on a unix system) into memory, and then reads words from stdin, and prints either the best spelling suggestion, or "NO SUGGESTION" if no suggestion can be found. The program should print ">" as a prompt before reading each word, and should loop until killed.

Your solution should be faster than O(n) per word checked, where n is the length of the dictionary. That is to say, you can't scan the dictionary every time you want to spellcheck a word.

For example:

<pre><code>> sheeeeep

sheep

> peepple

people

> sheeple

NO SUGGESTION</code></pre>


The class of spelling mistakes to be corrected is as follows:

+ Case (upper/lower) errors: "inSIDE" => "inside"
+ Repeated letters: "jjoobbb" => "job"
+ Incorrect vowels: "weke" => "wake"
Any combination of the above types of error in a single word should be corrected (e.g. "CUNsperrICY" => "conspiracy").

If there are many possible corrections of an input word, your program can choose one in any way you like. It just has to be an English word that is a spelling correction of the input by the above rules.

Final step: Write a second program that *generates* words with spelling mistakes of the above form, starting with correctly spelled English words. Pipe its output into the first program and verify that there are no occurrences of "NO SUGGESTION" in the output.

Algorithm Source
----------------
Peter Norvig - <a href="http://norvig.com/spell-correct.html">How to Write a Spelling Corrector</a>
