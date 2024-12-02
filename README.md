# advent-of-code-2024

Note that `d_p_golfed.py` are code-golfed versions of the respective Day _ Part _ solutions.

All one-liner solutions (don't get mad if this code is terrible, unreadable, or insecure; thats the point)
```py
# Day 1 Part 1
print((lambda d,v: sum(abs(sorted(list(d))[i] - sorted(list(v))[i]) for i in range(len(d))))(*zip(*([[int(l.split()[0]), int(l.split()[-1])] for l in open("day1.txt").readlines()]))))
```
```py
# Day 1 Part 2
print((lambda d,v: sum([num * v.count(num) for num in d]))(*zip(*([[int(l.split()[0]), int(l.split()[-1])] for l in open("day1.txt").readlines()]))))
```
```py
# Day 2 Part 1
print(sum([1 for report in [[int(t) for t in report.split()] for report in open("day2/day2.txt", "r").readlines()] if all([3 >= abs(diff) >= 1 for diff in [report[i] - report[i + 1] for i in range(len(report) - 1)]]) and (all([diff < 0 for diff in [report[i] - report[i + 1] for i in range(len(report) - 1)]]) or all([diff > 0 for diff in [report[i] - report[i + 1] for i in range(len(report) - 1)]]))]))
```
```py
# Day 2 Part 2
print(sum([1 if all([3 >= abs(d) >= 1 for d in [r[i] - r[i + 1] for i in range(len(r) - 1)]]) and (all([d < 0 for d in [r[i] - r[i + 1] for i in range(len(r) - 1)]]) or all([d > 0 for d in [r[i] - r[i + 1] for i in range(len(r) - 1)]])) else (1 if any([1 for ind in range(len(r)) if all([3 >= abs(d) >= 1 for d in [(r[:ind] + r[ind + 1:])[i] - (r[:ind] + r[ind + 1:])[i + 1] for i in range(len((r[:ind] + r[ind + 1:])) - 1)]]) and (all([d < 0 for d in [(r[:ind] + r[ind + 1:])[i] - (r[:ind] + r[ind + 1:])[i + 1] for i in range(len((r[:ind] + r[ind + 1:])) - 1)]]) or all([d > 0 for d in [(r[:ind] + r[ind + 1:])[i] - (r[:ind] + r[ind + 1:])[i + 1] for i in range(len((r[:ind] + r[ind + 1:])) - 1)]]))]) else 0) for r in [[int(t) for t in r.split()] for r in open("day2/day2.txt", "r").readlines()]]))
```