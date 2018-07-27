import numpy as np

from quantum_computer_simulator.gates.SingleQubitGate import SingleQubitGate

class Z(SingleQubitGate):

    def __init__(self):
        super().__init__(np.array([
            [1, 0],
            [0, -1]
        ], dtype=complex))
