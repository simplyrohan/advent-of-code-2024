import re

def solve(data):
    matches =  re.findall(r"mul\(\d{1,3},\d{1,3}\)", data)
    sum = 0    
    
    for match in matches:
        numbers = match[4:-1].split(',')
        
        if len(numbers) == 2:
            if len(numbers[0]) <= 3 and len(numbers[1]) <= 3:
                sum += int(numbers[0]) * int(numbers[1])
    return sum


# with open('day3/day3test.txt') as f:
#     print(solve(f.read()))


with open('day3/day3input.txt') as f:
    print(solve(f.read()))

