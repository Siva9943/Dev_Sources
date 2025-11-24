class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={
            ")":"(",
            "]":"[",
            "}":"{",
        }
        stack=[]
        for i in s:
            if i not in hashmap:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    popped=stack.pop()
                    if popped!=hashmap[i]:
                        return False
        return len(stack)==0


obj=Solution()
s="[]"
result=obj.isValid(s)
print(result)
