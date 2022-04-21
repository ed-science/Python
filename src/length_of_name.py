name = input("Enter your name: ")

length = len(name)

print(f"The length of your name is: {length}")

if length < 4:
    print("The name is less than 4 characters")

elif length < 10 :
    print("The name is greater than 4 but less thank 10")
else:
    print("The name is very long")
