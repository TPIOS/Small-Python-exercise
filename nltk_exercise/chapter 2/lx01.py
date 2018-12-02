inputstring = " This is an example sent. The sentence splitter will split on sent markers. Ohh really !!"
from nltk.tokenize import sent_tokenize
import nltk.tokenize.punkt
tokenizer = nltk.tokenize.punkt.PunktSentenceTokenizer()
all_sent = sent_tokenize(inputstring)
print(all_sent)