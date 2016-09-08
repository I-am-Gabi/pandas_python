
def repeticao():
    ### FOR
    a = ['gato', 'janela', 'defenestrar']
    for x in a:
        print x, len(x)

    while a:
        print a.pop()


def repeticao_range():
    ### RANGE
    for i in range(0, 10):
        if i < 5:
            print i
        else:
            continue

    for num in range(0, 20, 2):
        print (num)
