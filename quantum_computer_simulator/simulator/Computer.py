import numpy as np

from quantum_computer_simulator.helpers.Exceptions import QuantumRegisterException
from quantum_computer_simulator.helpers.Util import decimal_to_binary
import quantum_computer_simulator.gates as Gates

class Computer:

    def __init__(self, qubits):
        self._qubits = qubits
        self._state = np.zeros(2 ** self._qubits, dtype=complex)
        self._state[0] = 1 + 0j

        self._measured_value = None

    def _apply_gate(self, gate, *args):
        if self._measured_value:
            raise QuantumRegisterException({
                "message": "cannot apply a gate to a measured quantum register"
            })

        logic_gate_matrix = gate.generate_gate_matrix(args, self._qubits)
        print(logic_gate_matrix)

        self._state = logic_gate_matrix.dot(self._state)

    def measure(self):
        if not self._measured_value:
            print(self._state)

            probabilities = [
                abs(i) ** 2 for i in self._state
            ]

            print(probabilities)

            self._measured_value = "|psi> = |{0}>".format("".join(map(str, decimal_to_binary(
                self._qubits,
                np.random.choice(
                    range(len(probabilities)),
                    p=probabilities
                )
            ))))

        return self._measured_value

    def X(self, qubit):
        return self._apply_gate(Gates.X(), qubit)

    def Y(self, qubit):
        return self._apply_gate(Gates.Y(), qubit)

    def Z(self, qubit):
        return self._apply_gate(Gates.Z(), qubit)

    def R(self, qubit, phi):
        return self._apply_gate(Gates.R(phi), qubit)

    def H(self, qubit):
        return self._apply_gate(Gates.H(), qubit)

    def SqrtNOT(self, qubit):
        return self._apply_gate(Gates.SqrtNOT(), qubit)

    def CNOT(self, qubit_1, qubit_2):
        return self._apply_gate(Gates.CNOT(), qubit_1, qubit_2)
