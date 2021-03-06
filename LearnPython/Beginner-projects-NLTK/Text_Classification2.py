import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from nltk.tokenize import word_tokenize
#print(type(movie_reviews))

from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC

from nltk.classify import ClassifierI
from statistics import mode

from nltk.tokenize import word_tokenize

class VoteClassifier(ClassifierI):
    def __init__(self,*classifiers):
        self._classifiers=classifiers
        
    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)
     
    def confidance(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        
        choice_votes= votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
# ! NaiveBayesClassifier
# ! MultinomialNB,GaussianNB,BernoulliNB
# ! LogisticRegression,SGDClassifier
# ! SVC,LinearSVC,NuSVC

short_pos = open("short_reviews/positive.txt",'r').read()
short_neg = open("short_reviews/negative.txt",'r').read()

documents =[]    

for r in short_pos.split('\n'):
    documents.append((r,'pos'))
for r in short_neg.split('\n'):
    documents.append((r,'neg') )

all_words =[]
short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
    all_words.append(w.lower())
for w in short_neg_words:
    all_words.append(w.lower())

#print(type(all_words))
all_words=nltk.FreqDist(all_words)
#print(type(all_words))

#print(all_words.most_common(15))
#print(all_words['dead'])

word_features = list(all_words.keys())[:5000]

def find_features(documents):
    words = word_tokenize(documents)
    features = {} 
    for w in word_features:
        features[w] = (w in words)
    return features

featuresets = [(find_features(rev),category) for (rev,category) in documents]
random.shuffle(featuresets)

# pozitive data example:
training_set = featuresets[:1000]
testing_set = featuresets[1000:2000]


classifier = nltk.NaiveBayesClassifier.train(training_set)

classifier_f = open("naivebayes.pickle","rb")
classifier = pickle.load(classifier_f)
classifier_f.close()

print("Original Naiva Bayes Algo accuracy percent: ", (nltk.classify.accuracy(classifier,testing_set))*100)
classifier.show_most_informative_features(15)

"""save_classifier = open('naivebayes.pickle','wb')
pickle.dump(classifier,save_classifier)
save_classifier.close()"""

# ! MultinomialNB,GaussianNB,BernoulliNB
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent: ", (nltk.classify.accuracy(MNB_classifier,testing_set))*100)

"""GNB_classifier = SklearnClassifier(GaussianNB())
GNB_classifier.train(training_set)
print("GaussianNB accuracy percent: ", (nltk.classify.accuracy(GNB_classifier,testing_set))*100)"""

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent: ", (nltk.classify.accuracy(BNB_classifier,testing_set))*100)

# ! LogisticRegression,SGDClassifier
LR_classifier = SklearnClassifier(LogisticRegression())
LR_classifier.train(training_set)
print("LogisticRegression accuracy percent: ", (nltk.classify.accuracy(LR_classifier,testing_set))*100)

SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(training_set)
print("SGDClassifier accuracy percent: ", (nltk.classify.accuracy(SGDC_classifier,testing_set))*100)

# ! SVC,LinearSVC,NuSVC
"""SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC accuracy percent: ", (nltk.classify.accuracy(SVC_classifier,testing_set))*100)
"""
LSVC_classifier = SklearnClassifier(LinearSVC())
LSVC_classifier.train(training_set)
print("LinearSVC accuracy percent: ", (nltk.classify.accuracy(LSVC_classifier,testing_set))*100)

NSVC_classifier = SklearnClassifier(NuSVC())
NSVC_classifier.train(training_set)
print("NuSVC accuracy percent: ", (nltk.classify.accuracy(NSVC_classifier,testing_set))*100)


#voted_classifier = VoteClassifier(classifier,MNB_classifier,BNB_classifier,LR_classifier,SGDC_classifier,LSVC_classifier,NSVC_classifier)
#print("voted_classifier accuracy percent: ", (nltk.classify.accuracy(voted_classifier,testing_set))*100)

'''
print("Classfication: ",voted_classifier.classify(testing_set[1][0]),
    'Confidence %:', voted_classifier.confidance(testing_set[1][0]))
print("Classfication: ",voted_classifier.classify(testing_set[2][0]),
    'Confidence %:', voted_classifier.confidance(testing_set[2][0]))
print("Classfication: ",voted_classifier.classify(testing_set[3][0]),
    'Confidence %:', voted_classifier.confidance(testing_set[3][0]))
print("Classfication: ",voted_classifier.classify(testing_set[4][0]),
    'Confidence %:', voted_classifier.confidance(testing_set[4][0]))
print("Classfication: ",voted_classifier.classify(testing_set[5][0]),
    'Confidence %:', voted_classifier.confidance(testing_set[5][0]))'''