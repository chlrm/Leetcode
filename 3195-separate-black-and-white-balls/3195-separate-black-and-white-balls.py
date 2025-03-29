class Solution:
    def minimumSteps(self, s: str) -> int:
        arr = list(s)
        n = len(arr)
        swaps = 0
        black_position = n - 1
        for i in range(n - 1, -1, -1):
            if arr[i] == '1':
                swaps += black_position - i
                black_position -= 1    
        return swaps