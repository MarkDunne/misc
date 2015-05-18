import codecs
from textblob import TextBlob

uniText = codecs.open('nyt.txt').read()
blob = TextBlob(uniText)

print 'hi'
print blob