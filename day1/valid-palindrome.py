class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # 左のポインターが英数字でない場合は進める
            while left < right and not s[left].isalnum():
                left += 1
            # 右のポインターが英数字でない場合は戻す
            while left < right and not s[right].isalnum():
                right -= 1

            # 小文字化して比較
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# Example usage
if __name__ == "__main__":
    s = " "
    solution = Solution()
    ex = solution.isPalindrome(s)
    print(ex)
