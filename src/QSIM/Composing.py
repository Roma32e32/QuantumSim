import numpy as np


def compose_inrow(gates):
    output = 1

    for gate in gates:
        output = np.kron(output, gate)

    return output


def compose_inline(*mats):

    output = np.identity(mats[0].shape[0])

    for mat in mats:
        output = np.matmul(output, mat)

    return output