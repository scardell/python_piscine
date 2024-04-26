
def all_thing_is_obj(object: any) -> int:

    """
    Determines the type of the input object
    and prints a corresponding message.

    Parameters:
    - object (any): The input object
    whose type needs to be determined.

    Returns:
    - int: A constant value of 42.

    Prints a message indicating the type of the input object.
    If the object is of type 'str', it prints a special message
    indicating that the object is in the kitchen.
    """

    type_names = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
        str: "String"
    }

    object_type = type(object)
    type_name = type_names.get(object_type, "Type not found")

    if object_type == str:
        print(f"{object} is in the kitchen : {object_type}")
    elif type_name != "Type not found":
        print(f"{type_name} : {object_type}")
    else:
        print(f"{type_name}")

    return 42
