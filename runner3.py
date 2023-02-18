def function_and(T1, T2):
    list1 = T1
    list2 = T2
    len1 = len(list1)
    len2 = len(list2)
    comparision = 0
    i = 0
    j = 0
    final_list = []
    while (i < len1 and j < len2):
        if (int(list1[i]) == int(list2[j])):
            final_list.append(list1[i])
            i += 1
            j += 1

        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
        comparision += 1
    return final_list, comparision


def common_doc_selector(T1, T2):  # here T1 and T2 are list of docs in which words are present
    T3, _ = function_and(T1, T2)
    return T3


def contains_value(value,_list):
    if value in _list:
        return True
    return False


def checker(doc_value,word_list,pos_dict):
    for value in pos_dict[word_list[0]][doc_value]:
        flag = True
        for i in range(1,len(word_list)):
            if value+i not in pos_dict[word_list[i]][doc_value]:
                flag = False
                break
        if flag:
            return True
    return False





def query_int(word_list, pos_dict):  # list of words in which AND  is required to perform
    T_list = []
    for i in word_list:
        if i not in pos_dict:
            return []
    for word in word_list:
        temp = []
        for keys in pos_dict[word].keys():
            temp.append(keys)
        T_list.append(temp)

    T_common = common_doc_selector(T_list[0], T_list[1])
    print(T_common)
    for i in range(2, len(T_list)):
        T_common = common_doc_selector(T_list[i], T_common)
    ans_list = []
    for value in T_common:
        if checker(value,word_list,pos_dict):
            ans_list.append(value)
    return ans_list


import os
import pickle
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)

pickle_off = open("postional_dict.pickle", 'rb')
pos_dict_1 = pickle.load(pickle_off)

pickle_off.close()
from runner2 import find_bigram_query
answer=[]
from text_preprocessing import remove_punctuation, get_tokenize, get_stop_word

q= int(input())

for i in range(q):
    str=input()
    query = str

    content = query.lower()

    content = remove_punctuation(content)
    tokens = get_tokenize(content)
    final_tokens = get_stop_word(tokens)
    a=find_bigram_query(str,i+1)
    for el in a :
        answer.append(el)

    b=query_int(final_tokens,pos_dict_1)
    answer.append(f"Number of documents retrieved for query {q+1} using positional inverted index:{len(b)}")
    a = f"Names of documents retrieved for query {q+1} using postional inverted index:"
    strt = ""

    if(len(b)!=0):
        for k in b:
            c = "carnfield" + k + ","
            strt += c
        answer.append(a + strt[:-1])
    else:
        answer.append(a)






for i in answer:
    print(i)

