s = "Hi Everyone !    hola gr8"
print(s.split())

from nltk.tokenize import word_tokenize
print(word_tokenize(s))

from nltk.tokenize import regexp_tokenize, wordpunct_tokenize, blankline_tokenize
print(regexp_tokenize(s, pattern='\w+'))
print(regexp_tokenize(s, pattern='\d+'))
print(wordpunct_tokenize(s))
print(blankline_tokenize(s))

