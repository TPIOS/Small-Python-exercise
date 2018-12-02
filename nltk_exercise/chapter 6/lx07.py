import warnings
warnings.filterwarnings(action='ignore',category=UserWarning,module='gensim')
import gensim
from gensim import corpora, models, similarities
from itertools import chain
import nltk
from operator import itemgetter
import re
import sys, io, csv
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')


def preprocessing(text):
    # text = text.decode('utf8')
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    stop = stopwords.words('english')
    tokens = [token for token in tokens if token not in stop]
    tokens = [word for word in tokens if len(word) >= 3]
    tokens = [word.lower() for word in tokens]
    lmtzr = WordNetLemmatizer()
    tokens = [lmtzr.lemmatize(word) for word in tokens]
    preprocessed_text = " ".join(tokens)
    return preprocessed_text

smsdata = open('SMSSpamCollection', encoding='utf-8')
sms_data = []
sms_labels = []
csv_reader = csv.reader(smsdata, delimiter = '\t')
for line in csv_reader:
    sms_labels.append(line[0])
    sms_data.append(preprocessing(line[1]))

smsdata.close()

documents = [document for document in sms_data]
stoplist = stopwords.words('english')
texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]

si = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100)
si.print_topic(20)
n_topics = 5
lda = models.LdaModel(corpus_tfidf, id2word=dictionary, num_topics=n_topics)

for i in range(0, n_topics):
    temp = lda.show_topic(i, 10)
    # print(temp)
    terms = []
    for term in temp:
        terms.append(term[0])
    print('Top 10 terms for topic #'+str(i)+":", ",".join(terms))
