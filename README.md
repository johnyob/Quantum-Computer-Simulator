# Quantum Computer Simulator

> A Quantum Computer Simulator written in Python

This a simple Python package for a multi-qubit quantum computer simulator. This project was designed and implemented based of material provided by [An Introduction To Quantum Computing](https://arxiv.org/pdf/0708.0261.pdf)

## Features

- [x] Pauli-X gate
- [x] Pauli-Y gate
- [x] Pauli-Z gate
- [X] Hadamard gate
- [x] Phase shift gate
- [x] Square root of NOT gate 
- [x] CNOT gate
- [x] Quantum measurement

## Installation

```sh
pip install quantum_computer_simulator
```

Note: not working as of 2018-07-27

## Usage

The quantum computer simulator can be accessed via the `Computer` interface. This interface acts as a wrapper for the quantum register. When instantiating the `Computer` interface, the number of qubits is require, for example:
```python
from quantum_computer_simulator import Computer

five_qubit_computer = Computer(5)

print(five_qubit_computer.measure())
```

Printing:

```python
"|phi> = |00000>"
```

### Quantum measurement / observation
To observe / measure the state of the quantum register the `measure` method must be used, for example:
```python
from quantum_computer_simulator import Computer

two_qubit_computer, four_qubit_register = Computer(2), Computer(4)

print(two_qubit_computer.measure())
print(four_qubit_register.measure())
```

Printing:

```python
"|phi> = |00>"
"|phi> = |0000>"
```

After the register has been measured / observed, it can no-longer have any gates applied to it. Otherwise a `QuantumRegisterException` is raised, for example:
```python
from quantum_computer_simulator import Computer

one_qubit_computer = Computer(1)

print(one_qubit_computer.measure())

one_qubit_computer.H(1)
```

Printing:

```python
"|phi> = |0>"
"quantum_computer_simulator.helpers.Exceptions.QuantumRegisterException: {'message': 'cannot apply a gate to a measured quantum register'}"
```

### Single qubit gates

This quantum computer simulator support 6 commonly used single qubit gates: 

- Pauli-X gate
- Pauli-Y gate
- Pauli-Z gate
- Hadamard gate
- Phase shift gate
- Square root of NOT gate 

However, more single qubit gates can be implemented by creating subclasses of the `SingleQubitGate` class. 

The `Computer` interface provides methods for all six of these gates:

- `X(qubit)`
- `Y(qubit)`
- `Z(qubit)`
- `H(qubit)`
- `R(qubit, phi)`, where phi is the phase shift (in radians)
- `SqrtNOT(qubit)`

`qubit` is an index reference to the qubit that the gate will be applied too. Therefore `qubit` must be in the range of `1 <= qubit <= n`, where n is the number of qubits that are being simulated. 

Examples:

#### Pauli-X gate
```python
from quantum_computer_simulator import Computer

two_qubit_computer = Computer(2)
#Initial state of |phi> = |00>

two_qubit_computer.X(1)

print(two_qubit_computer.measure())
```

Printing:

```python
"|phi> = |10>"
```

#### Pauli-Y gate
```python
from quantum_computer_simulator import Computer

three_qubit_computer = Computer(3)
#Initial state of |phi> = |000>

three_qubit_computer.Y(2)

print(three_qubit_computer.measure())
```

Printing:

```python
"|phi> = |010>"
```

#### Pauli-Z gate
```python
from quantum_computer_simulator import Computer

one_qubit_computer = Computer(1)
#Initial state of |phi> = |0>

one_qubit_computer.Z(1)

print(one_qubit_computer.measure())
```

Printing:

```python
"|phi> = |0>"
```

#### Hadamard Gate
```python
from quantum_computer_simulator import Computer

two_qubit_computer = Computer(2)
#Initial state of |phi> = |00>

two_qubit_computer.H(2)

print(two_qubit_computer.measure())
```
Printing either:

```python
"|phi> = |00>"
```

or 
```python
"|phi> = |01>"
```

#### Phase shift (R_phi) Gate
```python
from numpy import pi

from quantum_computer_simulator import Computer

two_qubit_computer = Computer(2)
#Initial state of |phi> = |00>

two_qubit_computer.R(1, pi) #Pauli-Z gate when phi = pi

print(two_qubit_computer.measure())
```

Printing:

```python
"|phi> = |00>"
```

#### Square root of NOT Gate
```python
from quantum_computer_simulator import Computer

five_qubit_computer = Computer(5)
#Initial sate of |phi> = |00000>

five_qubit_computer.SqrtNOT(4)

print(five_qubit_computer.measure())
```

Printing either:

```python
"|phi> = |00000>"
```

or
```python
"|phi> = |00010>"
```

### Multi qubit gates

Currently this quantum computer simulator only supports 1 multi-qubit gate; the CNOT gate or Controlled NOT. The CNOT gate can be accessed via the `CNOT` method in the `Computer` interface. This method requires 2 arguments `qubit_1` and `qubit_2`. `qubit_1` is the control qubit and `qubit_2` is the target qubit. For example:
```python
from quantum_computer_simulator import Computer

three_qubit_simulator = Computer(3)
#Initial state of |phi> = |000>

three_qubit_simulator.X(1) #Set control qubit = 1
three_qubit_simulator.CNOT(1, 3)

print(three_qubit_simulator.measure())
```

Printing:

```python
"|phi> = |101>"
```

## Errors
If you discover an error within this package, please email [me](mailto:alistair.o'brien@ellesmere.com).

## Credits
- [Alistair O'Brien](https://github.com/johnyob)