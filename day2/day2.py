import itertools
import functools

def count_safe_codes(code_block, tolerance, funcs):
    counter = 0
    for line in code_block:
        entries = line_to_entries(line)
        if any(all_with_tolerance(entries, f, tolerance=tolerance) for f in funcs):
            counter += 1
    return counter

def line_to_entries(line):
    # Convert "'1' '2' '3'" to [1,2,3]
    return [int(e) for e in line.split()]

def is_gradual_ascending(input, delta_min, delta_max):
    # Check if the list is gradually ascending with differences between -4 and 0
    return all((-1)*delta_max <= input[i] - input[i+1] <= (-1)*delta_min for i in range(len(input) - 1))


def is_gradual_descending(input, delta_min = 1, delta_max = 3):
    # Check if the list is gradually descending with differences between 0 and 4
    return all(delta_min <= input[i] - input[i+1] <= delta_max for i in range(len(input) - 1))

def all_with_tolerance(input, func, tolerance=0):
    # Generate all subsets of the list by removing 'tolerance' number of elements
    # and check if any subset satisfies the given function 'func'
    t = max(len(input)-tolerance, 0) # defaults to no tolerance. 
    return any(func(l) for l in itertools.combinations(input, t))

def main():
    with open("input.txt", "r") as input:
        RAW_INPUT = input.readlines()

    is_gradual_ascending_1_3 = functools.partial(is_gradual_ascending, delta_min=1, delta_max=3)
    is_gradual_descending_1_3 = functools.partial(is_gradual_descending, delta_min=1, delta_max=3)
    day2_part1 = count_safe_codes(code_block=RAW_INPUT, tolerance=0, funcs=[is_gradual_ascending_1_3, is_gradual_descending_1_3])
    day2_part2 = count_safe_codes(code_block=RAW_INPUT, tolerance=1, funcs=[is_gradual_ascending_1_3, is_gradual_descending_1_3])
    print(day2_part1)
    print(day2_part2)

if __name__ == "__main__":
    main()