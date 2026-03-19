# Question1:
x = 1
y = 0
print(x and y or x)
#O/P: 1

# Question2:
print(10 < 20 < 30 == True)
# O/P: True Correct ans is  "False"

# Question3:
# a = 5
# b = a += 3
# print(b)
#O/P: 8 Correct is "Syntax Error"
#ModifiedOne:
a = 5
a += 3
b = a
print(b)
#O/P: 8

# Question4:
for i in range (3):
    i += 1
    print("X")
# O/P: 3

# Question5:
x = 0
y = 10
while y > x:
    y -= x
    x += 1
print(x, y)
# O/P: x = 4, y = 4