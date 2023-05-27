manu = 3
Manu = 7

a1 = "manu" \
    "is a good boy"
a2 = "manu" \
    'is a good boy'
a3 = '''Manu
is a good boy
'''
# a1[0] = "man"  # String is immutable and hence this line throws an error
print(a1 + a2 + a3)