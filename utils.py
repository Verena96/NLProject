#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Libs necessárias
import spacy
import PyPDF2
import textract
import pandas as pd
import re
import unidecode
import os
from calendar import month_name
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from time import time 
import numpy as np
from collections import Counter



#Support functions

import en_core_web_md
nlp = en_core_web_md.load()
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
stops = list(spacy_stopwords)
months = [m.lower() for m in month_name[1:]]
stopw = stops + months 
#stopwords
stopw += ['said','president','wall','street','standard','poors','ll','ve','vice','dow','jones','nasdaq','th',
          'chairman', 'chief', 'executive','new','york','analysts','federal','investors','economist','government',
          'economists','dollar','point','stock','time','stocks','points','bank','bond','nations','traders','face',
          'times','yields','generally','data','meeting','committee','figures','director','chairman','going','home','copom',
          'session','people','public','according','blue','chip','feds','banks','area','city','says','officials','day','secretary',
          'report','showed','todays','health','middle','class','crude','oil','focus','survey','ex','ante','copoms','baseline','the',
          'members','scenario']

def sub_str(x): 

    lista=[]

    for x in x.split():

        #x_1   = re.sub("([\d]+) *th",'',x)
        x_2=re.sub(r'[^a-zA-Z0-9]','',x)
        x_new = re.sub("\d+",'',x_2)
        #x_new = re.sub(r'(\d+)\s*(?:hours?\b|h?\b)','',x_)   
        lista+=[x_new]

    alpha_only_string = " ".join(lista)

    return alpha_only_string

#Cleaning functions

def split(x):

    if '\r\n' in x:

        x=x.split('\r\n')
        ''.join(x)
    else:

        x=x.split('\n')

        if '' in x:

            x.remove('')

    return ''.join(x)


def clean_words(t):
    x = []
    for w in t.split():
        if (len(w) > 2 and w not in stopw):
            x+=[w]
    z = ' '.join(x)
    return z

def clean_ents(t):
    doc = nlp(t)
    return " ".join([ent.text for ent in doc if not ent.ent_type_])




# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




