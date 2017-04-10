#!/usr/bin/python

import os
import pickle
import re
import sys

sys.path.append( "../tools/" )
from parse_out_email_text import parseOutText

"""
    Starter code to process the emails from Sara and Chris to extract
    the features and get the documents ready for classification.

    The list of all the emails from Sara are in the from_sara list
    likewise for emails from Chris (from_chris)

    The actual documents are in the Enron email dataset, which
    you downloaded/unpacked in Part 0 of the first mini-project. If you have
    not obtained the Enron email corpus, run startup.py in the tools folder.

    The data is stored in lists and packed away in pickle files at the end.
"""


from_sara  = open("from_sara.txt", "r")
from_chris = open("from_chris.txt", "r")

from_data = []
word_data = []

### temp_counter is a way to speed up the development--there are
### thousands of emails from Sara and Chris, so running over all of them
### can take a long time
### temp_counter helps you only look at the first 200 emails in the list so you
### can iterate your modifications quicker
temp_counter = 0


for name, from_person in [("sara", from_sara), ("chris", from_chris)]:
    for path in from_person:
        ### only look at first 200 emails when developing
        ### once everything is working, remove this line to run over full dataset
        temp_counter += 1
       # print temp_counter
        if temp_counter > 0:            
            path = os.path.join('..', path[:-1])
            email = open(path, "r")
            
            ### use parseOutText to extract the text from the opened email
            parsed_email =  parseOutText(email)
            # .encode('ascii')

            ### use str.replace() to remove any instances of the words
            ### ["sara", "shackleton", "chris", "germani"]
            names = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]
            # names = ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf", "houectect", "houect", "houston"]
            for name in names:
                parsed_email = parsed_email.replace(name, "")
            ## append the text to word_data
            word_data.append(parsed_email)

            ### append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            # print from_person.name
            if from_person.name == 'from_sara.txt':
                from_data.append(0)
            if from_person.name == 'from_chris.txt':
                from_data.append(1)

            email.close()

print "emails processed"
from_sara.close()
from_chris.close()

print word_data[152]
print word_data.__class__.__name__
print from_data

pickle.dump( word_data, open("your_word_data.pkl", "w") )
pickle.dump( from_data, open("your_email_authors.pkl", "w") )



### in Part 4, do TfIdf vectorization here

# from sklearn.feature_extraction import stop_words
# stop_words_eng = stop_words.ENGLISH_STOP_WORDS

# for idx, data in enumerate(word_data):
#     for sw in stop_words_eng:
#         data = data.replace(sw, '')
#     word_data[idx] = data

spliter = '_____'
file = open("word_data.txt","w") 
for word in word_data:    
    file.write(word) 
    file.write(spliter)
file.close() 
file = open("word_data.txt", "r") 
content = file.read() 
loaded_word_data = content.split(spliter)
loaded_word_data.pop()

print word_data == loaded_word_data

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)

print '-'*100
vectorizer.fit_transform(word_data)
vocab_list = vectorizer.get_feature_names()
print len(vocab_list)
print vocab_list[34597]
### 200 words should have 3805
### 17578 mails   38785 words



