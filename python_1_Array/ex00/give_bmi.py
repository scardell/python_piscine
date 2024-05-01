
def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """
    Calculate BMI values based on given heights and weights.

    Args:
        height (list[int | float]): List of heights in meters.
        weight (list[int | float]): List of weights in kilograms.

    Returns:
        list[int | float]: List of calculated BMI values.
    """

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same size")
    if not all(isinstance(x, (int, float)) for x in height):
        raise ValueError("All elements in height must be integers or floats")
    if not all(isinstance(x, (int, float)) for x in weight):
        raise ValueError("All elements in weight must be integers or floats")
    return [w / h ** 2 for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Determine whether BMI values are above a given limit.

    Args:
        bmi (list[int | float]): List of BMI values.
        limit (int): Limit to compare BMI values against.

    Returns:
        list[bool]: List of booleans indicating whether
        each BMI value is above the limit.
    """
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise ValueError("All elements in bmi must be integers or floats")
    if not isinstance(limit, int):
        raise ValueError("Limit must be an integer")
    return [b > limit for b in bmi]

