import os
path = "/Users/harshpuri/Desktop/ir_assignment_1/CSE508_Winter2023_Dataset"

def create_bi_index(file_path):
    file_path = r"/Users/harshpuri/Desktop/ir_assignment_1/CSE508_Winter2023_Dataset"
    os.chdir(file_path)
    dict = {}
    for file in sorted(os.listdir()):
        path = file_path + "/" + file
        f = open(path, "r")
        file_number = (file[-4:])
        temp = f.read()
        appeared_words = set()
        list_words = temp.split(" ")
        for i in range (0,len(list_words)-1):
            bi_word = list_words[i]+" "+ list_words[i+1]
            if bi_word not in dict:
                dict[bi_word] = []
            if bi_word not in appeared_words:
                dict[bi_word].append(file_number)
                appeared_words.add(bi_word)

    for word in dict.keys():
        print(word, dict[word])
    return  dict

bi_grams=create_bi_index(" ")
import os
import pickle
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)


pickling_on = open("bigram.pickle","wb")
pickle.dump(bi_grams, pickling_on)
pickling_on.close()
