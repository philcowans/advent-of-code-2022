import re

class StackSet:
    stack_spec_re = re.compile('\[(.)\]')

    def _parse_stack_spec_line(self, l):
        num_stacks = (len(l) + 1) // 4
        for i in range(num_stacks):
            stack_spec = l[i*4:i*4+3]
            if m := self.stack_spec_re.match(stack_spec):
                self._stacks[self._stack_labels[i]].insert(0, m[1])

    def _parse_stack_labels(self, l):
        num_stacks = (len(l) + 1) // 4
        self._stack_labels = [l[i*4 + 1] for i in range(num_stacks)]
        self._stacks = {l: [] for l in self._stack_labels}

    def parse_header(self, lines):
        self._parse_stack_labels(lines[-1])
        for l in lines[:-1]:
            self._parse_stack_spec_line(l)

    def transfer(self, count, src, dest):
        raise NotImplementedError

    def top_of_each_stack(self):
        return [self._stacks[i][-1] for i in self._stack_labels]

class Scenario1StackSet(StackSet):
    def transfer(self, count, src, dest):
        for i in range(count):
            self._stacks[dest].append(self._stacks[src].pop())

class Scenario2StackSet(StackSet):
    def transfer(self, count, src, dest):
        self._stacks[dest] += self._stacks[src][-count:]
        self._stacks[src] = self._stacks[src][:-count]

def strip_lines(f):
    for line in f:
        yield line[:-1]

stack_sets = [
    Scenario1StackSet(),
    Scenario2StackSet(),
]    

move_line_re = re.compile('move ([0-9]+) from ([0-9]+) to ([0-9]+)')

in_header = True
header = []

with open('input') as f:
    for line in strip_lines(f):
        if in_header:
            if line == '':
                for s in stack_sets:
                    s.parse_header(header)
                in_header = False
            else:
                header.append(line)
        else:
            if m := move_line_re.match(line):
                for s in stack_sets:
                    s.transfer(int(m[1]), m[2], m[3])

print(''.join(stack_sets[0].top_of_each_stack()))
print(''.join(stack_sets[1].top_of_each_stack()))
