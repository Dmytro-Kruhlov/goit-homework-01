from sort import categorize


print(categorize('1.jpeg'))
print(categorize('1.exe'))
print(categorize('1.exe.mp3'))
print(categorize('1'))
print(categorize('1.exe.qewr.jpeg!exe'))
print(categorize('1!jpeg'))

assert categorize('1.jpeg') == 'images'