import numpy as np

from quantum_computer_simulator.gates.SingleQubitGate import SingleQubitGate

class Y(SingleQubitGate):

    def __init__(self):
        super().__init__(np.array([
            [0, 0 - 1j],
            [0 + 1j, 0]
        ], dtype=complex))