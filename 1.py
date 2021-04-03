field = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]


def out_field11(field):
    print('----------')
    a1 = ''
    for i in field:
        for j in i:
            a1 += '| '
            a += j
            a += ' '
        a1 += '|'
        print(a1)
        a = ''
    print('-------------')
    return '\n'


print(out_field11(field))


def out_field(fielt):
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
