def stringrot(string):
    for char in string:
        yield chr(ord(char) + 13)

print("Hello, normal World!")
print("Hello Human!")
