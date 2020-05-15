from itertools import permutations


def check_correctness(rule, facts):
    match = 0
    new_rule = rule.split(", ")
    for i in range(len(new_rule) - 1):
        for fact in facts:
            fact = fact.replace('\n', "")
            if fact == new_rule[i]:
                match += 1
                break
    if match == len(new_rule) - 1:
        new_rule[len(new_rule) - 1] = new_rule[len(new_rule) - 1].replace("pridaj ", "")
        new_fact = new_rule[len(new_rule) - 1].split("; ")
        facts.append(new_fact[0])
        if len(new_fact) > 1 and new_fact[1][0:6] == 'sprava':
            print(new_fact[1][6:])


def explore_rule(rule, names, variables, facts):
    new_rule = rule
    for i in range(len(names)):
        for name in range(len(names[0])):
            new_rule = new_rule.replace(variables[name], names[i][name])
        check_correctness(new_rule.replace('\n', ""), facts)
        new_rule = rule


def read_rule(rule):
    variables = []
    for part in rule.split(", "):
        for word in part.split(" "):
            if word[0] == '?' and word.replace('\n', "") not in variables \
                    and word.replace(';', "") not in variables:
                word = word.replace(';', "")
                variables.append(word.replace('\n', ""))
    return variables


def do_stuff(rules, facts):
    names = get_names(facts)

    for rule in rules:
        variables = read_rule(rule)
        names_permutations = permutations(names, len(variables))
        explore_rule(rule, list(names_permutations), variables, facts)


def get_names(facts):
    names = []
    for fact in facts:
        for word in fact.split(" "):
            if 'A' <= word[0] <= 'Z':
                if word.replace('\n', "") not in names:
                    names.append(word.replace('\n', ""))
    return names


def readFile(file):
    facts = []
    for i in file:
        facts.append(i)
    return facts


def init():
    file = open('facts.txt', 'r')
    Lines = file.readlines()
    facts = readFile(Lines)
    file = open('rules.txt', 'r')
    Lines = file.readlines()
    rules = readFile(Lines)

    do_stuff(rules, facts)


init()
