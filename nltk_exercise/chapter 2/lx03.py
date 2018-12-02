from nltk.stem import PorterStemmer
from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer

# pst = PorterStemmer()
# lst = LancasterStemmer()

# print(lst.stem("eating"))
# print(pst.stem("shopping"))

wlem = WordNetLemmatizer()
print(wlem.lemmatize('ate', pos='v'))