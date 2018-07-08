import numpy as np
import math as Math
import Gates

class Computer:
    def __init__(self):
        self.reset()

    def reset(self):
        self._state = np.array([1 + 0j], dtype=complex) #set P(0) = 1
        self._qubits = 0

    #Register Method

    def addQubit(self, q):
        q.setIndex(self._qubits)
        _state = np.zeros(self._state.size * 2, dtype=complex)

        for i in range(self._state.size):
            for j in range(1):
                _state[2 * i + j] = self._state[i] * q.getState()[j]

        self._state = _state
        self._qubits += 1

    #Gate Method

    def _applySingleQubitGate(self, q, gate):
        _state = np.zeros(self._state.size, dtype=complex)
        for i in range(self._state.size):
            binary = self._decimalToBinary(i)
            a, b, c = (gate[3], gate[1], 0) if binary[q.getIndex()] else (gate[0], gate[2], 1)

            _state[i] += a * self._state[i]
            binary[q.getIndex()] = c
            _state[self._binaryToDecimal(binary)] += b * self._state[i]

        self._state = _state

    def X(self, q):
        return self._applySingleQubitGate(q, Gates.singleQubitGates["X"])

    def Y(self, q):
        return self._applySingleQubitGate(q, Gates.singleQubitGates["Y"])

    def Z(self, q):
        return self._applySingleQubitGate(q, Gates.singleQubitGates["Z"])

    def R(self, q, phi):
        return self._applySingleQubitGate(q, Gates.singleQubitGates["R"](phi))

    def H(self, q):
        return self._applySingleQubitGate(q, Gates.singleQubitGates["Hadamard"])

    def SqrtNOT(self, q):
        return self._applySingleQubitGate(q, Gates.singleQubitGates["Sqrt NOT"])

    def CNOT(self, q1, q2):
        """
        |q1, q2> ==> |q1, q1 xor q2>
        """
        _state = np.zeros(self._state.size, dtype=complex)

        for i in range(self._state.size):
            binary = self._decimalToBinary(i)
            binary[q2.getIndex()] = (binary[q2.getIndex()] + binary[q1.getIndex()]) % 2
            _state[self._binaryToDecimal(binary)] = self._state[i]

        self._state = _state

    #Measure Method
    def measure(self, q):
        probabilities = np.array([], dtype=complex)
        for i in self._state:
            probabilities = np.append(
                probabilities, (i * i.conjugate()).real
            )

        random = np.random.ranf()
        hi = 0
        for i in range(len(probabilities)):
            low, hi = hi, hi + probabilities[i]
            if low <= random and random < hi:
                #Collapse Quantum State into Pure State
                self._state = np.zeros(len(self._state), dtype=complex)
                self._state[i] = 1
                print(self._state[i])
                binary = self._decimalToBinary(i)
                return binary[q.getIndex()], i

    # Helper Methods
    def _decimalToBinary(self, n):
        return list(map(lambda x: int(x), list(format(n, "0{0}b".format(self._qubits)))))

    def _binaryToDecimal(self, n):
        return int("".join(map(lambda x: str(x), n)), 2)
