def ranges_from_line(line):
    return [[int(i) for i in r.split('-')] for r in line.strip().split(',')]

def is_subset(a, b):
    return a[0] >= b[0] and a[1] <= b[1]

def is_subset_or_superset(a, b):
    return is_subset(a, b) or is_subset(b, a)

def does_intersect(a, b):
    return a[0] <= b[1] and a[1] >= b[0]

with open('input') as f:
    ranges = [ranges_from_line(line) for line in f]

answer1 = sum([1 if is_subset_or_superset(r[0], r[1]) else 0 for r in ranges])
print(f'Answer to part 1: {answer1}')
answer2 = sum([1 if does_intersect(r[0], r[1]) else 0 for r in ranges])
print(f'Answer to part 2: {answer2}')
