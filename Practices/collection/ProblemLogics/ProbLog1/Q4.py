num  = int(input("Enter a number: "))
if num % 4 == 0 and num %8 != 0:
    print(f"{num} is divisible by 4 but not by 8")
else:
    print(f"{num} is either not divisible by 4 or divisible by 8")  