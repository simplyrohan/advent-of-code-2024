import pathlib
import re

enabled = True

print(sum([int(a) * int(b) for a, b, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", open("day3/day3test2.txt").read()) if enabled and a and b]))
#   if do:
#     enabled = True
#   elif dont:
#     enabled = False
#   elif enabled:
#     new_total += int(a) * int(b)

# print(new_total)