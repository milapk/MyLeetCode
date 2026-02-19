"""
I ACTUALLY GOT DID THIS ONE, NO HINTS NO VIDEOS NOT EVEN A GOOGLE SEARCH JUST PURE SKILL
PRESSED THE SUMBIT BUTTON AND IT RAN LIKE CLOCKWORK, I COULDNT BELIEVE MY EYES
LOOK HOW NICE IT ALSO LOOKS WOWWOWOWOW ACTUALLY PROUD OF THIS ONE
SHOUTOUT TO ANYONE WHOS ACTUALLY READING THIS, U DA REAL GOATTT
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(string, i, openP):
            if len(string) == n * 2:
                if openP <= 0:
                    result.append(string)
                return
            backtrack(string + "(", i - 1, openP + 1)
            if openP >= 1:
                backtrack(string + ")", i + 1, openP - 1)
        backtrack("", n, 0)
        return result