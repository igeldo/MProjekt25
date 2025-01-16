from enum import Enum

# TODO: come up with better names
class FitnessLevel(Enum):
    LOW     = 1
    MID     = 2
    HIGH    = 3

    @staticmethod
    def str_to_fitness_level(fitness_level: str):
        # TODO: exception handling, also convert to string first

        print(type(fitness_level))

        if "1" == fitness_level:
            fitness_level = FitnessLevel.LOW
        elif "2" == fitness_level:
            fitness_level = FitnessLevel.MID
        elif "3" == fitness_level:
            fitness_level = FitnessLevel.HIGH
        else:
            raise ValueError("Keine korrekte Eingabe")

        return fitness_level