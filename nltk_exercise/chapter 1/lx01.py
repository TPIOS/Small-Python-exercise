import re
mystring = "Monty Python ! And the holy Grail ! \n"
# print(mystring.split())
# print(mystring.strip())
# print(mystring.upper())
# print(mystring.replace('!',''''''))

# if re.search('Python', mystring):
#     print("We found Python")
# else:
#     print("No")

# print(re.findall('!',mystring))
word_freq = {}
for tok in mystring.split():
    if tok in word_freq:
        word_freq[tok] += 1
    else:
        word_freq[tok] = 1

print(word_freq)