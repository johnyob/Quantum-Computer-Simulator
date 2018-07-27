from functools import reduce

import numpy as np

from quantum_computer_simulator.helpers.Util import decimal_to_binary
from quantum_computer_simulator.helpers.Constants import STATES

class SingleQubitGate:

    def __init__(self, gate):
        """
        Creates a single qubit gate

        :param gate: A 2D array (matrix) representing the gate (numpy.array)
        """

        self._gate = gate

    def generate_gate_matrix(self, q, n):
        """
        Produces the logic gate matrix of size 2^n by 2^n, where n is the number of qubits being simulated.
        https://cs.stackexchange.com/questions/48834/applying-a-multi-qubit-quantum-gate-to-specific-qubits

        :param q: index of the qubit that the gate is being applied too (integer)
        :param n: number of qubits being simulated (integer)
        :return: (numpy.array)
        """

        logic_gate_matrix = np.zeros((2 ** n, 2 ** n), dtype=complex)
        for i in range(2 ** n):
            logic_gate_matrix[:, i] = self._gate_transformation_function(i, q[0], n)

        return logic_gate_matrix

    def _gate_transformation_function(self, x, q, n):
        """
        Calculates the logic gate transformation function for x.

        :param x: decimal representation of pure state. e.g. |00>, |01>, |10>, |11> -> x in [0, 1, 2, 3] (integer)
        :param q: index of the qubit that the gate is being applied too (integer)
        :param n: number of qubits being simulated (integer)
        :return: (numpy.array)
        """

        states = [
            STATES[state] if i != q else self._gate.dot(STATES[state]) \
            for i, state in enumerate(decimal_to_binary(n, x), start=1)
        ]

        print()
        print(x)
        print(states)

        return reduce(np.kron, states)
