from abc import ABC, abstractmethod


class ValidatedIdentifier(ABC):
    @abstractmethod
    def validate():
        pass

    @abstractmethod
    def not_null():
        pass

    @abstractmethod
    def not_empty():
        pass

    @abstractmethod
    def only_allowed_symbols():
        pass

    @abstractmethod
    def correct_len():
        pass

    @abstractmethod
    def checksum():
        pass
