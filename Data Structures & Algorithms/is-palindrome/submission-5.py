class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []

        for c in s:
            if (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122) or (48 <= ord(c) <= 57):
                res.append(c.lower())  # convert to lowercase immediately

        for i in range(len(res)):
            if res[i] != res[len(res) - 1 - i]:  # no need to lower again
                return False

        return True