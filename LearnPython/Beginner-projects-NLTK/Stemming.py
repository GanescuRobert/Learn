
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize as wt

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned","pythonly"]

for w in example_words:
    print(ps.stem(w))
    
exemple_sentence = "It is important to be very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = wt(exemple_sentence)

for w in words:
    print(ps.stem(w))

