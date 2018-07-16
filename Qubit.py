import Exceptions

class Qubit:

    def __init__(self, identifier, state, computer):
        if len(state) != 2:
            raise Exceptions.DimensionException({
                "message": "[Error] Qubit state must only have 2 dimensions.",
                "state": state
            })

        if sum(map(lambda x: abs(x), state)) != 1:
            raise Exceptions.NormalizationException({
                "message": "[Error] Qubit must be normalized. Condition: |c_0|^2 + |c_1|^2 = 1.",
                "state": state
            })

        self._identifier = identifier
        self._state = state
        computer.addQubit(self)

    def getIdentifier(self):
        return self._identifier

    def getState(self):
        return self._state

    def getIndex(self):
        return self._index

    def setIndex(self, index):
        self._index = index
