from itertools import permutations
from pprint import pprint


# steps urcuje, ci sa bude krokovat, alebo sa pojde rovno do konca
steps = 0


def init():
    global steps
    x = input('fiat/family\n').split(' ')
    file = open(x[0] + '_facts.txt', 'r')
    Lines = file.readlines()
    facts = readFile(Lines)
    file = open(x[0] + '.txt', 'r')
    Lines = file.readlines()
    rules = readFile(Lines)

    steps = int(x[1])
    family(rules, facts)
    pprint(facts)


# nacitanie suborov do listov
def readFile(file):
    facts = []
    for i in file:
        facts.append(i.replace("\n", ""))
    return facts


# z kazdeho pravidla si nacitam pocet premennych a z faktov mena
# urobim permutacie na mena podla poctu premennych
# pravidla preskumavam pokial vznikaju nove fakty
def family(rules, facts):
    messages = []
    names = get_names(facts)
    while 1:
        old = len(facts)
        for rule in rules:
            variables = read_rule(rule)
            names_permutations = permutations(names, len(variables))
            explore_rule(rule, list(names_permutations), variables, facts, messages)
        if len(facts) == old:
            pprint(messages)
            break


# zistim pocet mien vo faktoch
def get_names(facts):
    names = []
    for fact in facts:
        for word in fact.split(" "):
            if 'A' <= word[0] <= 'Z':
                if word not in names:
                    names.append(word)
    return names


# zistim pocet premennych v pravidle
def read_rule(rule):
    variables = []
    for part in rule.split(", "):
        for word in part.split(" "):
            word = word.replace(';', "")
            if word[0] == '?' and word not in variables:
                variables.append(word)
    return variables


# dosadzujem mena do pravidiel
def explore_rule(rule, names, variables, facts, messages):
    new_rule = rule
    for i in range(len(names)):
        for name in range(len(names[0])):
            new_rule = new_rule.replace(variables[name], names[i][name])
        check_correctness(new_rule, facts, messages)
        new_rule = rule


# preskumam spravnost pravidiel s dosadenymi menami
def check_correctness(rule, facts, messages):
    match = 0
    new_rule = rule.split(", ")
    for i in range(len(new_rule) - 1):
        for fact in facts:
            if fact == new_rule[i]:
                match += 1
                break
    if match == len(new_rule) - 1:
        process_new_fact(new_rule[len(new_rule) - 1].split("; "), facts, messages)


# pravidlo platilo, vzkonam akcie
def process_new_fact(new_fact, facts, messages):
    for actions in new_fact:
        if actions[0:6] == 'pridaj':
            add_new_fact(actions.replace("pridaj ", ""), facts)
        elif actions[0:5] == 'vymaz':
            delete_fact(actions.replace("vymaz ", ""), facts)
        elif actions[0:6] == 'sprava' and actions[7:] not in messages:
            messages.append(actions[7:])


def add_new_fact(new_fact, facts):
    global steps
    if new_fact not in facts:
        if steps == 1:
            print(new_fact)
            steps = int(input('1 = next step, 2 = finish\n'))
        facts.append(new_fact)


def delete_fact(fact, facts):
    if fact in facts:
        facts.remove(fact)


init()
