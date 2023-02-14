def vaild_parantheses(s):
    map = { ']': '[', '}': '{', ')': '(' }
    stack = []
    for l in s:
        if l in map and len(stack) > 0:
            if map[l] != stack.pop(len(stack)-1):
                
                return False
            
        else: 
            stack.append(l)

    if len(stack) > 0:
        return False
    return True
    """
    a = 0
    parantheses = {'[':']','{':'}','(':')'}
    for i in range(len(s)):
        if s[i] in parantheses.keys():
            for j in range(i+1,len(s)):
                if s[j] == parantheses.get(s[i]):
                    a+=1
        
    if a == len(s)/2:
        return True
    else:
        return False
    """


print(vaild_parantheses(input("Enter parantheses:")))
