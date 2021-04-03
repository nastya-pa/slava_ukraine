field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def out_field(field):
    print('-------------')
    a = ''
    for i in field:
        for j in i:
            a += '| '
            a += j
            a += ' '
        a += '|'
        print(a)
        a = ''
    print('-------------')
    return '\n'


print(out_field(field))
