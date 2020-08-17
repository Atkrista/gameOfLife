import numpy as np
from random import random
import string

#height and width of the board
WIDTH = 10
HEIGHT = 10

def dead_state(w= WIDTH, h= HEIGHT):
    new_arr = np.zeros(shape=(w,h),dtype = int)
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
    new_arr = np.zeros((len(state), len(state[0])), dtype = str)
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i, j] == 0:
                np.put(new_arr[i], j, '.' )
            else:
                np.put(new_arr[i], j, '#')             
    return new_arr



def print_state(arr):
    print(arr)
    

board1 = random_state()
board2 = dead_state()

rendered1 = render_state(board1)
rendered2 = render_state(board2)

#print(rendered1)
print(board2)

