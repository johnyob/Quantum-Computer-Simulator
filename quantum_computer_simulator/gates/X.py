import numpy as np

from quantum_computer_simulator.gates.SingleQubitGate import SingleQubitGate

class X(SingleQubitGate):

    def __init__(self):
        super().__init__(np.array([
            [0, 1],
            [1, 0]
        ], dtype=complex))
