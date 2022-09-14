import numpy as np

TIMESTEPS = 5
STREET_LENGTH = 10
START_AT = 0
p = 0.5 # probability of steping to the right

char = '_'
output = STREET_LENGTH*[char] +['[t=0]']
output[START_AT] = '🤑'
position = START_AT

for t in range(1, TIMESTEPS+1):
    rand_num = np.random.random()
    if p < rand_num and position != STREET_LENGTH:
        output[position+1], output[position] = output[position], output[position+1]
        position += 1
    elif p > rand_num and position != 0:
        output[position-1], output[position] = output[position], output[position-1]
        position -= 1
    print("".join(output))