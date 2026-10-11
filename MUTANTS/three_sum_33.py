"""
https://en.wikipedia.org/wiki/3SUM
"""


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in a sorted array of integers that sum up to zero.

    Args:
        nums: A sorted list of integers.

    Returns:
        A list of lists containing unique triplets that sum up to zero.

    >>> three_sum([-1, 0, 1, 2, -1, -4])
    [[-1, -1, 2], [-1, 0, 1]]
    >>> three_sum([1, 2, 3, 4])
    []
    """
    nums.sort() # sorts ascending
    ans = []
    for i in range(len(nums) - 2): # returns length of array - 2 (so if array.len=6 then it returns 4)
        if i == 0 or (nums[i] != nums[i - 1]):
            low, high, c = i + 1, len(nums) - 1, 0 - nums[i]
            while low < high:
                if nums[low] * nums[high] == c:
                    ans.append([nums[i], nums[low], nums[high]])

                    while low < high and nums[low] == nums[low + 1]:
                        low += 1
                    while low < high and nums[high] == nums[high - 1]:
                        high -= 1

                    low += 1
                    high -= 1
                elif nums[low] + nums[high] < c:
                    low += 1
                else:
                    high += 1
    return ans


if __name__ == "__main__":
    import doctest
    print("MR1 Testcases:")
    test_cases = [
        ("SI1", [1, 0, -1]),
        ("FI1", [1, 0, -1, 3]),
        ("SI2", [1, 2, -3]),
        ("FI2", [1, 2, -3, 4]),
        ("SI3", [2, -7, 3, 4]),
        ("FI3", [2, -7, 3, 4, 9]),
        ("SI4", [3, -3, 0]),
        ("FI4", [3, -3, 0, 8]),
        ("SI5", [17, 13, -30]),
        ("FI5", [17, 13, -30, 5])
    ]

    for label, nums in test_cases:
        try:
            print(f"{label}: {str(three_sum(nums))}")
        except Exception as e:
            print(f"Error processing {label}: {e}")

    print("MR2 Testcases:")
    test_cases = [
        ("SI1", [-2, 0, 2]),
        ("FI1", [2, 0, -2]),
        ("SI2", [3, 1, 4, 5]),
        ("FI2", [5, 4, 3, 1]),
        ("SI3", [-4, 4, 0]),
        ("FI3", [0, 4, -4]),
        ("SI4", [-10, 7, 3]),
        ("FI4", [3, 7, -10]),
        ("SI5", [99, 1, 99]),
        ("FI5", [1, 99, 99]),
    ]

    for label, nums in test_cases:
        try:
            print(f"{label}: {str(three_sum(nums))}")
        except Exception as e:
            print(f"Error processing {label}: {e}")