letter = '''Dear <|Name|>,
            You are selected!
             <|Date|>'''

print(letter.replace("<|Name|>","Drishya").replace("<|Date|>","11th  October"))

#the .replace function can be chained and used multiple times in a same sentence as I have used above. This is knowmn as function chaining
