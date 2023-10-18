import os
import string
import re
import nltk
from nltk import sent_tokenize

#nltk.download()

# load text
filename = 'metamorphosis_clean.txt'
filename = os.path.join( os.path.dirname( __file__ ), filename )
file = open(filename, 'rt')
text = file.read()
file.close()

# split into sentences
#sentences = sent_tokenize(text)
#print(sentences[0])

# split into words by white space
words = text.split()
#print(words[:100])

#print(string.punctuation)

# prepare regex for char filtering
re_punc = re.compile('[%s]' % re.escape(string.punctuation))
# remove punctuation from each word
stripped = [re_punc.sub('', w) for w in words]
#print(stripped[:100])

