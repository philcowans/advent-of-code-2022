
#0 = rock
#1 = paper
#2 = scissors

scores = {}

for opponents_move in range(3):
    for your_move in range(3):
        score = 3 * ((your_move - opponents_move) % 3 + 1) % 9 + your_move + 1
        opponents_symbol = 'ABC'[opponents_move]
        your_symbol = 'XYZ'[your_move]
        scores[f'{opponents_symbol} {your_symbol}\n'] = score

with open('/tmp/input2') as f:
    print(sum([scores[line] for line in f]))

