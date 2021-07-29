import glob
import pathlib

syllables = set()

for p in pathlib.Path("syllable_segmentation_data").rglob("*.ssg"): # iterate through all files

    with open(p) as f: # for each file
        sentences = f.readlines()

    for i in range(len(sentences)):

        sentences[i] = sentences[i].replace("\n", "")
        sentences[i] = sentences[i].replace("<s/>", "~")
        sentences[i] = sentences[i].split("~") # create list of all syllables

        syllables = syllables.union(sentences[i])


    print(len(syllables))

# Filter out syllables with English words
import re

a = []

for s in syllables:
    print("---")
    if bool(re.match("^[\u0E00-\u0E7F]*$", s)) and s != "" and " " not in s:
        print("Thai:", s)
        a.append(s)
    else:
        print("Not thai:", s)

a = set(a)
a = dict(zip(list(a), range(len(a))))

import json
print(a)
print(len(a))
with open("thai-syllable.json", "w") as fp:
    json.dump(a, fp)