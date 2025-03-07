from enum import Enum

class AgeRange(Enum):
    RANGE_18_TO_44  = '18 bis 44'
    RANGE_45_TO_64  = '45 bis 64'
    RANGE_65_TO_79  = '65 bis 79'

    @staticmethod
    def string_to_enum(string: str):
        value = None
        if '18 bis 44' == string:
            value = AgeRange.RANGE_18_TO_44
        elif '45 bis 64' == string:
            value = AgeRange.RANGE_45_TO_64
        elif '65 bis 79' == string:
            value = AgeRange.RANGE_65_TO_79
        return value