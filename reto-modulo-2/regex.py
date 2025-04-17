#import regex
import re


regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$'
usar_expresion = re.match(regex, 'alcides@gmail.com')
print(bool(usar_expresion))