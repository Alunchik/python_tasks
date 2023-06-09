import re


def split(elem):
    el = elem.split('|')
    return el


def elem_format(elem):
    if re.fullmatch(r'[0-9]+\/[0-9]+\/[0-9]+', elem):
        li = elem.split('/')
        elem = li[2] + '.' + li[1] + '.' + li[0]
    if re.fullmatch(r'[0-9]+\.[0-9]+', elem):
        elem = "{:.3f}".format(float(elem))
    if re.fullmatch(r'[А-Яа-я]*\s*[А-Яа-я]\.\s[А-Яа-я]*', elem):
        li = elem.split(' ')
        elem = li[0][0] + '.' + li[1] + ' ' + li[2]
    if re.fullmatch(r'\w*@\w*\.\w*', elem):
        elem = re.findall(r'(\w*)@\w*\.\w*', elem)[0]
    return elem


def del_empty(table):
    i = 0
    while i < len(table):
        # empty = True
        # j = 0
        # while j < len(table[i]):
        #     if table[i][j] is not None:
        #         empty = False
        #     j += 1
        if len(table[i]) == 0:
            table.remove(table[i])
            i -= 1
        i += 1
    return table


def main(table):
    new_table = []
    cols = len(table)
    rows = len(table[0])
    empty = False
    for i in range(rows):
        new_table.append([])
    new_table.append([])
    i = 0
    while i < len(table):
        if (empty):
            table.remove(table[i - 1])
            i -= 1
        empty = True
        j = 0
        while (j < len(table[i])):
            elem = table[i][j]
            if (elem is None):
                pass
            else:
                empty = False
                if re.match(r'.*\|.*', elem):
                    for k in range(len(split(elem))):
                        new_table[j + k].append(elem_format(split(elem)[k]))
                else:
                    elem = elem_format(elem)
                    new_table[j].append(elem)
            j += 1
        i += 1
    new_table = del_empty(new_table)
    return new_table
