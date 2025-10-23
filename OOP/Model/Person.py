from abc import ABC, abstractmethod
class Person(ABC):

    def __init__(self, name: str, age: int, gender: str, birthplace: str):
        self.__name = name  # Encapsulation - private attribute
        self.__age = age
        self.__gender = gender
        self.__birthplace = birthplace

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender

    @property
    def birthplace(self) -> str:
        return self.__birthplace

    # Setter methods (Encapsulation)
    @name.setter
    def name(self, value: str):
        if value and isinstance(value, str):
            self.__name = value

    @age.setter
    def age(self, value: int):
        if isinstance(value, int) and value > 0:
            self.__age = value

    @gender.setter
    def gender(self, value: str):
        if value.lower() in ['nam', 'nữ', 'male', 'female']:
            self.__gender = value

    @birthplace.setter
    def birthplace(self, value: str):
        if value and isinstance(value, str):
            self.__birthplace = value

    @abstractmethod
    def get_info(self) -> str:
        pass

    @abstractmethod
    def get_role(self) -> str:
        pass
