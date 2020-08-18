#dimensions of the board
import random
import numpy as np
import time

HEIGHT = 10
WIDTH = 10


def dead_state():
    #list = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
    list = np.zeros(shape = (HEIGHT, WIDTH), dtype = int)
    return list

def is_alive(cell, i, j):
    if cell[i][j] == 1:
        return True
    else:
        return False

def initial_state():
    initial = dead_state()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if random.random() > 0.5 :
                initial[i][j] = 1
            else: 
                initial[i][j] = 0 
    return initial

def change_state(cell, i, j):
    #if cell is Alive
    state = cell
    sum = 0 
    #Exception for index error
    try:
        sum = (state[i-1][j-1] + state[i-1][j] + state[i-1][j+1] + state[i][j-1] +
        state[i][j] +state[i][j+1]+ state[i+1][j+1] + state[i+1][j+1] + state[i+1][j+1])

    except IndexError:
        state[i][j] = 0

    if is_alive(state,i ,j) and (sum == 0 or sum == 1):
        return True

    elif is_alive(state,i ,j) and (sum == 2 or sum == 3):
        return False

    elif is_alive(state,i ,j) and (sum > 3):    
        return True

    elif not(is_alive(state,i ,j)) and (sum == 3) :
        return True
    else:
        return False

def next_state(previous_state):
    new_state = previous_state

    #for each cell in previous state
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if(change_state(new_state, i, j) == True):
                if new_state[i][j] == 1:
                    new_state[i][j] == 0
                else:
                    new_state[i][j] == 1        

    return new_state


def render_board(state):
    cell =  state
    #print the top border
    print('+' + WIDTH * '--' + '+')

    #print the rest of the board
    for i in range(HEIGHT):
        print("|", end = '')
        for j in range(WIDTH):
            if is_alive(cell, i, j):
                print('# ', end = '')
            elif not(is_alive(cell, i, j)):
                print('  ', end = '')
        print("|", end ='')
        print()

    #print the bottom border
    print('+' + WIDTH * '--' + '+')


if __name__ == '__main__':
    #initialize the empty state
    old_state = initial_state()

    condition = True

    render_board(old_state)

    new = next_state(old_state)

    render_board(new)

    # #Run forever
    # while(condition):
    #     #print the state
    #     render_board(old_state)
    #     new_state = next_state(old_state)
    #     time.sleep(0.5)
    #     render_board(new_state)
    #     old_state = new_state
        
                