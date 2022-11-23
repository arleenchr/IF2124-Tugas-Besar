list_terminal = []


def file_to_cfg(filename):
    file = open(filename, 'r')
    cfg = {}

    row = file.readline()
    while (row != ''):
        head, body = row.replace('\n', '').split(' -> ')
        head, body = row.replace(';', '').split(' -> ')

        if (head not in cfg.keys()):
            cfg[head] = [body.split(' ')]
        else:
            cfg[head].append(body.split(' '))
        row = file.readline()

    file.close()
    return cfg


def is_terminal(string):
    return string in list_terminal


def is_variabel(string):
    return string not in list_terminal
