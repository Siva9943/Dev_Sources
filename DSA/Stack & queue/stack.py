from collections import deque
arr=[2,4,6,3,8,4,9]
stack=[]
q=deque()
#stack
for i in arr:
    stack.append(i)
    q.append(i)
#print(stack)
#print(q)
#q.popleft()
#print(q)

p=map(lambda x : stack.append(x) , q)
print(list(p))



