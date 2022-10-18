def maxnum(array: list[str]) -> str:
    """
    Return the largest number that can be composed from an array of numbers.
    Time complexity: O(n^2)
    Based on buble sort algorithm
    """
    n = len(array)
    for i in range(n- 1):
        for j in range(0, n-i-1):
            var1 = array[j] + array[j+1]
            var2 = array[j + 1] + array[j]
            if var1 < var2:
                array[j], array[j+1] = array[j+1], array[j]

    return "".join(array)

if __name__ == '__main__':
    assert maxnum(["11", "5", "9"]) == "9511"
