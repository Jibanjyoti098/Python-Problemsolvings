print('Int To Others\n')
# Int to Others
print(int(10.5))
# print(int('10.5'))#Invalid
print(int('10'))
# print(int('string')) #Invalid
print(int(True))
# print(int(10+20j))#Invalid

print("Float To Others\n")
# Float to Others
print(float(10))
print(float('10'))
print(float('10.5'))
# print(float('string')) #Invalid
print(float(True))
# print(float(10+20j))#Invalid

print("String To Others\n")
# String to others
print(str(10))
print(str(10.23))
print(str(True))
print(str(10+20j))

print("Complex To Others\n")
# Complex to Others
print("Form 1: \n")
print(complex(10))
print(complex('10'))
print(complex('10.5'))
# print(complex('string')) #Invalid
print(complex(True))

print("Form 2: \n")
print(complex(10,20))
# print(complex('10','20')) #Invalid
print(complex(True, False))
print(complex(10.5, 30.5))

print("Boolean To Others\n")
#Bool to Others
print(bool(10))
print(bool("10"))
print(bool(1))
print(bool(10+20j))
print(bool(" "))
print(bool("False"))
print(bool(True))
# False
print(bool(0))
print(bool())
print(bool(""))
print(bool(False))
