from main import *

#dead cells with no live neighbors should stay dead
init_state1 = np.array([[0,0,0],[0,0,0],[0,0,0]])
expected_next_state1 = np.array([[0,0,0],[0,0,0],[0,0,0]])
actual_next_state1 = next_state(init_state1)

if np.all(expected_next_state1 == actual_next_state1):
    print("Passed")
else:
    print("Failed")

#dead cells with 3 alive neighbors will come alive
init_state2 = np.array([
            [0,0,1],
            [0,1,1],
            [0,0,0]
            ])
expected_next_state2 = np.array([
            [0,1,1],
            [0,1,1],
            [0,0,0]
            ])

actual_next_state2 = next_state(init_state2)
if np.all(actual_next_state2 == expected_next_state2):
    print("Passed")
else:
    print("Failed")