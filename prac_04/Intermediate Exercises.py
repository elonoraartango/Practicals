#1
numbers = []
for i in range (5):
    digit = int(input("Enter number: "))
    numbers.append(digit)

print("The first number is",numbers[0])
print("The last number is", numbers[4])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))

#2
usernames = ['jimbo', 'gilston98' 'derekf', 'Whatsup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("What is your username?")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")

