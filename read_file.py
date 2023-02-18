import os

path = "/Users/harshpuri/Desktop/ir_assignment_1/CSE508_Winter2023_Dataset"
def read_example():
    os.chdir(path)
    i=1
    for file in os.listdir():
        file_path = f"{path}/{file}"
        if i<=5:
            with open(file_path, 'r') as f:
                a=str(f.read())
                print(f"content for the {file}={a}")
                i+=1
        else :
            exit()


read_example()