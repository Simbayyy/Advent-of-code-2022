import os, pathlib
os.chdir(pathlib.Path(__file__).parent.resolve())

class Elf:
    def __init__(self):
        self.food = []
    def calories(self):
        return sum(self.food)

elves = [Elf()]

with open('input','r') as fp:
    data = fp.readlines()

for line in data:
    if len(line) == 1:
        elves.append(Elf())
    else:
        elves[-1].food.append(int(line))

print(f"Day 1 solution is {max([elf.calories() for elf in elves])}")

print(f"Day 1.2 solution is {sum(sorted([elf.calories() for elf in elves])[-3:])}")