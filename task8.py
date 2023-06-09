import re


def main(table):
    new_table = []
    first_string=True
    for string in table:
        for elem in string:
            if elem is not None:
                if len(re.findall(r'[0-9]+\/[0-9]+\/[0-9]+', elem)) > 0:
                    elem = elem.replace('/', '.')
                if elem.isdigit():
                    elem = round(elem, 3)
                if re.match(r'.*|.*', elem):                    elem = elem.split('|')

    return table
