with open('input') as f:
    data = [[int(c) for c in l.strip()] for l in f]

def find_distances(row):
    accumulators = [0] * 10
    accumulators2 = [0] * 10
    r = ([], [])
    for height in row:
        r[0].append(accumulators[height])
        r[1].append(accumulators2[height])
        for i in range(10):
            if i <= height:
                accumulators[i] = 0
                accumulators2[i] = 1
            else:
                accumulators[i] += 1
                accumulators2[i] += 1
    return r

def transpose(d):
    iterators = [iter(row) for row in d]
    r = []
    try:
        while True:
            r.append([next(it) for it in iterators])
    except StopIteration:
        return r

left = [find_distances(row)[0] for row in data]
right = [list(reversed(find_distances(list(reversed(row)))[0])) for row in data]
top = transpose([find_distances(row)[0] for row in transpose(data)])
bottom = transpose([list(reversed(find_distances(list(reversed(row)))[0])) for row in transpose(data)])

left2 = [find_distances(row)[1] for row in data]
right2 = [list(reversed(find_distances(list(reversed(row)))[1])) for row in data]
top2 = transpose([find_distances(row)[1] for row in transpose(data)])
bottom2 = transpose([list(reversed(find_distances(list(reversed(row)))[1])) for row in transpose(data)])

count = 0
scores = [[0 for j in i] for i in data]

for i in range(len(data)):
    for j in range(len(data[0])):
        if (left[i][j] == j) or (right[i][j] == len(data[0]) - 1 - j) or (top[i][j] == i) or (bottom[i][j] == len(data) - 1 - i):
            count += 1
        scores[i][j] = left2[i][j] * right2[i][j] * top2[i][j] * bottom2[i][j]

print(count)
print(max([max(row) for row in scores]))
