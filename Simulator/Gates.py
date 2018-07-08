import numpy as np

singleQubitGates = {
    # Pauli-X (Not Gate)
    "X": np.array([
        0, 1, 1, 0
    ], dtype=complex),

    # Pauli-Y Gate
    "Y": np.array([
        0, 0 - 1j, 0 + 1j, 0
    ], dtype=complex),

    # Pauli-Z Gate
    "Z": np.array([
        1, 0, 0, -1
    ], dtype=complex),

    #Hadamard Gate
    "Hadamard": np.multiply(1 / np.sqrt(2), np.array([
        1, 1, 1, -1
    ], dtype=complex)),

    "R": lambda phi: np.array([
        1, 0, 0, np.e ** (0 - 1j * phi)
    ], dtype=complex),

    "Sqrt NOT": np.multiply(0.5, np.array([
        1 + 1j, 1 - 1j, 1 - 1j, 1 + 1j
    ], dtype=complex))

}
