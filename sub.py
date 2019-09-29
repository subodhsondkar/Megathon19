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
    insensitive_hippo = re.compile(re.escape("" + word), re.IGNORECASE)
    return insensitive_hippo.sub('__________________', sentence)

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
        return (word, sentence, replaced)
    else:
        #print("words are empty")
        return (None, sentence, None)
    
def replaceKey(sposs, poss):
    (word, sentence, replaced) = removeWord(sposs, poss)
    if replaced is None:
        return [sposs, None]
    else:
        return [sentence, word] 

file = open(input())
text = file.read()
paragraphs = text.split(".")
while "" in paragraphs:
    paragraphs.remove("")
y = []
for paragraph in paragraphs:
    sposs, poss = blobbing(paragraph)
    x = replaceKey(sposs, poss)
    y += [{"text": x[0], "fibs": x[1]}]

import json
f = open("chemistry.json", "w+")

f.write(json.dumps(y) + "\n")
f.close()

