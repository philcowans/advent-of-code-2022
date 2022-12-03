def strip_lines(it):
    for i in it:
        yield i.strip()

def group_with_separator(it):
    accumulator = []
    for i in it:
        if i == '':
            yield accumulator
            accumulator = []
        else:
            accumulator.append(i)
    yield accumulator

def to_int(it):
    for i in it:
        yield int(i)

def top_n(it, n):
    max_values = [0] * n
    for i in it:
        if i > max_values[0]:
            max_values = sorted(max_values + [i])[1:]
    return max_values

with open('input') as f:
    answer1 = sum(top_n([sum(to_int(group)) for group in group_with_separator(strip_lines(f))], 1))
    print(f'Answer to part 1: {answer1}')
    f.seek(0)
    answer2 = sum(top_n([sum(to_int(group)) for group in group_with_separator(strip_lines(f))], 3))
    print(f'Answer to part 2: {answer2}')
