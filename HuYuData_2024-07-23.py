from collections import deque

# Create an empty deque
my_deque = deque()

# Adding elements to the deque
my_deque.append(1)      # deque: [1]
my_deque.appendleft(2)  # deque: [2, 1]

# Removing elements from the deque
print(my_deque.pop())   # Output: 1, deque: [2]
print(my_deque.popleft())  # Output: 2, deque: []

# Adding and removing from both ends
my_deque.extend([3, 4, 5])       # deque: [3, 4, 5]
my_deque.extendleft([2, 1, 0])   # deque: [0, 1, 2, 3, 4, 5]

print(my_deque)

from collections import deque


def sliding_window_max(nums, k):
    n = len(nums)
    result = []
    dq = deque()

    for i in range(n):
        # Remove elements not within the window
        if dq and dq[0] == i - k:
            dq.popleft()

        # Maintain decreasing order in deque
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()

        dq.append(i)

        # Add maximum of current window to result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Example usage:
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_max(nums, k))  # Output: [3, 3, 5, 5, 6, 7]