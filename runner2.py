import pickle
from text_preprocessing import lower_str, remove_punctuation, stopwords, get_tokenize, get_stop_word
import os
import pickle
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
pickle_off = open("bigram.pickle", 'rb')
inverted_index = pickle.load(pickle_off)
pickle_off.close()

from basic_operation import function_and
# print(inverted_index)
# num=int(input())

# # print()
# # print()
# # print()
def find_bigram_query(sent, ind):
    answer=[]


    for i in range(1):
        query=sent
        # print(query)

        content = query.lower()
        # print(content)
        content = remove_punctuation(content)
        tokens = get_tokenize(content)
        # print("tookens are:",tokens)
        final_tokens = get_stop_word(tokens)
        # print(final_tokens)
        bigrams_token=[]
        i=0
        if len(final_tokens)==1:
            final_tokens.append(" ")
        while i<len(final_tokens)-1:
            bigrams_token.append(final_tokens[i]+" "+final_tokens[i+1])
            i+=1
        l1=[]
        if bigrams_token[0] in inverted_index:
            l1=inverted_index[bigrams_token[0]]
        # print(l1)
        # print(bigrams_token)
        for i in range(1,len(bigrams_token)):
            l2=[]
            # print(bigrams_token[i])

            if bigrams_token[i] in inverted_index:
                l2 = inverted_index[bigrams_token[i]]
                # print("yeeeeed")


            # print(l2)
            l1,cmp=function_and(l1,l2)
        answer.append(f"Number of documents retrieved for query {ind} using bigram inverted index:{len(l1)}")
        a=f"Names of documents retrieved for query {ind} using bigram inverted index:"
        str=""
        print(l1)
        for k in l1:
            b= "carnfield"+k+","
            str+=b

        answer.append(a+str[:-1])

    return answer




