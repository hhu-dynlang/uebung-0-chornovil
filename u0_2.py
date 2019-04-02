def is_palindrom(text):
    len1 = int(len(text)/2)
    for i in range(len1):
        if text[i] != text[len(text)-i-1]:
            return False
    return True

print(is_palindrom("yoy"))
print(is_palindrom("yo"))
