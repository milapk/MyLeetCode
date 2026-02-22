class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []

        def backtracking(i, currentStr):
            if len(currentStr) == len(digits):
                result.append(currentStr)
                return
            for char in letters[digits[i]]:
                backtracking(i + 1, currentStr + char)
        if digits:
            backtracking(0, '')
        return result