print((lambda d,v: sum([num * v.count(num) for num in d]))(*zip(*([[int(l.split()[0]), int(l.split()[-1])] for l in open("day1.txt").readlines()]))))
