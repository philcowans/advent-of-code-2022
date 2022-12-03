
#0 = rock
#1 = paper
#2 = scissors

scores = {}

for opponents_move in range(3):
    for desired_outcome in range(3):
        your_move = (opponents_move + desired_outcome - 1) % 3
        print(f'{opponents_move}, {desired_outcome}, {your_move}')
        score = 3 * desired_outcome + your_move + 1
        opponents_symbol = 'ABC'[opponents_move]
        your_symbol = 'XYZ'[desired_outcome]
        scores[f'{opponents_symbol} {your_symbol}\n'] = score

print(scores)

with open('/tmp/input2') as f:
    print(sum([scores[line] for line in f]))

