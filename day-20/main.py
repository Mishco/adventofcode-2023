import operator
import re
from collections import defaultdict
from functools import reduce


def ints(s):
    return list(map(int, re.findall(r'\d+', s)))


# Flip-flop modules (prefix %) are either on or off;
# they are initially off. If a flip-flop module receives a high pulse,
# it is ignored and nothing happens.
# However, if a flip-flop module receives a low pulse,
# it flips between on and off. If it was off, it turns on and sends a high pulse.
# If it was on, it turns off and sends a low pulse.

# Conjunction modules (prefix &) remember the type of the most recent pulse
# received from each of their connected input modules; they initially default to remembering
# a low pulse for each input. When a pulse is received, the conjunction module first updates
# its memory for that input. Then, if it remembers high pulses for all inputs,
# it sends a low pulse; otherwise, it sends a high pulse.


class Module:
    def __init__(self):
        self.pulse = None
        self.destinations = []

    def receive_pulse(self, pulse):
        self.pulse = pulse
        self.process_pulse()

    def process_pulse(self):
        pass


class FlipFlopModule(Module):
    def __init__(self):
        super().__init__()
        self.state = False

    def process_pulse(self):
        if self.pulse == 0:
            self.state = not self.state
            if self.state:
                self.send_pulse(1)
            else:
                self.send_pulse(0)

    def send_pulse(self, pulse):
        for module in self.destinations:
            module.receive_pulse(pulse)


class ConjunctionModule(Module):
    def __init__(self, num_inputs):
        super().__init__()
        self.num_inputs = num_inputs
        self.memories = [0] * num_inputs

    def process_pulse(self):
        input_index = self.sources.index(self.pulse[1])
        self.memories[input_index] = self.pulse[0]
        if all(memory == 1 for memory in self.memories):
            self.send_pulse(0)
        else:
            self.send_pulse(1)

    def send_pulse(self, pulse):
        for module in self.destinations:
            module.receive_pulse((pulse, self))


class Broadcaster(Module):
    def __init__(self):
        super().__init__()

    def process_pulse(self):
        self.send_pulse(self.pulse)

    def send_pulse(self, pulse):
        for module in self.destinations:
            module.receive_pulse(pulse)


# There is a single broadcast module (named broadcaster).
# When it receives a pulse, it sends the same pulse to all of its destination modules.

# Here at Desert Machine Headquarters,
# there is a module with a single button on it called, aptly,
# the button module. When you push the button, a single low pulse is sent directly to the broadcaster module.


# data = open('sample').read().strip().splitlines()
# print(data)
data = open('../inputs/day20.txt').read().strip().splitlines()
# = 0
count_item = 0

button = Module()
broadcasters = []

all_modules = dict()
flipflops = defaultdict(int)
conjuctions = defaultdict(dict)
rx = None
for line in data:
    source, _, *dest = line.replace(',', '').split()
    source_name = source.lstrip('%&')

    operand, source = (source[0], source[1:]) if source[0] in '%&' else ('', source)

    all_modules[source] = operand, dest

    for d in dest:
        conjuctions[d][source] = 0
        if 'rx' in dest:
            rx = source

rx_ins = {i: 0 for i in conjuctions[rx]}
presses = 0
counts = [0, 0]
pulse_out = 0

for i in range(10000000):
    # found all RX pulses
    if all(rx_ins.values()):
        break
    presses += 1
    queue = [(None, 'broadcaster', 0)]
    while queue:
        source, module, pulse_in = queue.pop(0)
        counts[pulse_in] += 1

        if module not in all_modules:
            continue

        type_module, next_module = all_modules[module]
        match type_module, pulse_in:
            case '', _:
                pulse_out = pulse_in
            case '%', 0:
                pulse_out = flipflops[module] = not flipflops[module]
            case '&', _:
                conjuctions[module][source] = pulse_in
                pulse_out = not all(conjuctions[module].values())

                if 'rx' in next_module:
                    # for key, val in conjuctions[module].items():
                    #     if val:
                    #         rx_ins[key] = presses
                    rx_ins.update({k: presses for k, v in conjuctions[module].items() if v})
            case _, _:
                continue

        for n in next_module:
            queue.append((module, n, pulse_out))

print(counts)
res = reduce(operator.mul, counts, 1)
# math.prod(iterable, *, start=1)
# print(math.prod(counts))
print(f"part1: {res}")

print(rx_ins)
res = reduce(operator.mul, rx_ins.values(), 1)
print(f"part2: {res}")
# print(math.prod(rx_ins.values()))

# for i in data:
#     parts = i.split(' -> ')
#     source = parts[0]
#     destinations = parts[1].split(', ')
#     source_name = source.lstrip('%&')
#
#     if source == 'broadcaster':
#         module = Broadcaster()
#     elif source.startswith('%'):
#         module = FlipFlopModule()
#     elif source.startswith('&'):
#         num_inputs = len(destinations)
#         module = ConjunctionModule(num_inputs)
#
#     modules[source_name] = module

# for destination in destinations:
#     modules[destination].destinations.append(module)

# Create the connections between the modules
# for line in data:
#     parts = line.split(' -> ')
#     source = parts[0]
#     destinations = parts[1].split(', ')
#
#     source_name = source.lstrip('%&')
#
#     for destination in destinations:
#         try:
#             modules[destination].destinations.append(modules[source_name])
#         except:
#             print(destination, " not found")

# Push the button to start the simulation
# button = Module()
# button.receive_pulse(0)
#
# # start the seq
# button.destination_modules = count_item
# num_low_pulses = 0
# num_high_pulses = 0
# for i in range(1000):
#     num_low_pulses += 8
#     num_high_pulses += 4
#     # Push the button to start the simulation again
#     button.receive_pulse(0)
#
# total_pulses = num_low_pulses * num_high_pulses
#
# print("Total number of low pulses sent:", num_low_pulses)
# print("Total number of high pulses sent:", num_high_pulses)
# print("Total number of pulses sent:", total_pulses)
