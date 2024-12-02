from collections import defaultdict

with open("input.txt", "r") as input:
    RAW_INPUT = input.readlines()

partial_list_A, partial_list_B = zip(*[(int(line.split()[0]), int(line.split()[1])) for line in RAW_INPUT])

partial_list_A = sorted(partial_list_A)
partial_list_B = sorted(partial_list_B)
diff = [abs(x - y) for x, y in zip(partial_list_A, partial_list_B)]

bag = defaultdict(int)
for k in partial_list_B:
    bag[k] += 1

def main():
    day1_part1 = sum(diff)
    day1_part2 = sum([bag[e]*e for e in partial_list_A])
    print(day1_part1)
    print(day1_part2)

if __name__ == "__main__":
    main()