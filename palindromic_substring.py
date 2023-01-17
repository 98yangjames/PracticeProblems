s = "abc"
output = 3

def countStrings(s):
    res = 0
    left = 0
    right = 0
    for i in range(len(s)):
        
        #Even values
        left = right = i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -=1
            right += 1
        #Odd strings
        left = i
        right = i + 1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -=1
            right += 1
    return res

print(countStrings(s) == output)