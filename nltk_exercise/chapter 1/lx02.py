from urllib.request import urlopen
import re
import nltk
from bs4 import BeautifulSoup
import operator
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

response = urlopen('https://www.python.org')
html = response.read().decode('utf-8')
# print(len(html))
# tokens = [tok for tok in html.split()]
# print('Total no of tokens:', str(len(tokens)))
# print(tokens[:100])
# tokens = re.split('\W+', html)
# print(len(tokens))
# print(tokens[:100])
clean = BeautifulSoup(html, 'lxml').get_text()
tokens = [tok for tok in clean.split()]

# freq_dis = {}
# for tok in tokens:
#     if tok in freq_dis:
#         freq_dis[tok] += 1
#     else:
#         freq_dis[tok] = 1

freq_dist_nltk = nltk.FreqDist(tokens)
print(freq_dist_nltk)
for k, v in freq_dist_nltk.items():
    print(str(k),':',str(v))

# freq_dist_nltk.plot(50, cumulative=False)


# sorted_freq_dist = sorted(freq_dis.items(), key=operator.itemgetter(1), reverse=True)
# print(sorted_freq_dist[:25])