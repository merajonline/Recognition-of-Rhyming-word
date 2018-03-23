# Recognition-of-Rhyming-word
Natural Language Processing Project

Developed an algorithm for finding out different rhyming words of a given word with the help corresponding word pronunciation through CMU dictionary and phoneme set .
Implemented in python by using NLTK corpus package.

# About the CMU dictionary
The Carnegie Mellon University Pronouncing Dictionary is an open-source
machine-readable pronunciation dictionary for North American English that contains
over 134,000 words and their pronunciations. CMUdict is being actively maintained
and expanded. We are open to suggestions, corrections and other input.
Its entries are particularly useful for speech recognition and synthesis, as it has
mappings from words to their pronunciations in the ARPAbet phoneme set, a standard
for English pronunciation. The current phoneme set contains 39 phonemes; vowels
carry a lexical stress marker:
0    — No stress
1    — Primary stress
2    — Secondary stress
Bear in mind that this is a dictionary. If your word is not in it (or was misspelled)
nothing will be returned. This applies to items such as numbers. This tool will try to
come up with pronunciations for words not in the dictionary.


# Phoneme Set
The current phoneme set has 39 phonemes, not counting variation due to
lexical stress. This phoneme (or more accurately, phone) set is based on the
ARPAbet symbol set developed for speech recognition uses. You can find
a description of the ARPAbet on Wikipedia, as well information on how it
relates to the standard IPA symbol set.
Phoneme Example Translation
-- -- -- - -- -- -- - -- -- -- -- -- -
AA odd AA D

AE at AE T

AH hut HH AH T

AO ought AO T

AW cow K AW

AY hide HH AY D

B be B IY

CH cheese CH IY Z

D dee D IY

DH thee DH IY

EH Ed EH D

ER hurt HH ER T

EY ate EY T

F fee F IY


# About nltk.corpus Package
NLTK corpus readers. The modules in this package provide functions that can be
used to read corpus files in a variety of formats.These functions can be used to read
both the corpus files that are distributed in the NLTK corpus package, and corpus files
that are part of external corpora.
