import random
import string

new_string = string.ascii_uppercase
a = [''.join(random.choice(new_string) for i in range(10)) ]
a.append(".txt")
filename = ''.join(a)
print(filename)

#print(filename)

#alternative solution found for file name so this module was not in use