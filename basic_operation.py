#  here retrieving the basic dictionary and the basic set of all the files


# import pickle
# pickle_off = open("dict.pickle", 'rb')
# inverted_index = pickle.load(pickle_off)
# print(inverted_index)
#
# pickle_off.close()
#
#
# pickle_off = open("master.pickle", 'rb')
# master = pickle.load(pickle_off)
# print(master)
#
# pickle_off.close()
# -------------------------------------------------------------> retrived all the dictionary of the unigram model




def function_and(T1,T2):
    list1=T1
    list2=T2
    len1=len(list1)
    len2=len(list2)
    comparision=0
    i=0
    j=0
    final_list=[]
    while(i<len1 and j<len2):
        if(int(list1[i])==int(list2[j])):
            final_list.append(list1[i])
            i+=1
            j+=1

        elif list1[i]<list2[j]:
            i+=1
        else:
            j+=1
        comparision+=1
    return final_list,comparision


def function_or(w1, w2):
    l1 = w1
    l2 = w2
    p1 = 0
    p2 = 0
    union = []
    cmp = 0
    while p1 < len(l1) and p2 < len(l2):
        if int(l1[p1]) == int(l2[p2]):
            union.append(l1[p1])
            p1 += 1
            p2 += 1
        elif int(l1[p1]) < int(l2[p2]):
            union.append(l1[p1])
            p1 += 1
        else:
            union.append(l2[p2])
            p2 += 1
        cmp += 1
    while p1 < len(l1):
        union.append(l1[p1])
        p1 += 1

    while p2 < len(l2):
        union.append(l2[p2])
        p2 += 1
    return union, cmp


def function_not(T1,master):
    T2=set(master)-set(T1)
    T2= list(T2)

    return sorted(T2)

def function_and_not(T1,T2,master):
    T3= function_not(T2,master)
    uni,cmp=function_and(T1,T3)
    return uni,cmp

def function_and_or(T1,T2,master):
    T3=function_not(T2,master)
    uni,cmp=function_or(T1,T3)
    return uni,cmp

