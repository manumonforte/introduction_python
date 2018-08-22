# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 20:26:29 2018

@author: Manu

Console Game TIC TAC TOE
"""
# -*- coding: utf-8 -*-
from collections import deque

turn = deque(["O", "X"])

board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]


def process_position(position):
    fila, columna = position.split(",")
    return int(fila) - 1, int(columna) - 1


def valid_position(position):
    if 0 <= position[0] <= 2 and 0 <= position[1] <= 2:
        if board[position[0]][position[1]] == " ":
            return True
    return False

def refreshBoard(position, player):
    board[position[0]][position[1]] = player


def win(j):
    if board[0] == [j, j, j] or board[1] == [j, j, j] or board[2] == [j, j, j]:
        return True
    elif board[0][0] == j and board[1][0] == j and board[2][0] == j:
        return True
    elif board[0][1] == j and board[1][1] == j and board[2][1] == j:
        return True
    elif board[0][2] == j and board[1][2] == j and board[2][2] == j:
        return True
    elif board[0][0] == j and board[1][1] == j and board[2][2] == j:
        return True
    elif board[0][2] == j and board[1][1] == j and board[2][0] == j:
        return True
    return False


def draw():
    return set(board[0]).union(set(board[1])).union(set(board[2])) == set(["X", "O"])



def change_turn():
    turn.rotate()
    return turn[0]


def show_board():
    print("")
    for row in board:
        print([square for square in row])


def game():
    player = change_turn()
    while True:
        position_str = input("Player {}, Choose a position (row,column 1 - 3). 'exit' for exit: ".format(player))
        if position_str == "exit":
            print("Thx for playing!")
            break
        try:
            position_process = process_position(position_str)
        except:
            print("Error, position {} invalid. The format must be (row, column)".format(position_str))
            continue
        if valid_position(position_process):
            refreshBoard(position_process, player)
            show_board()
            if win(player):
                print("Player {} has won!.".format(player))
                break
            if draw():
                print("Empate!.\n")
                break
            player = change_turn()
        else:
            print("Position {} invalid".format(position_str))

#%%
if __name__ == "__main__":
    game()

