import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import csv
import sklearn
import numpy as np
import sys, io
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn import tree

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

trainset_size = int(round(len(sms_data)*0.70))
print("The training set size for this classifier is", trainset_size, '\n')

x_train = np.array([''.join(el) for el in sms_data[0:trainset_size]])
x_test = np.array([''.join(el) for el in sms_data[trainset_size:]])
y_train = np.array([el for el in sms_labels[0:trainset_size]])
y_test = np.array([el for el in sms_labels[trainset_size:]])

print(x_train)
print(y_train)

vectorizer = TfidfVectorizer(min_df=2, ngram_range=(1,2), stop_words='english', strip_accents='unicode', norm='l2')
X_train = vectorizer.fit_transform(x_train)
X_test = vectorizer.transform(x_test)

clf = tree.DecisionTreeClassifier().fit(X_train.toarray(), y_train)
y_tree_predicted = clf.predict(X_test.toarray())
print(y_tree_predicted)
print('\n Here is the classification report:')
print(classification_report(y_test, y_tree_predicted))
