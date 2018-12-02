import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
results = []
news_content = "Mr. Obama planned to promote the effort on Monday during a visit to Camden, N.J. The ban is part of Mr. Obama's push to ease tensions between law enforcement and minority \communities in reaction to the crises in Baltimore; Ferguson, Mo. We are, without a doubt, sitting at a defining moment in American policing, Ronald L. Davis, the director of the Office of Community Oriented Policing Services at the Department of Justice, told reporters in a conference call organized by the White House"
sentences = nltk.sent_tokenize(news_content)
vectorizer = TfidfVectorizer(norm='l2', min_df = 0, use_idf=True, smooth_idf=False, sublinear_tf=True)
sklearn_binary = vectorizer.fit_transform(sentences)
print(vectorizer.get_feature_names())
print(sklearn_binary.toarray())
for i in sklearn_binary.toarray():
    results.append(i.sum()/len(i.nonzero()[0]))
