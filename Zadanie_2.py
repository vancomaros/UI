from pprint import pprint
import copy


class Struct(object):
    def __init__(self, c=None, x=0, y=0):
        if c is None:
            c = [[], []]
        self.chessboard = c
        self.x = x
        self.y = y


def find_path(queue, border):
    counter = 0
    while True:
        Node = queue.pop(0)
        board = Node.chessboard
        if board[Node.x][Node.y] == border * border:
            pprint(board)
            print(counter, "Jumps!")
            return
        for i in range(-2, 3):
            if i and 0 <= Node.x + i < border:
                for j in range(-2, 3):
                    if j and abs(i) != abs(j) and 0 <= Node.y + j < border:
                        if board[Node.x + i][Node.y + j] == 0:
                            newBoard = copy.deepcopy(board)
                            newBoard[Node.x + i][Node.y + j] = board[Node.x][Node.y] + 1
                            newNode = Struct(newBoard, Node.x + i, Node.y + j)
                            queue = [newNode] + queue
                            counter += 1


def main():
    x = int(input("Dlzka hrany: "))

    arr = [[0 for i in range(x)] for j in range(x)]
    arr[x-1][0] = 1
    start = Struct(arr, x-1, 0)
    queue = [start]

    pprint(arr)
    find_path(queue, x)


main()
