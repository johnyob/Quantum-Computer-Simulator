import numpy as np

from quantum_computer_simulator.gates.SingleQubitGate import SingleQubitGate

class SqrtNOT(SingleQubitGate):

    def __init__(self):
        super().__init__(np.multiply(
            0.5,
            np.array([
                [1 + 1j, 1 - 1j],
                [1 - 1j, 1 + 1j]
            ], dtype=complex))
        )