import time
import numpy as np

start = time.time()
print(start)
import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer, LancasterStemmer
import tensorflow
import tflearn
import random
from tkinter import *

start = time.time()
print(start)

le = WordNetLemmatizer()
ls = LancasterStemmer()

with open('data_structure\data\pair\intsets.json') as jf:
    da = json.load(jf)

with open("data_structure\chatbot\mdata.pickle", "rb") as f:
    words, labels, training, output = pickle.load(f)

# tensorflow.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("data_structure\chatbot\model.tflearn")
except:
    model.fit(training, output, n_epoch=100, batch_size=8, show_metric=True)
    model.save("data_structure\chatbot\model.tflearn")


def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [ls.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return np.array(bag)


def chat():
    print("Start talking with the bot (type quit to stop)!")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        results = model.predict([bag_of_words(inp, words)])
        results_index = np.argmax(results)
        tag = labels[results_index]

        for tg in da["intents"]:
            if tg['tag'] == tag:
                responses = tg['responses'][0]

        print(random.choice(responses))


chat()
