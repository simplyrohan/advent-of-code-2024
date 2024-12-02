def validate(line: list[int]):
    diffs = [line[i] - line[i + 1] for i in range(len(line) - 1)]
    if not all([3 >= abs(diff) >= 1 for diff in diffs]):
        return False

    return all([diff < 0 for diff in diffs]) or all([diff > 0 for diff in diffs])


def solve(reports: list[list[int]]):
    safe = 0
    for report in reports:
        success = validate(report)
        if success:
            safe += 1
    return safe


with open("day2/day2.txt", "r") as f:
    reports = []
    for report in f.readlines():
        reports.append([int(t) for t in report.split()])

    print(solve(reports)) # Solve: 442
