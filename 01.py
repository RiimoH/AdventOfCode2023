
def part_one(inp):
    def find_num(s: str):
        for char in s:
            if char.isdigit():
                first = char
                break
        for char in s[::-1]:
            if char.isdigit():
                second = char
                break
        return int(first + second)
    m = map(find_num, inp)
    return sum(m)


digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
}

def part_two(inp):

    def find_num(s: str):
            
        f_idx = 1000
        f_char= "0"

        l_idx = -1
        l_char= "0"

        for digit in digits:
            idx = s.find(digit)
            if idx < f_idx and idx >= 0:
                f_idx = idx
                f_char = digits[digit]
            idx = s.rfind(digit)
            if idx > l_idx and idx >= 0:
                l_idx = idx
                l_char = digits[digit]
        
        result = f_char + l_char
        print(result.ljust(5), "-", s)
        return int(result)
    


    m = map(find_num, inp)
    l = list(m)
    return sum(l)


# with open("01.test") as fp:
#     inp = fp.read().strip('\n').split('\n')

# print("Test One", part_one(inp))



# with open("01.inp") as fp:
#     inp = fp.read().strip('\n').split('\n')

# print("Part One", part_one(inp))

# part_two(["7msxhtdk"])

with open("01.test2") as fp:
    inp = fp.read().strip('\n').split('\n')

print("Test Two", part_two(inp))

with open("01.inp") as fp:
    inp = fp.read().strip('\n').split('\n')

print("Part Two", part_two(inp))




