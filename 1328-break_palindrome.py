def breakPalindrome(palindrome):
    n = len(palindrome)
    if n == 1: return ""
    for i in range(len(palindrome)//2):
        if palindrome[i] != 'a':
            return palindrome[:i] +"a"+palindrome[i+1:]
     
    return palindrome[:-1] + "b"

print(breakPalindrome("bdb"))