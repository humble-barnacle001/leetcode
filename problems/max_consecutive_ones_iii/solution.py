class Solution:
    def longestOnes(self, arr: List[int], k: int) -> int:
        one_found = 0
        result = 0
        window_start = 0
        for i, x in enumerate(arr):
            if x == 1:
                one_found += 1
            if i - window_start + 1 > k + one_found:
                left_char = arr[window_start]
                if left_char == 1:
                    one_found -= 1
                window_start += 1
            result = max(result, i - window_start + 1)
        return result