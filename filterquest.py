import re
import csv

"""
this is a test sentence. Don't take it seriously!
cm: talk / q/ done

x = input("test:")
"""
n = input("fname:")

canq = []

with open("data_structure\data\scource\qu\mostAskedgoogle.txt","r",encoding="utf8") as c1:
    next(c1)
    for i in c1:
        l = i.strip()
        try:
            q1 = re.findall(r"([a-zA-Z]+( [a-zA-Z]+)+)",l)
            q = q1[0][0]
            canq.append(q)
        except:
            continue

print(len(canq),canq)

with open('data_structure\data\cform\{}.csv'.format(n), 'w', newline='') as csvfile:
    srite = csv.writer(csvfile)
    srite.writerow(canq)
