import numpy as np

from quantum_computer_simulator.gates.SingleQubitGate import SingleQubitGate

class R(SingleQubitGate):

    def __init__(self, phi):
        super().__init__(np.array([
            [1, 0],
            [0, np.e ** ((0 + 1j) * phi)]
        ], dtype=complex))

