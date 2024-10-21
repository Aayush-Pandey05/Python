# replace <|Name|> and <|Date|> in the program given below with custom input

letter= ''' Dear <|Name|>,
 you are selected!
<|Date|>'''
print(letter.replace("<|Name|>", "Aayush").replace("<|Date|>","05/09/24"))# here we replaced name with our custom name and then we used .replace chaining and replaced date as well