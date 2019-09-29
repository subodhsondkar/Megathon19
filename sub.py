from textblob import TextBlob
import random
import re

def blobbing(text):
    blobbedtext = TextBlob(text)
    poss = {}
    sposs = blobbedtext.string;
    for bt in blobbedtext.tags:
        tag = bt[1]
        if tag not in poss:
            poss[tag] = []
        if bt[0] not in {"'", "-", ";", ":"} and bt[0] not in poss[tag]:
            poss[tag].append(bt[0])
    return sposs, poss

def replaceIC(word, sentence):
    temp_re = re.compile(re.escape("" + word), re.IGNORECASE)
    return temp_re.sub('__________________', sentence)

def removeWord(sentence, poss):
    words = None
    if 'NNP' in poss:
        words = poss['NNP']
    elif 'NN' in poss:
        words = poss['NN']
    else:
        #print("NN and NNP not found")
        return (None, sentence, None)
    if len(words) > 0:
        word = random.choice(words) # randomisation ki jagah global kuchh algo maarneka
        replaced = replaceIC(word, sentence)
        return (words, sentence, replaced)
    else:
        #print("words are empty")
        return (None, sentence, None)

def replaceKey(sposs, poss):
    (word, sentence, replaced) = removeWord(sposs, poss)
    if replaced is None:
        return [sposs, None]
    else:
        return [sentence, word] 

import json
fl1 = open(input(), "w+")
fl2 = open(input())
text = fl2.read()
fl2.close()
paragraphs = text.split(".")
while "" in paragraphs:
    paragraphs.remove("")
for i in range(len(paragraphs)):
    paragraphs[i] = paragraphs[i].replace("\n", "")
for paragraph in paragraphs:
    sposs, poss = blobbing(paragraph)
    x = replaceKey(sposs, poss)
    y = {"text": x[0], "fibs": x[1]}
    fl1.write(json.dumps(y) + "\n")

fl1.close()

