
import json
import pandas as pd
import re

newd = { "tag":"",# kind of input querstion, command,fact, opinion, idk
         "patterns": [], #possible inputs
         "responses": [],#possible responce
         "context": []
         }


def wjs(da, fn="chatbot project (1)\intents.json"):#write to json file
    with open(fn,"w") as f:
        json.dump(da,f, indent=4)



#opens json file and looks to the intents file.

def adtag():
    with open('chatbot project (1)\intents.json') as jf:
        da = json.load(jf)
        temp = da["intents"]# info under intents list in Array name not file

        temp.append()# appends new dictionary
    #wjs(da) #re loads content of intent file with new data


def look(fi):
    while True:
        cm = input('cm:')
        if cm == 'done':
            break
        elif cm == 'look':
            for i in fi:
                print(i)
        elif cm == 'ap':
            return #():# runs appropriate function
        else:
            continue


def inp(f):
    while True:
        variable = input("fact to save:")
        if variable == 'done':
            break
        else:
            f.write(str(variable)+"\n")

def findq(x):

    with open(x, "r",encoding="utf8") as f:#errors="ignore"
        fhand = f.read()
        lns= fhand.split("\n")
        count = 0
        nel = [i for i in lns if i.strip() != ""]
        for i in nel:
            count+=1
        print(count,nel)



def newf(x):# creates new file I can name
    fn = input("name: ")

    try:
        with open("data\scratch\{}.txt".format(fn),"w+") as f:
            f.write(x)
    except:
        return

    f.close()




#run the funcvtions
#newf() new file with name needs lines

findq("data\qu\canQ.txt")


"""
f = open("storedb.txt", "a")#empty file to load data
with open("storedb.txt", "r") as rf:# automatily closes file and
    con = f.read()# for small file
    lines = rf.readlines()# gets list of all the line with nl cgharachter
    pass
"""

# w+ creates or clears it/ empties content
# a appends to the last string
# r read? reads and can stor


#print()



#f.read(4)
#f.seek(37)
#f.readline() grab single line/next line
#f.writelines(lines)

#df = pd.read_json('E:\ITNTech\projects and management\capstone\chatbox\code\chatbot project (1)\intents.json')
# dataframe file


#dfc = df['intents']
# calling the series



#f.close()

#test string
#where is the file. I want lists and inouts here