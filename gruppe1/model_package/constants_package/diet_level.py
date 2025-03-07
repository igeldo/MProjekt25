from enum import Enum

# TODO: come up with better names
class DietLevel(Enum):
    UNHEALTHY   = 1
    MID         = 2
    HEALTHY     = 3

    diet_level_to_str = {
        UNHEALTHY: 'wenig ausgewogen',
        MID: 'ausgewogen',
        HEALTHY: 'sehr ausgewogen'
    }

    str_to_diet_level = {
        'wenig ausgewogen': UNHEALTHY,
        'ausgewogen': MID,
        'sehr ausgewogen': HEALTHY
    }


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