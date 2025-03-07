from enum import Enum

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