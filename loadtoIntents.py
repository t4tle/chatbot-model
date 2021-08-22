import re
import csv
import pandas as pd
import os
import random
import numpy as np
import json
import pickle
import warnings
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer, LancasterStemmer
from string import punctuation
from nltk.corpus import stopwords

"""
this is a test sentence. Don't take it seriously!
cm: talk / q/ done

x = input("test:")

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
"""
# linear algebra
# data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
"""
df4 = pd.read_csv('data_structure\data\pair\QAdsets\S08_question_answer_pairs.txt', header=None)
df5 = pd.read_csv('data_structure\data\pair\QAdsets\S09_question_answer_pairs.txt', header=None)
df5 = pd.read_csv('data_structure\data\pair\QAdsets\S10_question_answer_pairs.txt', header=None)
"""


df1 = pd.read_csv('data_structure\data\pair\QAdsets\kids_teen.tsv', sep='\t', header=0)
df2 = pd.read_csv('data_structure\data\pair\QAdsets\master_season1-35.tsv', sep='\t', header=0)
df3 = pd.read_csv('data_structure\data\pair\QAdsets\JEOPARDY_CSV.csv', header=0)

# column values
cols = list(df1.columns.values)
cols2 = list(df2.columns.values)
cols3 = list(df3.columns.values)

q = pd.concat([df1['question'], df2['question'], df3[' Question']])
a = pd.concat([df1['answer'], df2['answer'], df3[' Answer']])
c = pd.concat([df1['category'], df2['category'], df3[' Category']])

qa = pd.concat([q, a, c], axis=1)  # jepordy question

qa = qa.rename(columns={0: "question", 1: "answer", 2: "category"})  # good

# print(qa.head(3))


cat = qa.category.unique()  # categories


def wjs(da, fn="data_structure\data\pair\intsets.json"):  # write to json file
    with open(fn, "w") as f:
        json.dump(da, f, indent=4)


newd = {"tag": "",  # kind of input querstion, command,fact, opinion, idk
        "patterns": [],  # possible inputs q
        "responses": [],  # possible responce A
        "context": []  # Facts
        }

# def adtag(di):
with open('data_structure\data\pair\intsets.json') as jf:
    da = json.load(jf)
    temp = da["intents"]  # info under intents list in Array name not file
    for i in temp:
        t = i["tag"]
        p = i["patterns"]
        r = i["responses"]
        co = i["context"]
        li = qa.loc[qa['category'].str.contains(t, regex=False)]
        ql = li['question'].tolist()
        al = li['answer'].tolist()
        asicon = []
        if len(ql) == 0:
            continue
        else:

            p.append(ql)
            r.append(al)
            co.append("dir")

    wjs(da)  # re loads content of intent file with new data
"""
                        for c in range(len(ql)):
                 con = ([ql[c],al[c]])

                 asicon.append(con)
"""

# appends new item to list of dictionary


# list[i][1] anser/fact about question, list[i][0] suject in question
# print(asicon[3][1],asicon[3][0])
