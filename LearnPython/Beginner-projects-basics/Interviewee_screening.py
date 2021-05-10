# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 19:08:02 2020

@author: robyb
"""

applicants_dict = {'Anna':{'experience':2,
                           'languages':['Python','Ruby','Rust','Java'],
                           'proj_supervision':False},
                   'Calvin':{'experience':5,
                           'languages':['Java','Haskell','C++','Perl'],
                           'proj_supervision':False},
                   'Ben':{'experience':3,
                           'languages':['Python','C','Scala','Java'],
                           'proj_supervision':True},
                   'Dorothy':{'experience':6,
                           'languages':['Python','Elm','Clojure','Java'],
                           'proj_supervision':False},
                   'Esther':{'experience':4,
                           'languages':['Java','Go','Ruby','C#'],
                           'proj_supervision':True},
                   }

min_experience=4
requaired_languages = ['Python','Java']

for name,cv_dict in applicants_dict.items():
    if cv_dict['experience']>=min_experience and \
        (set(requaired_languages).issubset(set(cv_dict['languages']))or
         cv_dict['proj_supervision']):
            print(name,'passes the screening.')
            