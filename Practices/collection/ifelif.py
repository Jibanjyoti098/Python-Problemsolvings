# n1 = int(input("Enter a num1: "))
# n2 = int(input("Enter a num2: "))
# n3 = int(input("Enter a num3: "))
# if n1>n2 and n1>n3:
#     print(f"The number n1 = {n1} is greatest.")
# elif n2>n1 and n2>n3:
#     print(f"The number n2 = {n2} is greatest.")
# elif n3>n2 and n3>n1:
#     print(f"The number n3 = {n3} is greatest.")


# n1 = int(input("Enter a num1: "))
# n2 = int(input("Enter a num2: "))
# n3 = int(input("Enter a num3: "))
# if n1<n2 and n1<n3:
#     print(f"The number n1 = {n1} is smallest.")
# elif n2<n1 and n2<n3:
#     print(f"The number n2 = {n2} is smallest.")
# elif n3<n2 and n3<n1:
#     print(f"The number n3 = {n3} is smallest.")


ch = input("Enter character: ")
rem = 0
asc = 0
if 'a'<= ch <= 'z':
    ch = ch.upper()
    print(f'The upper case of ch is {ch}.')
elif 'A'<= ch <= 'Z':
    ch = ch.lower()
    print(f'The lower case of ch is {ch}.')
elif '0'<= ch <= '9':
    rem = int(ch)%3
    print(f'The reminder of ch is {rem}.')
else:
    asc = ord(ch)
    print(f"The ASCII value of ch is {asc}")

