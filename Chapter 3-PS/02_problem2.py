#  Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>


letter = '''Dear <|Name|>,
            You are selected!
             <|Date|>'''

print(letter.replace("<|Name|>","Drishya").replace("<|Date|>","11th  October"))

#the .replace function can be chained and used multiple times in a same sentence as I have used above. This is knowmn as function chaining
