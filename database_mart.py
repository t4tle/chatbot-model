import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer , WordNetLemmatizer,LancasterStemmer
from string import punctuation

ls = LancasterStemmer()

import pandas as pd
import json
import spacy
import numpy as np
import random
import string
import re

#nltk.download()


#f = open('dm.txt', 'r', errors='ignore')
#raw = f.read()
ps = PorterStemmer()
tl = WordNetLemmatizer()

# ctoke = PunktSentenceTokenizer(training_data) # trainiable machine learning tokenizer
# tokenizing- sentences / words
# lexicon and corpas
# corpa - body of text
# lexicon - words meanings  later into values


"""
path = "file dir"
file = 'file name'

dfjson  = pd.read_json(path + file)

dfsql = pd.read_sql("file name")

df = pd.read_json('F:\ITNTech\projects and management\capstone\chatbox\code\chatbot project (1)\intents.json')
# dataframe


dfc = df['intents']
# series

"""


#  the user input

def ntlsorted(x):
    ignore_letters = ['!', '?', ',', '.']
    plw = {}  #
    plw['orig'] = x  # input / full string
    plw['tw'] = []
    plw['p'] = []
    # tokenizing
    plw['is'] = word_tokenize(x)  # spliting by word or space /list
    for i in plw['is']:
        if i in ignore_letters:
            plw['p'].append(i)# punctuation list
        else:
            plw['tw'].append(i.lower())# list of words lowered

    plw['ts'] = sent_tokenize(x)  # spliting by sentence / list
    # associate punctuation with sntence

    # lemmaztize and lower each word and remove duplicates

    plw['nostp'] = remo_sw(plw['tw'])  # list with removed stop words / list
    #plw['stem'] = [fun() for w in tw]
    # NEEDS A LIST OF LOWERED NON punctuation words
    plw['pos'] = ps(nltk.pos_tag(plw['tw']))  # adds part of speech or puncuation /list of tuples
    plw['posu'] = ps(nltk.pos_tag(plw['tw'], tagset='universal'))
    # [('this', 'DT'), ('is', 'VBZ')
    #plw['lw'] = lema(plw['pos'])
    plw['l'] = len(plw['tw'])
    return plw


def remo_sw(tw):# removes fluff words
    stemw = []
    sw = set(stopwords.words("english"))  # fluff, filler words
    for i in tw:
        stemw.append(ps.stem(i))

    return stemw


def sortsen():
    return

def ps(lt):
    posl = []
    for i in lt:
        li = []
        for x in i:
            li.append(x)
        posl.append(li[1])
    return posl

def chw(tw):#pull all
    reg = r"""Chunk: {<RB.?>*<VB>} """
    reg.draw()
    return


def chink():  # chunk everything exept
    reg = r"""Chunk: {<RB.?>*<VB>} """
    # use regex to find pos tag
    # cp = nltk.RegexpParser.(regexvariable)
    # chunk = cp.parse(pos)

    # chunked.draw()
    return


def lema(tw):# finds the root of the word animal to anima
    lw=[]
    for i in tw:
        lw.append(tl.lemmatize(i[0],i[1]))

    return lw


"""
fs = [w for w in tw if not w in sw]# sw filtered sentence
print(ts)
print(tw)
print(sw)
print(stemw)
print(pos)
"""

ws = [('who', 'WP'), ('what', 'WP'), ('when', 'WRB'), ('where', 'WRB'), ('why', 'WRB'), ('how', 'WRB'),
      ('which', 'WDT')]
# WP wh-pronoun who, what
# WRB wh-abverb where, when
#

"""
print(ui)
print(tw)
print(pos)
"""
def runit():
    while True:
        ui = input('command:')
        if ui == 'done':# leaves bot
            break
        if ui == 'talk':# comunicate
            s = input("test sentence:")
            stip = ntlsorted(s)
            return stip
        if ui == 'q': #question

            pass
        else:
            print("no command try again")



#x = runit()
#print(x)  # sorted input
"""

"""


"""
for x, y in (stip).items():

   print(x, type(y))

"""

# this is a test sentence. Don't take it seriously!
