

def ft_filter(function, sequence):
    """Filters elements from a sequence based on a filtering function.

    Args:
        function (function or None): A filtering function that takes an element from the sequence as input and returns True or False.
        If None, the identity function (bool(item)) will be used as the default filtering function.
        sequence (iterable): The sequence of elements to filter.

    Returns:
        generator: A generator that yields elements from the sequence for which the filtering function returns True,
          or for which the identity function returns True if no custom filtering function is provided.

    Note:
        If function is provided, elements in the sequence for which function(item) returns True are included in the output.
        If function is None, elements in the sequence that are evaluated as True (using bool(item)) are included in the output.

    """
    if function:
        return (item for item in sequence if function(item))
    return (item for item in sequence if item)