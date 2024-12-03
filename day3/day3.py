import re

def find_multiplication_operations(file):
    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    return re.findall(pattern, file)

def find_multiplicaton_or_skip_operatins(file):
    pattern = r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)'
    return re.findall(pattern, file)

def atoi(num_str):
    return int("".join(a for a in num_str if a.isdigit()))

def execute_multiplication(mul_str, skip=False):
    if skip: return 0
    a, b = mul_str.split(",")
    return atoi(a)*atoi(b)

def main():
    with open("input.txt", "r") as input:
        RAW_INPUT = input.read()
    day3_part1 = sum([execute_multiplication(m) for m in find_multiplication_operations(RAW_INPUT)])

    instructions = find_multiplicaton_or_skip_operatins(RAW_INPUT)
    skip = False
    day3_part2 = 0
    for instruction in instructions:
        match instruction:
            case "do()":
                skip = False
                print(instruction)
            case "don't()":
                skip = True
                print(instruction)
            case _:
                day3_part2 += execute_multiplication(instruction, skip)
    print(day3_part1)
    print(day3_part2)
    
if __name__ == "__main__":
    main()