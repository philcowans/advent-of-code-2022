def find_unique_string(f, length=None):
    buffer = []
    characters_read = 0
    while True:
        c = f.read(1)
        characters_read += 1
        if not c:
            raise RuntimeError('Reached end of file without a match')
        if len(buffer) == length:
            buffer = buffer[1:]
        buffer.append(c)
        if len(set(buffer)) == length:
            return characters_read

with open('input') as f:
    answer1 = find_unique_string(f, length=4)
    print(f'Answer to part 1: {answer1}')
    f.seek(0)
    answer2 = find_unique_string(f, length=14)
    print(f'Answer to part 2: {answer2}')
