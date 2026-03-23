# Task 1
num = input("Enter a number: ")
start = input("Enter start: ")
end = input("Enter end: ")

if num.isdigit() and start.isdigit() and end.isdigit():
    num = int(num)
    start = int(start)
    end = int(end)

    if start <= num <= end:
        print("True")
    else:
        print("False")
else:
    print("Please enter digits.")


# Task 2
age = int(input("Enter your age: "))
haveCopun = input("Do you have a copun? (y/n): ").lower()
if(age < 18 or age > 65 or haveCopun == 'y'):
    print("True")
else:
   print("False")

# Task 3
name = input("Enter your name: ")
print("Hello " + name + "!")

# Task 4
full_name = str(input("Enter your full name: "))
names = full_name.split()
print(names[0][0] + " " + names[-1][0])

# Task 5
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(name + " is " + str(age) + " years old.")