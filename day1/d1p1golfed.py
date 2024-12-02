print((lambda d,v: sum(abs(sorted(list(d))[i] - sorted(list(v))[i]) for i in range(len(d))))(*zip(*([[int(l.split()[0]), int(l.split()[-1])] for l in open("day1/day1.txt").readlines()]))))
