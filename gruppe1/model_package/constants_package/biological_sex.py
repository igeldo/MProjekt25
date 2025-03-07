from enum import Enum

class BiologicalSex(Enum):
    FEMALE  = 'w'
    MALE    = 'm'

    @staticmethod
    def string_to_enum(string: str):
        value = None
        if 'w' == string:
            value = BiologicalSex.FEMALE
        elif 'm' == string:
            value = BiologicalSex.MALE
        return value