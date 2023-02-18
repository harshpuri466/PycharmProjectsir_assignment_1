from text_preprocessing import lower_str, get_tokenize, remove_punctuation, get_stop_word
import pickle
from basic_operation import function_or,function_and,function_not,function_and_not,function_and_or
import os
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)

pickle_off = open("dict.pickle", 'rb')
inverted_index = pickle.load(pickle_off)
# print(inverted_index)

pickle_off.close()


pickle_off = open("master.pickle", 'rb')
master = pickle.load(pickle_off)
# print(master)



pickle_off.close()
d= int(input())

answer=[]
enu=1
while d>0:
    str = input()
    content = lower_str(str)
    content = remove_punctuation(content)
    tokens = get_tokenize(content)
    final_tokens = get_stop_word(tokens)
    # print(final_tokens)
    order=input().split(",")
    query=f"Query {enu}:"
    query+=final_tokens[0]
    # print(final_tokens)
    # print(order)
    # print("------")
    for i in range(len(order)):
        query+=(" "+order[i]+" "+final_tokens[i+1])
    answer.append(query)
    # print(order)

    if(len(final_tokens)-len(order)==1):
        if(final_tokens[0] in inverted_index):
            l1=inverted_index[final_tokens[0]]
        else:
            l1=[]
        cmp=0
        for i in range(len(order)):
            op=order[i]
            l2=inverted_index[final_tokens[i+1]]
            if op=="AND":
                # specificheat beappreciably acorresponding
                l1,a=function_and(l1,l2)

                cmp+=a
            elif op=="OR":
                l1,a=function_or(l1,l2)
                cmp+=a
            elif op=="AND NOT":
                l1,a=function_and_not(l1,l2,master)
                cmp+=a
            else:
                l1,a=function_and_or(l1,l2,master)
                cmp+=a

        answer.append(f"Number of documents retrieved for query{enu}:{len(l1)}")
        str1=f"Names of the documents retrieved for query{enu}:"
        for i in l1:
            str1+=("carnfield"+i+",")
        answer.append(str1[:-1])
        answer.append(f"Number of comparisons required for query{enu}:{cmp}")


    d-=1
    enu+=1





for i in answer:
    print(i)
