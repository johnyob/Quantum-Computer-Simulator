import numpy as np

from quantum_computer_simulator.gates.SingleQubitGate import SingleQubitGate

class H(SingleQubitGate):

    def __init__(self):
        super().__init__(np.multiply(
            1 / np.sqrt(2),
            np.array([
                [1, 1],
                [1, -1]
            ], dtype=complex)
        ))