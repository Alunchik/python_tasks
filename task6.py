def main(x):
    if x[0] == 1974:
        return 9
    if x[0] == 2019:
        return 10
    if x[2] == 2018:
        return 3
    if x[2] == 2000:
        return ['STON', 'CLICK', 'ALLOY'].index(x[4])
    if x[4] == 'ALLOY':
        return ['LIMBO', 'STON', 'RDOC'].index(x[3]) + 6
    return ['STON', 'CLICK'].index(x[4]) + 4
