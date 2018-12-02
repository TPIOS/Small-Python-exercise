import sys
import nltk
f = open('nyt.txt','r')
news_content = f.read()
results = []
for sent_no, sentence in enumerate(nltk.sent_tokenize(news_content)):
    no_of_tokens = len(nltk.word_tokenize(sentence))
    print(no_of_tokens)
    tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
    no_of_nouns = len([word for word,pos in tagged if pos in ["NN", "NNP"]])
    ners = nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sentence)), binary=False)
    no_of_ners = len([chunk for chunk in ners if hasattr(chunk, 'label')])
    score = (no_of_ners + no_of_nouns) / no_of_tokens
    
    results.append((sent_no, no_of_tokens, no_of_ners, no_of_nouns, score, sentence))

for sent in sorted(results, key=lambda x : x[4], reverse=True):
    print(sent[5])
