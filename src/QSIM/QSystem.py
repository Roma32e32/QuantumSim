import numpy as np

from QSIM.Composing import *
from QSIM.Observing import *
from QSIM.Exceptions import *


class QSystem:
    def __init__(self, qbits_count, initial_state=None) -> None:
        self.qbits_count = qbits_count

        if initial_state != None:
            self.set_state(initial_state)
        else:
            self.__state__ = np.full(2**qbits_count, 0)
            self.__state__[0] = 1


    def set_state(self, state):
        state = np.array(state)
        corect_shape = 2 ** self.qbits_count
        if list(state.shape) == list([corect_shape]):
            if np.sum(find_probality(state)) == 1:
                self.__state__ = state
        else:
            raise QSystem_Incorect_State_Shape(f"Форма массива должна быть: {corect_shape}, не: {state.shape}.")        


    def apply(self, *gates):
        self.__state__ = np.dot(self.__state__, compose_inrow(gates))

    
    def apply_mat(self, mat):
        self.__state__ = np.dot(self.__state__, mat)
        

    def observe(self, accur=100):
        return observe(self.__state__, accur)