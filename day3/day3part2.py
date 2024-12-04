import re


def solve(data):
    mul_index = [
        m.start(0) for m in re.finditer(r"mul\(\d{1,3},\d{1,3}\)", data)
    ]
    muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)

    do_ind = [m.start(0) for m in re.finditer(r"do\(\)", data)]
    dont_ind = [m.start(0) for m in re.finditer(r"don't\(\)", data)]

    sum = 0

    enable = True

    for i in range(len(data)):
        if i in do_ind:
            print('di')
            enable = True
        elif i in dont_ind:
            print('dont')
            enable = False
        
        elif i in mul_index:
            mul = muls.pop(0)
        
            if enable:
                # find the mul
                numbers = mul[4:-1].split(',')

                sum += int(numbers[0]) * int(numbers[1])
    return sum


# with open("day3/day3test2.txt") as f:
#     print(solve(f.read()))


with open('day3/day3input.txt') as f:
    print(solve(f.read()))
