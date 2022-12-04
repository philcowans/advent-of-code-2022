def all_combinations():
    for a in range(3):
        for b in range(3):
            yield a, b

# If we define rock = 0, paper = 1 and scisors = 2, then the mod-3 arithmetic
# below computes the outcome with 0 = draw, 1 = win, 2 = lose

def compute_outcome(you, opponent):
    return (you - opponent) % 3

# This can then be inverted (mod-n arithmetic works just like normal integer
# arithmetic here).

def compute_you(opponent, outcome):
    return (outcome + opponent) % 3

def score(you, outcome):
    return 3 * ((outcome + 1) % 3) + you + 1

def symbol_opponent(opponent):
    return 'ABC'[opponent]

def symbol_2(you):
    return 'XYZ'[you]

def table_row(opponent, idx_2):
    return f'{symbol_opponent(opponent)} {symbol_2(idx_2)}\n'

# Precompute scores for each row type in each scheme

scores_scheme1 = {table_row(opponent, you): score(you, compute_outcome(you, opponent)) for opponent, you in all_combinations()}
scores_scheme2 = {table_row(opponent, (outcome + 1) % 3): score(compute_you(opponent, outcome), outcome) for opponent, outcome in all_combinations()}

with open('input') as f:
    answer1 = sum([scores_scheme1[line] for line in f])
    print(f'Answer to part 1: {answer1}')
    f.seek(0)
    answer2 = sum([scores_scheme2[line] for line in f])
    print(f'Answer to part 2: {answer2}')
