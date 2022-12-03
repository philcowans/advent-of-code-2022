def priority(lines):
    print(lines)
    overlap = set(lines[0])
    for line in lines[1:]:
        overlap = overlap & set(line)
    overlap = list(overlap)[0]
    if ord(overlap) >= ord('a'):
        return ord(overlap) - ord('a') + 1
    else:
        return ord(overlap) - ord('A') + 27

with open('/tmp/input3') as f:
    lines = f.read().split('\n')[:-1]
    print(sum([priority(lines[i*3:i*3+3]) for i in range(len(lines) // 3)]))
