import numpy as np
import re

def truncate_diff(diff):
    for i in range(2):
        if diff[i] >= 1:
            diff[i] = 1
        elif diff[i] <= -1:
            diff[i] = -1
        else:
            diff[i] = 0

def count_tail_positions(f, l):
    move_re = re.compile('([UDLR]) ([0-9]+)')

    moves = {
        'U': np.array([0, 1]),
        'D': np.array([0, -1]),
        'L': np.array([-1, 0]),
        'R': np.array([1, 0]),
    }

    knots = [np.array([0, 0]) for i in range(l)]
    tail_positions = set(['0,0'])

    for line in f:
        if m:= move_re.match(line):
            for k in range(int(m[2])):
                knots[0] += moves[m[1]]
                for t in range(1, l):
                    diff = knots[t-1] - knots[t]
                    if max([abs(i) for i in diff]) > 1:
                        truncate_diff(diff)
                        knots[t] += diff
                tail_positions.add(','.join([str(x) for x in knots[-1]]))
    
    return(len(tail_positions))

with open('input') as f:
    print(count_tail_positions(f, 2))
    f.seek(0)
    print(count_tail_positions(f, 10))
