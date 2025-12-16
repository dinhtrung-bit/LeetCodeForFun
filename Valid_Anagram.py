def isAnagram(s,t):
    if s[::-1] == t:
        print(s[::-1])
        return True 
    return False 
s = str(input())
t=str(input())
print(isAnagram(s,t))