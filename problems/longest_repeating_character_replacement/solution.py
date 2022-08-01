class Solution:
    def characterReplacement(self, arr: str, k: int) -> int:
        c_dict = dict()
        max_ct_prev = 0
        result = 0
        window_start = 0
        for i, x in enumerate(arr):
            if x not in c_dict:
                c_dict[x] = 0
            c_dict[x] +=1
            max_ct_prev = max(max_ct_prev, c_dict[x])
            if i - window_start + 1 > k + max_ct_prev:
                left_char = arr[window_start]
                c_dict[left_char] -= 1
                window_start += 1
            result = max(result, i - window_start + 1)
        return result