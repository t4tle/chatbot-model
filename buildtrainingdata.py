import time
import numpy as np
start = time.time()
print(start)
import json
import pickle
import nltk
from nltk.stem import WordNetLemmatizer, LancasterStemmer


start = time.time()
print(start)

le = WordNetLemmatizer()
ls = LancasterStemmer()

words = []
classes = []
documents = []
ignore_letters = ['!', '?', ',', '.', ]

with open('data_structure\data\pair\intsets.json') as jf:
    da = json.load(jf)

# da["intents"]  # info under intents list in Array name not file
    for i in da["intents"][:30]:  # reduce list of data
        t = i["tag"]
        p = i["patterns"][0]
        r = i["responses"][0]
        co = i["context"]
        for pat in p:
            word = nltk.word_tokenize(pat)
            if word[0] == '(' or 'href=' in word:
                continue

            else:
                words.append(word)
                documents.append((word, t))
                if t not in classes:
                    classes.append(t)
    mid = time.time()

    print(mid)
    words = [w for w in words if w not in ignore_letters]
    #words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))

    training = []
    output = []
    output_empty = [0] * len(classes)  # training set, bag of words for each sentence
    for x, doc in enumerate(documents):
        pattern_words = doc[0]
        # lemmatize each word - create base word, in attempt to represent related words
        pattern_words = [ls.stem(word) for word in pattern_words]
        # create our bag of words array with 1, if word match found in current pattern
        bag = [1 if word in pattern_words else 0 for word in words]
        # output is a '0' for each tag and '1' for current tag (for each pattern)
        output_row = output_empty[:]
        output_row[classes.index(doc[1])] = 1

        training.append(bag)
        output.append(output_row)

    end = time.time()
    training = np.array(training)
    output = np.array(output)

    # create train and test lists. X - patterns, Y - intents
    train_x = list(training[:, 0])
    train_y = list(training[:, 1])

    print("Training data created")

    print(output)

    with open("data_structure\chatbot\mdata.pickle", "wb") as f:
        pickle.dump((words, classes, training, output), f)

