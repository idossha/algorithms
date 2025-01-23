'''

Given an integer x, return true if x is a palindrome, and false otherwise.

Jan23, 2025

'''


def isPalindrome(x):
    
    if x < 0:
        return False
 
    x_str = str(x)
    return x_str == x_str[::-1]




list  = [121, 0, -121, 77, 78]

for i in list:
    print(f"is {i} a Pilandrome? {isPalindrome(i)}")
