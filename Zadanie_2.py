from pprint import pprint
from random import randint
import copy


# V strukture si pamatam sachovnicu s aktualnym ohodnetenim
# poli a momentalnu poziciu jazdca na tej sachovnici
class Struct(object):
    def __init__(self, c=None, x=0, y=0, o=None):
        if c is None:
            c = [[], []]
        if o is None:
            o = [[]]
        self.chessboard = c
        self.x = x
        self.y = y
        self.output = o


def find_path(queue, border):
    # Pocitadlo skokov konika
    counter = 0

    while True:

        # Prazdna queue = Riesenie neexistuje
        if not queue or (border == 5 and counter > 600000):
            print('Nema riesenie!')
            print()
            return

        # Vytiahnem z queue prvy prvok,
        # z neho budem hladat dalsiu cestu
        Node = queue.pop()
        board = Node.chessboard

        # Ak su ocislovane vsetky pozicie, koncim
        if board[Node.x][Node.y] == border * border:
            pprint(board)
            print(Node.output)
            print(counter, "Jumps!")
            print()
            return

        # Jazdec sa pohybuje max o 2 polia do vsetkych smerov
        # Nemoze sa hybat po osiach priamo, preto i, j nemoze byt 0
        # a takisto nemozu byt rovnake, inak by sa spraval aj ako strelec ;-)
        for i in range(-2, 3):
            if i and 0 <= Node.x + i < border:
                for j in range(-2, 3):
                    if j and abs(i) != abs(j) and 0 <= Node.y + j < border:
                        if board[Node.x + i][Node.y + j] == 0:
                            newBoard = copy.deepcopy(board)
                            newBoard[Node.x + i][Node.y + j] = board[Node.x][Node.y] + 1
                            newOutput = copy.deepcopy(Node.output)
                            newOutput += " -> [" + str(Node.x + i) + "][" + str(Node.y + j) + "]"
                            newNode = Struct(newBoard, Node.x + i, Node.y + j, newOutput)
                            queue = queue + [newNode]
                            counter += 1

    # Pokial existuje legalny skok, vyvtori sa nova sachovnica s novym ohodnotenim.
    # Takisto si zapamatam nove suradnice jazdca a tieto idaje ulozim do Struct
    # Nasledne to vsetko pridam na zaciatok queue, aby sa prehladavalo do hlbky


def main():
    x = 5

    while x < 7:

        for i in range(5):

            arr = [[0 for _ in range(x)] for _ in range(x)]

            # Pozicie su nahodne generovane, okrem prvej
            if i > 0:
                position_x = randint(0, x - 1)
                position_y = randint(0, x - 1)
                print("Start = [" + str(position_x) + "][" + str(position_y) + "]")
            else:
                position_x = x - 1
                position_y = 0
                print("Zaciatok vlavo dole: [" + str(position_x) + "][" + str(position_y) + "]")

            arr[position_x][position_y] = 1
            start = Struct(arr, position_x, position_y, "[" + str(position_x) + "][" + str(position_y) + "]")
            queue = [start]

            pprint(arr)
            print()
            find_path(queue, x)
            queue.clear()

        x += 1


main()
