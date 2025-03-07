from enum import Enum

class PreCondition(Enum):
    NONE        = 'nein'
    CONDITION_1 = 'Bluthochdruck'
    CONDITION_2 = 'Schilddrüsenüberfunktion'
    OTHER       = 'andere'

    @staticmethod
    def string_to_enum(string: str):
        value = None
        if 'nein' == string:
            value = PreCondition.NONE
        elif 'Bluthochdruck' == string:
            value = PreCondition.CONDITION_1
        elif 'Schilddrüsenüberfunktion' == string:
            value = PreCondition.CONDITION_2
        elif 'andere' == string:
            value = PreCondition.OTHER
        return value