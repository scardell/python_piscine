
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Aqui va la documentacion.
    """
    try:
        if not isinstance(family, list) \
                or not isinstance(start, int) or not isinstance(end, int):
            raise AssertionError("input must be a list and two integers.")
        if not all(len(item) == len(family[0]) for item in family):
            raise AssertionError("Input list with different sizes.")
        print(f"My shape is : {np.array(family).shape}")
        print(f"My new shape is : {np.array(family)[start:end+1].shape}")
        return np.array(family)[start:end].tolist()
        
    except AssertionError as error:
        print("\33[31m", AssertionError.__name__+":", error, "\33[0m")
        return ""
