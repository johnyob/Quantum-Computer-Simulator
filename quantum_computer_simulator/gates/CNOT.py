from functools import reduce

import numpy as np

from quantum_computer_simulator.helpers.Util import decimal_to_binary
from quantum_computer_simulator.helpers.Constants import STATES

class CNOT:

    def generate_gate_matrix(self, qs, n):
        """
        Produces the logic gate matrix of size 2^n by 2^n, where n is the number of qubits being simulated.

        :param qs: list of qubits that the gate is being applied too (tuple)
        :param n: number of qubits being simulated (integer)
        :return: (numpy.array)
        """
        q_1, q_2 = qs #q_1 is control, q_2 is target


        logic_gate_matrix = np.zeros((2 ** n, 2 ** n), dtype=complex)
        for i in range(2 ** n):
            logic_gate_matrix[:, i] = self._gate_transformation_function(i, q_1, q_2, n)

        return logic_gate_matrix

    def _gate_transformation_function(self, x, q_1, q_2, n):
        """
        Calculates the logic gate transformation function for x.

        :param x: decimal representation of pure state. e.g. |00>, |01>, |10>, |11> -> x in [0, 1, 2, 3] (integer)
        :param q: index of the qubit that the gate is being applied too (integer)
        :param n: number of qubits being simulated (integer)
        :return: (numpy.array)
        """

        binary = decimal_to_binary(n, x)

        return reduce(np.kron, [
            STATES[state] if i != q_2 else STATES[self._apply(binary[q_1 - 1], binary[q_2 - 1])] \
            for i, state in enumerate(binary, start=1)
        ])

    def _apply(self, q_1, q_2):
        return q_1 ^ q_2
