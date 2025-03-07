from enum import Enum

# TODO: come up with better names
class DietLevel(Enum):
    UNHEALTHY   = 'wenig ausgewogen'
    MID         = 'ausgewogen'
    HEALTHY     = 'sehr ausgewogen'

    @staticmethod
    def string_to_enum(string: str):
        value = None
        if 'wenig ausgewogen' == string:
            value = DietLevel.UNHEALTHY
        elif 'ausgewogen' == string:
            value = DietLevel.MID
        elif 'sehr ausgewogen' == string:
            value = DietLevel.HEALTHY
        return value


    # @staticmethod
    # def str_to_diet_level(diet_level: str):
    #     # TODO: exception handling
    #
    #     if "1" == diet_level:
    #         diet_level = DietLevel.UNHEALTHY
    #     elif "2" == diet_level:
    #         diet_level = DietLevel.MID
    #     elif "3" == diet_level:
    #         diet_level = DietLevel.HEALTHY
    #     else:
    #         raise ValueError("Keine korrekte Eingabe")
    #
    #     return diet_level