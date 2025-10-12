
"""
Parenthesis Checker
*******************
Difficulty: EasyAccuracy: 28.56%Submissions: 699K+Points: 2
Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
An expression is balanced if:

Each opening bracket has a corresponding closing bracket of the same type.
Opening brackets must be closed in the correct order.
Examples :

Input: s = "[{()}]"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "[()()]{}"
Output: true
Explanation: All the brackets are well-formed.
Input: s = "([]"
Output: false
Explanation: The expression is not balanced as there is a missing ')' at the end.
Input: s = "([{]})"
Output: false
Explanation: The expression is not balanced as there is a closing ']' before the closing '}'.
Constraints:
1 ≤ s.size() ≤ 106
s[i] ∈ {'{', '}', '(', ')', '[', ']'}
"""


class Solution:
    def isBalanced(self, s):
        stack=[]
        pairs={')':'(',
               ']':'[',
               '}':'{',
               }

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or stack[-1] !=pairs[char]:
                    return False
                stack.pop()
        return len(stack)==0

obj=Solution()
print(obj.isBalanced("{([])}"))
        
