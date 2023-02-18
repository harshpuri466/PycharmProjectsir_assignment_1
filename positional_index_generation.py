path = "/Users/harshpuri/Desktop/ir_assignment_1/CSE508_Winter2023_Dataset"
import os
from text_preprocessing import get_tokenize

position={}
def create():
    os.chdir(path)
    for file in sorted(os.listdir()):
        file_path = f"{path}/{file}"
        with open(file_path, 'r') as f:
            content=str(f.read())
            tokens= get_tokenize(content)
            for i in range(len(tokens)):
                token= tokens[i]

                if token not in position:
                    position[token] = {}
                doc_dict=position[token]
                if file[-4:] not in doc_dict:
                    doc_dict[file[-4:]] = []
                doc_dict[file[-4:]].append(i)


create()
import os
import pickle

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)


pickling_on = open("postional_dict.pickle","wb")
pickle.dump(position, pickling_on)
pickling_on.close()



