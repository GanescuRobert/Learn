import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from nltk.tokenize import word_tokenize
from nltk.translate.meteor_score import allign_words

from sklearn.naive_bayes import MultinomialNB,GaussianNB,BernoulliNB
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC

from nltk.classify import ClassifierI
from statistics import mode

from nltk.tokenize import word_tokenize

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

documents_f = open('pickled_algos/documents.pickle','rb')
documents = pickle.load(documents_f)
documents_f.close()

word_features5k_f = open('pickled_algos/word_features5k.pickle','rb')
word_features = pickle.load(word_features5k_f)
word_features5k_f.close()

def find_features(documents):
    words = word_tokenize(documents)
    features = {} 
    for w in word_features:
        features[w] = (w in words)
    return features

featuresets_f = open('pickled_algos/featuresets5k.pickle','rb')
featuresets = pickle.load(featuresets_f)
featuresets_f.close()

open_file = open('pickled_algos/NBC_classifier5k.pickle','rb')
NBC_classifier = pickle.load(open_file)
open_file.close()

#open_file = open('pickled_algos/MNB_classifier5k.pickle','rb')
#MNB_classifier = pickle.load(open_file)
#open_file.close()

#open_file = open('pickled_algos/BNB_classifier5k.pickle','rb')
#BNB_classifier = pickle.load(open_file)
#open_file.close()
#
#open_file = open('pickled_algos/LR_classifier5k.pickle','rb')
#LR_classifier = pickle.load(open_file)
#open_file.close()
#
#open_file = open('pickled_algos/SGDC_classifier5k.pickle','rb')
#SGDC_classifier = pickle.load(open_file)
#open_file.close()
#
#open_file = open('pickled_algos/LSVC_classifier5k.pickle','rb')
#LSVC_classifier = pickle.load(open_file)
#open_file.close()
#
#open_file = open('pickled_algos/NSVC_classifier5k.pickle','rb')
#NSVC_classifier = pickle.load(open_file)
#open_file.close()



# ! VoteClassifier
voted_classifier = VoteClassifier(NBC_classifier)#,MNB_classifier,BNB_classifier,LR_classifier,SGDC_classifier,LSVC_classifier,NSVC_classifier)


def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidance(feats)