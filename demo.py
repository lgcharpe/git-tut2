def stringrot(string):
    for char in string:
        yield chr(ord(char) + 13)


print("Hello, normal World!")
print("Hello Human!")

print(stringrot("something"))
for foo in stringrot("something"):
    print(foo)
