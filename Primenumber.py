prime=int(input("enter your number"))

for i in range (2,prime):
    if prime%i ==0:
        print(prime,"its not a prime number")
        break
    else:
        print(prime,"its a prime number")

# Factorial=int(input("enter number"))
# num=1
# for i in range(1,Factorial+1):
#     num=num*i
#
# print(num)

# reverse = input("Enter your name: ")
# reverse="lohith"
# new = ""
#
# for i in reverse:
#     new = i + new
#
# print(new)
#
# #
reverse = ["lojhi "]
new = []

for i in reverse:
    string = ""
    for char in i:
        string = char + string
    new.append(string)  # Append the fully reversed string after the inner loop

print(new)

numbers = [5, 10, 3, 8, 15]
max_number = numbers[0]  # Initialize max_number with the first element of the list

for num in numbers:
    if num > max_number:
        max_number = num

print(max_number)



