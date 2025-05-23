class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        print(len(s))
        while left < right:
            s[left], s[right] = s[right], s[left]
            print(left, right)
            left += 1
            right -= 1


# Example usage
if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    solution = Solution()
    solution.reverseString(s)
    print(s)  # Output: ['o', 'l', 'l', 'e', 'h']
