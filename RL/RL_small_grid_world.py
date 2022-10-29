#In[]
import numpy as np
grid_height =4
grid_width = grid_height
epoch = 100
action = [0, 1, 2, 3]



def get_state(state, action):
    
    action_grid = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    state[0]+=action_grid[action][0]
    state[1]+=action_grid[action][1]
    
    if state[0] < 0 :
        state[0] = 0
    elif state[0] > 3 :
        state[0] = 3
    
    if state[1] < 0 :
        state[1] = 0
    elif state[1] > 3 :
        state[1] = 3
    
    return state[0], state[1]



policy = np.empty([grid_height, grid_width, len(action)], dtype=float) ## make action policy
for i in range(grid_height):
    for j in range(grid_width):
        for k in range(len(action)):
            if i==j and ((i==0) or (i==3)):
                policy[i][j]=0.00
            else :
                policy[i][j]=0.25
policy[0][0] = [0] * grid_width
policy[3][3] = [0] * grid_width

policy_table = np.zeros([grid_height, grid_width], dtype=float) ## value table declaration
for tmp in range(epoch):
    policy_update_table = np.zeros([grid_height, grid_width], dtype=float) ## update table declaration
    for j in range(grid_width):
        for i in range(grid_height):
            if i==j and (i==0 or i==3):
                continue
            else:
                value_tmp = 0
                for act in action:
                    i_, j_ = get_state([i,j], act)
                    value = policy[i][j][act] * (-1 + 1 * policy_table[i_][j_])
                    value_tmp += value
            policy_update_table[i][j] = round(value_tmp, 3)
    policy_table = policy_update_table
print("\n\nRESULT")
for line in policy_table:
    for item in range(4):
            line[item] = np.round(line[item],4) #round
    print(line)
    



value_table = np.zeros([grid_height, grid_width], dtype=float) #value table declaration
for tmp in range(epoch):
    value_update_table = np.zeros([grid_height, grid_width], dtype=float) ## update table declaration
    for j in range(4): 
        for i in range(4):
            if i==j and (i==0 or i==3):
                continue
            else : 
                tmp = []
                for act in action:
                    i_, j_ = get_state([i,j], act)
                    value = (-1 + 1*value_table[i_][j_])
                    tmp.append(value)
                value_table[i][j] = max(tmp)

print("\n\nRESULT")
for line in value_table:
    for item in range(4):
            line[item] = round(line[item],4)
    print(line)

# %%
''' 
Chad 🐶  ~/Documents/workspace/git/study
 /usr/bin/python3 /Users/gimdongju/Documents/workspace/git/study/RL/RL_small_grid_world.py


RESULT
[  0.    -13.942 -19.915 -21.905]
[-13.942 -17.925 -19.916 -19.915]
[-19.915 -19.916 -17.925 -13.942]
[-21.905 -19.915 -13.942   0.   ]


RESULT
[ 0. -1. -2. -3.]
[-1. -2. -3. -2.]
[-2. -3. -2. -1.]
[-3. -2. -1.  0.]
'''