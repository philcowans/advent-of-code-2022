def priority(line):
    overlap = list(set(line[:len(line)//2]) & set(line[len(line)//2:]))[0]
    if ord(overlap) >= ord('a'):
        return ord(overlap) - ord('a') + 1
    else:
        return ord(overlap) - ord('A') + 27

with open('/tmp/input3') as f:
    print(sum([priority(line.strip()) for line in f]))
