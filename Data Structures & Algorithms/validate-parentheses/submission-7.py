class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        brace={"}":"{","]":"[",")":"("}

        for c in s: #[ ( ]
            if c in brace: 
                if stack and stack[-1]==brace[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) #[( ]
        return True if not stack else False