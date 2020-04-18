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
class Map(object):
    def __init__(self, size, start, treasures, number_of_treasures, map=None):
        if map is None:
            map = [[], []]
        if treasures is None:
            treasures = [[]]
        self.number_of_treasures = number_of_treasures
        self.size = size
        self.treasures = treasures
        self.start = start
        self.map = map


class Memory(object):
    def __init__(self, fitness, path=None, memory=None):
        if memory is None:
            memory = [[]]
        if path is None:
            path = [[]]
        self.memory = memory
        self.path = path
        self.fitness = fitness


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


def is_in_map(position, size):
    if 0 <= position[0] < size:
        if 0 <= position[1] < size:
            return True
    return False

# :)
def is_on_treasure(position, treasures, found):
    for i in range(0, len(treasures), 2):
        if position[0] == treasures[i]:
            if position[1] == treasures[i+1]:
                for j in found:
                    if position == j:
                        return False
                return True
    return False


def found_all(found, all):
    if len(found) == all:
        return True
    return False


def new_position(direction, position):
    vertical = 0
    horizontal = 0
    if direction == 'H':
        vertical = -1
    elif direction == 'D':
        vertical = 1
    elif direction == 'L':
        horizontal = -1
    else:
        horizontal = 1
    position[0] = position[0] + vertical
    position[1] = position[1] + horizontal
    return position


def calculate_fitness(steps, found, all, path):
    fitness = len(found) - (steps * 0.001)
    fitness = round(fitness, 3)
    if fitness > len(all)/2 - 1:
        print(fitness, path, found)
    return fitness


def start_finding(subjects, parameters, number_of_subject):
    gene = copy.deepcopy(subjects[number_of_subject])
    position = copy.deepcopy(parameters.start)
    path = ""
    new_address = 0
    counter = 500
    steps = 0
    found = []
    i = gene.memory[new_address]
    while counter:
        if i >= 192:
            steps += 1
            direction = write(i & 63, gene.memory)
            position = new_position(direction, position)
            path += " " + direction
            if not is_in_map(position, parameters.size):
                break
            if is_on_treasure(position, parameters.treasures, found):
                found.append(copy.deepcopy(position))
                if found_all(found, parameters.number_of_treasures):
                    break
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
    subjects[number_of_subject].path = copy.deepcopy(path)
    return calculate_fitness(steps, found, parameters.treasures, path)


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


def add_new_blood(subjects):
    memory = generate_memory()
    subject = Memory(-1, [], copy.deepcopy(memory))
    subjects.append(subject)
    return subjects


def crossover(subjects, dad, mom, mutation_rate):
    memory = []
    ancester = dad
    for i in range(64):
        if i % 4:
            if ancester == mom:
                ancester = dad
            else:
                ancestor = mom
        if randint(1, 100) <= mutation_rate:
            mutant = randint(0,256)
            memory.append(mutant)
        else:
            memory.append(ancester.memory[i])
    child = Memory(-1, [], memory)
    subjects.append(child)
    return subjects


def keep_winner(subjects, winner):
    subjects.append(copy.deepcopy(winner))
    subjects[len(subjects) - 1].path = ""
    subjects[len(subjects) - 1].fitness = -1


def fight(sample):
    sample.sort(key=lambda x: x.fitness, reverse = True)
    return sample


def tournament(subjects, population, mutation):
    counter = 0
    x = len(subjects)
    for i in range(10):
        sample = x - population + counter
        subjects[sample: sample + 10] = fight(subjects[sample: sample + 10])
        keep_winner(subjects, subjects[sample])
        for j in range (8):
            dad = randint(0, population - 1)
            mom = randint(0, population - 1)
            if mom == dad:
                mom = population - dad
            subjects = crossover(subjects, subjects[x - population + dad], subjects[x - population + mom], mutation)
        counter += round(population / 10)
        add_new_blood(subjects)
    return subjects


def roulette():
    return


def reproduction(subjects, population, mutation):
    return tournament(subjects, population, mutation)
    return  roulette()


def evaluate_population(population, parameters_of_map, mutation):
    generation = 1
    subjects = []
    for i in range(population):
        add_new_blood(subjects)
    while generation:
        for i in range(population):
            fitness = start_finding(subjects, parameters_of_map, population*(generation-1)+i)
            subjects[population * (generation - 1) + i].fitness = fitness
            if fitness > parameters_of_map.number_of_treasures - 1:
                return
        print("************* GENERATION = ", generation, "*************\n\n\n")
        generation += 1
        subjects = reproduction(subjects, population, mutation) # nova generacia


def main():
    file = open('test3.txt', 'r')
    Lines = file.readlines()
    info = Lines[0].split(" ")
    size = int(info[0])
    number_of_treasures = int(info[1])
    population = int(info[2])
    mutation_rate = int(info[3])

    map = [[0 for _ in range(size)] for _ in range(size)]
    start, treasures = make_map(map, Lines, size)
    file.close()
    parameters_of_map = Map(size, start, treasures, number_of_treasures, map)
    evaluate_population(population, parameters_of_map, mutation_rate)


main()

#TODO veci zo stranky