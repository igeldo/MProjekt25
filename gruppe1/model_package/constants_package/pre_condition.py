from enum import Flag

# TODO: names
class PreCondition(Flag):
    CONDITION_1 = 1
    CONDITION_2 = 2
    CONDITION_3 = 4
    CONDITION_4 = 8
    CONDITION_5 = 16
    OTHER       = 32

    CONDITION_MAP = {
        "1": CONDITION_1,
        "2": CONDITION_2,
        "3": CONDITION_3,
        "4": CONDITION_4,
        "5": CONDITION_5,
        "6": OTHER
    }

    @staticmethod
    def str_to_pre_condition(pre_conditions_argument: str):
        # TODO: exception handling

        # # separate string to get provided conditions
        # pre_condition_list = [pre_condition.strip() for pre_condition in pre_conditions_argument.split(",")]
        # # print(pre_condition_list[0] in PreCondition.CONDITION_MAP.name)
        # #
        # # pre_conditions = "test"

        # pre_conditions = PreCondition(0)
        # if not pre_condition_list:
        #     raise ValueError("PreCondition cannot be empty")
        # else:
        #     for pre_condition in pre_condition_list:
        #         if pre_condition in PreCondition.CONDITION_MAP.name:
        #             test.append(PreCondition.CONDITION_MAP[pre_condition])
        #             pre_conditions |= PreCondition.CONDITION_MAP[pre_condition]
        #
        #
        # print(pre_conditions)
        # print(test)

        # # extract all conditions from the given parameter
        # pre_conditions = [PreCondition.CONDITION_MAP[pre_condition].value for pre_condition in
        #           (pre_condition.strip() for pre_condition in pre_conditions_argument.split(","))
        #           if pre_condition in PreCondition.CONDITION_MAP]

        ## zero-initialize return value
        # pre_conditions = PreCondition(0)
        # if "1" == pre_condition:
        #     pre_conditions |= PreCondition.CONDITION_1
        # if "2" == pre_condition:
        #     pre_conditions |= PreCondition.CONDITION_2
        # if "3" == pre_condition:
        #     pre_conditions |= PreCondition.CONDITION_3
        # if "4" == pre_condition:
        #     pre_conditions |= PreCondition.CONDITION_4
        # if "5" == pre_condition:
        #     pre_conditions |= PreCondition.CONDITION_5
        # if "6" == pre_condition:
        #     pre_conditions |= PreCondition.OTHER

        pre_conditions = PreCondition(2)

        print(pre_conditions)

        return pre_conditions

