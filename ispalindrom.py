def palindrome(string):
    for i in range(int(len(string)/2)):
        if string[i]!=string[len(string)-i-1]:
            return False
        return True

if palindrome("SaS"):
    print("Palindrom")
else:
    print("Not a plaindrom ")