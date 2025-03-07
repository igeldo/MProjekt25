from enum import Enum

# TODO: come up with better names, think about smaller ranges
class AgeRange(Enum):
    RANGE_18_TO_44  = 1
    RANGE_45_TO_64  = 2
    RANGE_65_TO_79  = 3

    age_range_to_str = {
        RANGE_18_TO_44: '18 bis 44',
        RANGE_45_TO_64: '45 bis 64',
        RANGE_65_TO_79: '65 bis 79',
    }

    str_to_age_range = {
        '18 bis 44': RANGE_18_TO_44,
        '45 bis 64': RANGE_45_TO_64,
        '65 bis 79': RANGE_65_TO_79
    }

    # @staticmethod
    # def str_to_age_range(age_range: str):
    #     age_range = int(age_range)
    #     # TODO: exception handling
    #
    #     if 18 <= age_range <= 27:
    #         age_range = AgeRange.RANGE_18_TO_27
    #     elif 28 <= age_range <= 37:
    #         age_range = AgeRange.RANGE_28_TO_37
    #     elif 38 <= age_range <= 47:
    #         age_range = AgeRange.RANGE_38_TO_47
    #     elif 48 <= age_range <= 57:
    #         age_range = AgeRange.RANGE_48_TO_57
    #     elif 58 <= age_range <= 67:
    #         age_range = AgeRange.RANGE_58_TO_67
    #     elif 68 <= age_range <= 77:
    #         age_range = AgeRange.RANGE_68_TO_77
    #     else:
    #         age_range = AgeRange.NOT_SUPPORTED
    #
    #     return age_range