import numpy as np


def I():
    return np.array([[1,0],
                     [0,1]])

def SWAP():
    return np.array([[1,0,0,0],
                     [0,0,1,0],
                     [0,1,0,0],
                     [0,0,0,1]])

def H():
    return np.array([[1,1],
                     [1,-1]]) / np.sqrt(2)

def X():
    return np.array([[0,1],
                     [1,0]])

def Z():
    return np.array([[1,0],
                     [0,-1]])

def Y():
    return np.array([[0,-1j],
                     [1j,0]])

def S():
    return np.array([[1,0],
                     [0,1j]])

def T():
    pw = np.e ** (1j * np.pi/4)
    return np.array([[1,0],
                     [0,pw]])

def Rx(angle):
    return np.array([[np.cos(angle/2), -1j*np.sin(angle/2)],
                     [-1j*np.sin(angle/2), np.cos(angle/2)]])

def Ry(angle):
    return np.array([[np.cos(angle/2), -np.sin(angle/2)],
                     [np.sin(angle/2), np.cos(angle/2)]])

def Rz(angle):
    pw = np.e ** (-1j*angle/2)
    return np.array([[pw, 0],
                     [0, pw]])

"""
def U1(angle):
    pw = np.e ** (1j * angle)
    return np.array([[1, 0],
                     [0, pw]])

def U2(angle, angle2):
    pw1 = -np.e ** (1j * angle2)
    pw2 = np.e ** (1j * angle)
    pw3 = np.e ** (1j * (angle + angle2))
    return np.array([[1, pw1],
                     [pw2, pw3]])

def U3(angle3, angle, angle2):
    pw1 = -np.e ** (1j * angle2)
    pw2 = np.e ** (1j * angle)
    pw3 = np.e ** (1j * (angle + angle2))
    return np.array([[np.cos(angle3/2), pw1 * np.sin(angle3/2)],
                     [pw2 * np.sin(angle3/2), pw3 * np.cos(angle3/2)]])
"""

def C(gate: np.ndarray, target_size=0):
    gate_size = gate.shape[0]
    if target_size == 0:
        target_size = gate_size * 2

    up_mat = np.full((2, gate_size), 0)
    left_mat = np.full((gate_size, 2), 0)
    
    left = np.vstack((I(), left_mat))
    right = np.vstack((up_mat, gate))

    final = np.hstack((left, right))

    if final.shape[0] == target_size:
        return final
    else:
        return C(final, target_size)