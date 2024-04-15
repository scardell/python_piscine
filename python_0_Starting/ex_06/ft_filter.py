
def ft_filter(function, sequence):
    if function:
        return (item for item in sequence if function(item))
    return (item for item in sequence if item)