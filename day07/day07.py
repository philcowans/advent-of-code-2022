def strip_lines(f):
    for line in f:
        yield line.strip()

active_command = None
path = []
command_output = []

directory_sizes = {}

def increment_directory_size(path, size, directory_sizes=None):
    if path not in directory_sizes:
        directory_sizes[path] = 0
    directory_sizes[path] += size

def process_directory_output(output, path, directory_sizes=None):
    for line in output:
        if line.split(' ')[0] == 'dir':
            continue
        file_size = int(line.split(' ')[0])
        path_fragment = '/'
        increment_directory_size(path_fragment, file_size, directory_sizes=directory_sizes)
        for p in path:
            path_fragment += (p + '/')
            increment_directory_size(path_fragment, file_size, directory_sizes=directory_sizes)

def process_command_output(active_command, command_output, path, directory_sizes=None):
        if active_command is None:
            pass
        elif active_command == 'ls':
            process_directory_output(command_output, path, directory_sizes=directory_sizes)
        elif active_command == 'cd':
            pass
        else:
            raise RuntimeError(f'Unexpected state, processing output for unknown command {active_command}')

with open('input') as f:
    for line in strip_lines(f):
        if line[0] == '$': # Command
            process_command_output(active_command, command_output, path, directory_sizes=directory_sizes)
            argv = line[2:].split(' ')
            command_output = []
            active_command = argv[0]
            if argv[0] == 'cd':
                if argv[1] == '/':
                    path = []
                elif argv[1] == '..':
                    path.pop()
                else:
                    path.append(argv[1])
            elif argv[0] == 'ls':
                pass
            else:
                raise RuntimeError(f'Command {argv[0]} not known.')
        else:
            command_output.append(line)
    process_command_output(active_command, command_output, path, directory_sizes=directory_sizes)

print(sum([directory_sizes[path] for path in directory_sizes if directory_sizes[path] <= 100000]))

free_space = 70000000 - directory_sizes['/']
required_size = 30000000 - free_space
print(min([directory_sizes[path] for path in directory_sizes if directory_sizes[path] >= required_size]))
