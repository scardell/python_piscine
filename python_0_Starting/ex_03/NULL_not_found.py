import math

def NULL_not_found(object: any) -> int:
    type_names = {
        None: "Nothing",
        math.nan: "Cheese",
        0: "Zero",
        '0': "Zero",
        '': "Empty",
        False: "Fake"
    }

    type_name = type_names.get(object, "Type not Found")

    if type(object) is float and math.isnan(object):
        print(f"Cheese: {object} {type(object)}")
    elif object == 0 and type(object) is int:
        print(f"Zero: {object} {type(object)}")
    elif type_name != "Type not Found":
        print(f"{type_name}: {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0
