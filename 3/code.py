import os, pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())

with open('input','r') as fp:
    data = fp.readlines()


def level1():
    duplicates = []


    for line in data:
        length = len(line)-1
        block1 = line[:int(length/2)]
        block2 = line[int(length/2):]
        for char in block1:
            if char in block2:
                duplicates.append(char)
                break

    result = 0

    for elt in duplicates:
        ordelt = ord(elt)
        if ordelt %64 < 30:
            result += 26

        result += ordelt % 32
    print(len(data))
    print(len(duplicates))
    print(result)   

def level2():
    result = 0
    count = 0
    for index in range(int(len(data)/3)):
        for elt in data[3*index]:
            if elt in data[3*index+1] and elt in data[3*index + 2]:
                ordelt = ord(elt)
                count +=1
                if ordelt %64 < 30:
                    result += 26

                result += ordelt % 32
                break
    print(count)
    print(result)



level2()