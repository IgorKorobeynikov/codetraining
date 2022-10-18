def maxnum_(array: list[str]) -> str:
    """
    Based on python's sorting algorithm
    Time compexity (presumably): O(n log n)
    """
    array.sort(reverse=True)
    return "".join(array)
