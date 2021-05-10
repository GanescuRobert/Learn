
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

exemple_sentence = "This is a sample sentence, showing off the stop words filtration."
stop_words = set(stopwords.words('english'))

print(stop_words)

words=word_tokenize(exemple_sentence)

filtered_sentence=[]
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)

