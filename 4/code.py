import os, pathlib, re
os.chdir(pathlib.Path(__file__).parent.resolve())

with open('input','r') as fp:
    data = fp.readlines()


def level1():
    count = 0
    for line in data:
        if pattern := re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line):
            if int(pattern.group(1)) <= int(pattern.group(3)) and int(pattern.group(2)) >= int(pattern.group(4)):
                count += 1
                print(f'{line[:-1]} : {pattern.group(1)},{pattern.group(3)}')
            elif int(pattern.group(1)) >= int(pattern.group(3)) and int(pattern.group(2)) <= int(pattern.group(4)):
                count += 1
        else:
            print('error')

    print(len(data))
    print(count)

def level2():
    count = 0
    for line in data:
        if pattern := re.match(r'(\d+)-(\d+),(\d+)-(\d+)', line):
            if int(pattern.group(1)) <= int(pattern.group(4)) and int(pattern.group(1)) >= int(pattern.group(3)):
                count += 1
#                print(f'{line[:-1]} : {pattern.group(1)},{pattern.group(3)}')
            elif int(pattern.group(2)) <= int(pattern.group(4)) and int(pattern.group(2)) >= int(pattern.group(3)):
                count += 1
            elif int(pattern.group(1)) <= int(pattern.group(3)) and int(pattern.group(2)) >= int(pattern.group(4)):
                count += 1
            elif int(pattern.group(1)) >= int(pattern.group(3)) and int(pattern.group(2)) <= int(pattern.group(4)):
                count += 1
        else:
            print('error')
    print(count)

level2()    
