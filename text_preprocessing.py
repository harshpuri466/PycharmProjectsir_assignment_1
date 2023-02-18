import fileinput

import nltk
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from nltk import word_tokenize,sent_tokenize
import nltk

def lower_str(para):
    return para.lower()

def get_tokenize(para):
    return word_tokenize(para)

def get_stop_word(word_token):
    stop_words = set(stopwords.words('english'))
    without_stop_word=[]
    for w in word_token:
        if w not in stop_words:
            without_stop_word.append(w)
    return without_stop_word

def remove_punctuation(test_str):
    test_str = test_str.translate(str.maketrans('', '', string.punctuation))
    return test_str
def remove_blank_spces(tokens):
     new_token=[]
     for  i in tokens:
         if i==" ":
             continue
         else:
             new_token.append(i)
     return new_token


path= "/Users/harshpuri/Desktop/ir_assignment_1/CSE508_Winter2023_Dataset"

def edit_file(path):
    os.chdir(path)
    for file in os.listdir():
        file_path = f"{path}/{file}"
        f=open(file_path,"r")
        content= str(f.read())
        f.close()

        # print("intital content",content)
        content= lower_str(content)
        content=remove_punctuation(content)
        tokens=get_tokenize(content)
        final_tokens=get_stop_word(tokens)
        # print("final_content",final_tokens)

        f=open(file_path,"w")

        for item in final_tokens:
            f.write(item + " ")
        f.close()



edit_file(path)





