from nltk.corpus import stopwords
stoplist = stopwords.words('english')
text = 'this is just a test'
cleanwordlist = [word for word in text.split() if word not in stoplist]
print(cleanwordlist)