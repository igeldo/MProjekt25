from enum import Enum

class BiologicalSex(Enum):
    FEMALE  = 1
    MALE    = 2

    @staticmethod
    def str_to_biological_sex(biological_sex: str):
        # TODO: exception handling
        biological_sex.lower()

        if "w" == biological_sex or "weiblich":
            biological_sex = BiologicalSex.FEMALE
        elif "m" == biological_sex or "männlich" or "maennlich":
            biological_sex = BiologicalSex.MALE
        else:
            raise ValueError("Keine korrekte Eingabe")

        return biological_sex