import numpy as np
from random import random
import string

#height and width of the board
WIDTH = 20
HEIGHT = 10

def dead_state(w= HEIGHT, h= WIDTH):
    new_arr = np.zeros(shape=(w,h), dtype = int)
    return new_arr

def random_state():
    #Initializing a board of empty cells
    initial_state = dead_state()

    #Randomising state of the cells to either 0 or 1
    for i in range(len(initial_state)):
        for j in range(len(initial_state[0])):
            seed = random()
            if seed >= 0.5:
                initial_state[i][j] = 0
            else:
                initial_state[i][j] = 1

    return initial_state

def render_state(state):
    new_arr = np.zeros(shape=(len(state), len(state[0])), dtype = str)
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i, j] == 0:
                new_arr[i][j] = '.'
            else:
                new_arr[i][j] = '#'
    return new_arr



def print_board(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print('|' + arr[i][j] + '|', end ='')
        print()        

def update_state(initial_state):
    new_state = initial_state
    for i in range(len(new_state)):
        for j range(len(new_state[0])):
            if ()(update_cell_state(initial_state[i][j]) == True):
                new_state[i][j] = 



def update_cell_state(cell):
    if cell == 1:
        cell_alive = True
        try:
        sum =(cell[i-1][j-1]+ cell[i-1][j] + cell[i-1][j+1] + cell[i][j-1]+ cell[i][j] + cell[i][j+1] +cell[i+1][j-1]+ cell[i+1][j] + cell[i+1][j+1])
        except IndexError:
            cell[i][j] = 0
        
        if (cell_alive == True) AND (sum <= 1):
            cell_next_state = False
        elif (cell_alive == True) AND (sum == 2 OR sum == 3):
            cell_next_state = True 
        elif (cell_alive == True) AND (sum > 3):
            cell_next_state = False
    elif cell == 0:
        cell_alive = False
        try:
        sum =(cell[i-1][j-1]+ cell[i-1][j] + cell[i-1][j+1] + cell[i][j-1]+ cell[i][j] + cell[i][j+1] +cell[i+1][j-1]+ cell[i+1][j] + cell[i+1][j+1])
        except IndexError:
            cell[i][j] = 0

        if(cell_alive == False) AND (sum == 3):
            cell_next_state = True        
    

    return cell_next_state    







board1 = random_state()
board2 = dead_state()

rendered1 = render_state(board1)
rendered2 = render_state(board2)

print_board(rendered1)


    