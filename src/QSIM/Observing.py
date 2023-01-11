import numpy as np


def find_probality(qbits):
    return np.absolute(qbits ** 2)


def observe(qbits, accur=100):
    qbits2 = find_probality(qbits) * accur
    lst = []

    for el in range(len(qbits2)):
        for el2 in range(int(qbits2[el])):
            lst.append(el)


    return np.random.choice(lst)