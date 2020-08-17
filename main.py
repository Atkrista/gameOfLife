import numpy as np
from random import random
import string

#height and width of the board
WIDTH = 5
HEIGHT = 5

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
    #making a new empty array
    new_arr = np.zeros(shape=(len(state), len(state[0])), dtype = str)
    #Print '.' in board if cell state is 0, and '#' if cell state is 1
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i, j] == 0:
                new_arr[i][j] = '.'
            else:
                new_arr[i][j] = '#'
    return new_arr


#Muh Aesthetics!
def print_board(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print('|' + arr[i][j] + '|', end ='')
        print()        


#render new board state for next iteration of game of life
def next_board_state(previous_state):
    #creating a new dead state to append changes to
    new_state = dead_state()

    #Function that tells us if we change the state of an individual cell or nah
    def change_state(cell,i , j):
        #As some indexes will be out of bounds
        #Edge and corner cells dont have 8 neighbors
        sum = 0
        try:
            sum =(cell[i-1][j-1]+ cell[i-1][j] + cell[i-1][j+1] + cell[i][j-1]+ cell[i][j] + cell[i][j+1] +cell[i+1][j-1]+ cell[i+1][j] + cell[i+1][j+1])
        except IndexError:
            cell[i][j] = 0
        #change state if neighbors = 3 dead or alive
        if (sum > 3):
            return True


    for i in range(len(previous_state)):
        for j in range(len(previous_state[0])):
            if previous_state[i][j] == 1:
                if change_state(previous_state, i, j) == True:
                    new_state[i][j] = 0
            else:
                if change_state(previous_state, i, j)== True:
                    new_state[i][j] = 1
    return new_state

board1 = random_state()
board2 = next_board_state(board1)

rendered1 = render_state(board1)
rendered2 = render_state(board2)

print_board(rendered1)
print()
print()
print()
print_board(rendered2)


    