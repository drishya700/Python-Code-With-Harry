# Repeat program 4 for a list of such words to be censored

words = ["Donkey","bad","ganda"]

with open("temporary.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#"*len(word))

with open("temporary.txt","w") as f:
    f.write(content)