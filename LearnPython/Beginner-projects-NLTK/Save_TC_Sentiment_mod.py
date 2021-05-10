import nltk
import random

from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import allign_words

from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC

from nltk.classify import ClassifierI
from statistics import mode


# ! NaiveBayesClassifier
# ! MultinomialNB,GaussianNB,BernoulliNB
# ! LogisticRegression,SGDClassifier
# ! SVC,LinearSVC,NuSVC

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


short_pos = open("short_reviews/positive.txt",'r').read()
short_neg = open("short_reviews/negative.txt",'r').read()

documents =[]    
all_words = []

# J is adject
allowed_word_types = ['J']


for p in short_pos.split('\n'):
    documents.append((p,'pos'))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    [all_words.append(w[0].lower()) for w in pos if w[1][0] in allowed_word_types]

for p in short_neg.split('\n'):
    documents.append((p,'neg'))
    words = word_tokenize(p)
    pos = nltk.pos_tag(words)
    [all_words.append(w[0].lower()) for w in pos if w[1][0] in allowed_word_types]

pickle.dump(documents,open('pickled_algos/documents.pickle','wb'))

all_words=nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]
pickle.dump(word_features,open('pickled_algos/word_features5k.pickle','wb'))

def find_features(documents):
    words = word_tokenize(documents)
    features = {} 
    for w in word_features:
        features[w] = (w in words)
    return features

featuresets = [(find_features(rev),category) for (rev,category) in documents]
random.shuffle(featuresets)
pickle.dump(featuresets,open('pickled_algos/featuresets5k.pickle','wb'))

# positive data example:
training_set = featuresets[:10000]
testing_set = featuresets[10000:]


# *****************************************************************************************************************************************
# ! NaiveBayesClassifier
NBC_classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naiva Bayes Algo accuracy percent: ", (nltk.classify.accuracy(NBC_classifier,testing_set))*100)
NBC_classifier.show_most_informative_features(15)
pickle.dump(NBC_classifier,open('pickled_algos/NBC_classifier5k.pickle','wb'))

# *****************************************************************************************************************************************
# ! MultinomialNB,GaussianNB,BernoulliNB
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MultinomialNB accuracy percent: ", (nltk.classify.accuracy(MNB_classifier,testing_set))*100)
pickle.dump(MNB_classifier,open('pickled_algos/MNB_classifier5k.pickle','wb'))

"""GNB_classifier = SklearnClassifier(GaussianNB())
GNB_classifier.train(training_set)
print("GaussianNB accuracy percent: ", (nltk.classify.accuracy(GNB_classifier,testing_set))*100)"""

BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print("BernoulliNB accuracy percent: ", (nltk.classify.accuracy(BNB_classifier,testing_set))*100)
pickle.dump(BNB_classifier,open('pickled_algos/BNB_classifier5k.pickle','wb'))
# *****************************************************************************************************************************************
# ! LogisticRegression,SGDClassifier
LR_classifier = SklearnClassifier(LogisticRegression())
LR_classifier.train(training_set)
print("LogisticRegression accuracy percent: ", (nltk.classify.accuracy(LR_classifier,testing_set))*100)
pickle.dump(LR_classifier,open('pickled_algos/LR_classifier5k.pickle','wb'))

SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(training_set)
print("SGDClassifier accuracy percent: ", (nltk.classify.accuracy(SGDC_classifier,testing_set))*100)
pickle.dump(SGDC_classifier,open('pickled_algos/SGDC_classifier5k.pickle','wb'))

# *****************************************************************************************************************************************
# ! SVC,LinearSVC,NuSVC
"""SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC accuracy percent: ", (nltk.classify.accuracy(SVC_classifier,testing_set))*100)
"""
LSVC_classifier = SklearnClassifier(LinearSVC())
LSVC_classifier.train(training_set)
print("LinearSVC accuracy percent: ", (nltk.classify.accuracy(LSVC_classifier,testing_set))*100)
pickle.dump(LSVC_classifier,open('pickled_algos/LSVC_classifier5k.pickle','wb'))

NSVC_classifier = SklearnClassifier(NuSVC())
NSVC_classifier.train(training_set)
print("NuSVC accuracy percent: ", (nltk.classify.accuracy(NSVC_classifier,testing_set))*100)
pickle.dump(NSVC_classifier,open('pickled_algos/NSVC_classifier5k.pickle','wb'))


# *****************************************************************************************************************************************
# ! VoteClassifier
voted_classifier = VoteClassifier(NBC_classifier,MNB_classifier,BNB_classifier,LR_classifier,SGDC_classifier,LSVC_classifier,NSVC_classifier)
print("voted_classifier accuracy percent: ", (nltk.classify.accuracy(voted_classifier,testing_set))*100)


def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats)