num = eval(input("Enter num: "))
if type(num) == float:
    print("Its float")

data = eval(input("enter data: "))
li = [int, float, complex, bool]
if type(data) in li:
    print("Its SVD")

char = input("Enter Char: ")
if type(int(char)) == int :
    print("Its an integer")

val = int(input("Enter value: "))
if val%3==0:
    print("It's multiply by 3")
