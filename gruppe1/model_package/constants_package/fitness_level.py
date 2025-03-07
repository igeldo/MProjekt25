from enum import Enum

class FitnessLevel(Enum):
    LOW     = 'wenig aktiv (weniger als 150 min Sport/Woche)'
    MID     = 'aktiv (mind. 150 min Sport/Woche)'
    HIGH    = 'sehr aktiv (deutlich mehr als 150 min Sport/Woche)'

    @staticmethod
    def string_to_enum(string: str):
        value = None
        if 'wenig aktiv (weniger als 150 min Sport/Woche)' == string:
            value = FitnessLevel.LOW
        elif 'aktiv (mind. 150 min Sport/Woche)' == string:
            value = FitnessLevel.MID
        elif 'sehr aktiv (deutlich mehr als 150 min Sport/Woche)' == string:
            value = FitnessLevel.HIGH
        return value