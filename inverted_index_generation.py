import os
import pickle
dict={}
master=[]





def create_dict(file_path):
    file_path = r"/Users/harshpuri/Desktop/ir_assignment_1/CSE508_Winter2023_Dataset"
    os.chdir(file_path)
    # dict = {}
    # master = set()
    for file in sorted(os.listdir()):
        path = file_path + "/" + file
        f = open(path, "r")
        file_number = file[-4:]
        master.append(file_number)
        temp = f.read()
        appeared_words = set()
        for word in temp.split(" "):
            if word not in dict:
                dict[word] = []
            if word not in appeared_words:
                dict[word].append(file_number)
                appeared_words.add(word)

    for word in dict.keys():
        print(word, dict[word])



#
create_dict("")
print(master,dict)
print(type(master))
print(type(dict))
#  here we are pickling the dictionary

import os
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)


pickling_on = open("dict.pickle","wb")
pickle.dump(dict, pickling_on)
pickling_on.close()

pickling_on = open("master.pickle","wb")
pickle.dump(master, pickling_on)
pickling_on.close()

