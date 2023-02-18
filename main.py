import os
import re




def find_word(tag,text):
    reg_str = "<" + tag + ">(.*?)</" + tag + ">"
    res=re.findall(reg_str,text)
    return str(res)
def read_file(file_add):
    os.chdir(file_add)
    i=0
    for file in os.listdir():
        # print(file)
        # print(file)



        content=""

        file_path = f"{file_add}/{file}"
        with open(file_path, 'r') as f:
            a=str(f.read())
            # print(a)
            a=a.replace("\n","")


            title=find_word("TITLE", a)[2:-2]
            # print(f"title of the {file}={title}")

            body=find_word("TEXT", a)[2:-2]
            print(f"body of the {file}={body}")

            content=title+body
            print(content)
            f.close()

        f=open(file_path,"w")
        f.write(content)
        f.close()






path = "/Users/harshpuri/Desktop/ir_assignment_1/CSE508_Winter2023_Dataset"

read_file(path)

