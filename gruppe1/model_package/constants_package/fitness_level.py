from enum import Enum

# TODO: come up with better names
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

    # @staticmethod
    # def str_to_fitness_level(fitness_level: str):
    #     # TODO: exception handling, also convert to string first
    #
    #     print(type(fitness_level))
    #
    #     if "1" == fitness_level:
    #         fitness_level = FitnessLevel.LOW
    #     elif "2" == fitness_level:
    #         fitness_level = FitnessLevel.MID
    #     elif "3" == fitness_level:
    #         fitness_level = FitnessLevel.HIGH
    #     else:
    #         raise ValueError("Keine korrekte Eingabe")
    #
    #     return fitness_level