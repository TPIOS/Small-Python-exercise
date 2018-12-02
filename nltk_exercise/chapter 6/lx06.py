import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import csv
import sklearn
import numpy as np
import collections
import sys, io
from optparse import OptionParser
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import tree
from sklearn.linear_model import SGDClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.cluster import KMeans, MiniBatchKMeans

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

op = OptionParser()
op.add_option("--lsa",
              dest="n_components", type="int",
              help="Preprocess documents with latent semantic analysis.")
op.add_option("--no-minibatch",
              action="store_false", dest="minibatch", default=True,
              help="Use ordinary k-means algorithm (in batch mode).")
op.add_option("--no-idf",
              action="store_false", dest="use_idf", default=True,
              help="Disable Inverse Document Frequency feature weighting.")
op.add_option("--use-hashing",
              action="store_true", default=False,
              help="Use a hashing feature vectorizer")
op.add_option("--n-features", type=int, default=10000,
              help="Maximum number of features (dimensions)"
                   " to extract from text.")
op.add_option("--verbose",
              action="store_true", dest="verbose", default=False,
              help="Print progress reports inside k-means algorithm.")

(opts, args) = op.parse_args()

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

trainset_size = int(round(len(sms_data)*0.70))
# print("The training set size for this classifier is", trainset_size, '\n')

x_train = np.array([''.join(el) for el in sms_data[0:trainset_size]])
x_test = np.array([''.join(el) for el in sms_data[trainset_size:]])
y_train = np.array([el for el in sms_labels[0:trainset_size]])
y_test = np.array([el for el in sms_labels[trainset_size:]])

# print(x_train)
# print(y_train)

vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1,2), stop_words='english', strip_accents='unicode', norm='l2')
X_train = vectorizer.fit_transform(x_train)
X_test = vectorizer.transform(x_test)

true_k = 5
km = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
kmini = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=1, init_size=1000, batch_size=1000, verbose=opts.verbose)
km_model = km.fit(X_train)
kmini_model = kmini.fit(X_train)
print('For K-mean clustering')
clustering = collections.defaultdict(list)
for idx, label in enumerate(km_model.labels_):
    clustering[label].append(idx)

print(clustering)

print('For K_means Mini batch clustering')
clustering = collections.defaultdict(list)
for idx, lable in enumerate(kmini_model.labels_):
    clustering[label].append(idx)

print(clustering)