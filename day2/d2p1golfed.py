print(sum([1 for report in [[int(t) for t in report.split()] for report in open("day2/day2.txt", "r").readlines()] if all([3 >= abs(diff) >= 1 for diff in [report[i] - report[i + 1] for i in range(len(report) - 1)]]) and (all([diff < 0 for diff in [report[i] - report[i + 1] for i in range(len(report) - 1)]]) or all([diff > 0 for diff in [report[i] - report[i + 1] for i in range(len(report) - 1)]]))]))