from pprint import pprint
from random import randint
import copy

#
# Ak to robite v pythone ten virtualny stroj si predstavte proste ako nejaku klasu kde mate ulozenu mapu
# Ta pamat toho stroja je proste pythonovsky list o velkosti 64 kde kazdy element je cislo od 0 do 256
# Tych 64 buniek pamati su zaroven geny chromozomu jedindcov, ktore crossoverujete a menite, a mutujete.
# Ked testujete jedinca, poslete jeho genu ako tu pamat do virtulaneho stroja
# Tam mate metodu kde proste mate pointer nastaveny na 0 na zaciatku akoze na prvy element
#
# subject sa mozno zaobide len s memory v strukture
class Struct(object):
    def __init__(self, size, treasures, map=None, memory=None):
        if map is None:
            map = [[], []]
        if memory is None:
            memory = [[]]
        self.size = size
        self.treasures = treasures
        self.map = map
        self.memory = memory


def write(address, memory):
    if memory[address] & 3 == 3:
        return 'H'
    elif memory[address] & 3 == 2:
        return 'D'
    elif memory[address] & 3 == 1:
        return 'P'
    else:
        return 'L'
    return


def jump(address, memory):
    return memory[address], address


def incement(address, memory):
    if memory[address] == 63:
        memory[address] = 0
    else:
        memory[address] += 1
    return memory


def decrement(address, memory):
    if memory[address] == 0:
        memory[address] = 63
    else:
        memory[address] -= 1
    return memory


def start_finding(subjects):
    sub = copy.deepcopy(subjects)
    gene = sub.pop()
    new_address = 0
    counter = 500
    i = gene.memory[new_address]
    while counter:
        if i >= 192:
            write(i & 63, gene.memory)
        elif i >= 128:
            i, new_address = jump(i & 63, gene.memory)
            counter -= 1
            continue
        elif i >= 64:
            gene.memory = decrement(i & 63, gene.memory)
        else:
            gene.memory = incement(i & 63, gene.memory)
        new_address = (new_address + 1) % 64
        i = gene.memory[new_address]
        counter -= 1
    return


def generate_memory():
    memory = []
    for i in range(64):
        memory.append(randint(0, 256))
    return memory


def make_map(map, Lines, size):
    start = []
    treasure = []
    for row, line in enumerate(Lines):
        if row == 0:
            continue
        coordinates = line.split(" ")
        for col in range(size):
            map[row-1][col] = int(coordinates[col])
            if int(coordinates[col]) == -1:
                start.append(row - 1)
                start.append(col)
            if int(coordinates[col]) == 1:
                treasure.append(row - 1)
                treasure.append(col)
    return start, treasure


def main():
    file = open('test.txt', 'r')
    Lines = file.readlines()
    info = Lines[0].split(" ")
    size = int(info[0])
    number_of_treasures = int(info[1])

    map = [[0 for _ in range(size)] for _ in range(size)]
    start, treasures = make_map(map, Lines, size)
    file.close()
    for i in range(20):
        memory = generate_memory()
        subject = Struct(size, treasures, map, memory)
        subjects = [subject]
        start_finding(subjects)
        memory.clear()

main()