# ==================================================
# Strings
# ==================================================

lineBreak = f"{30 * '-'}"

# 1. Reverse a String: Ask the user for a string and print it reversed

userString = input("Please enter a string: ")# .lower() # making it lower case just for ease of use, can use .casefold() for each individual case if you want to preserve individual string

print(lineBreak)

print("This is your string backwards: ", end = "")

def stringReverser(string) : # making function for purpose of palindrome checker

    i = len(userString)

    reverseString = ""

    while i > 0 : # does not need to be >= 0, as length of string array is narturally one less than length of string
        
        i -= 1
        #print(userString[i], end = "") # default ending character is a new line, make it blank to print on same line

        reverseString += userString[i]
        #print(i)

    return reverseString
    
reverseString = stringReverser(userString)
print(reverseString)

print(lineBreak)

# 2. Count vowels: Count the number of vowels in a user-provided sentence

# Use the same string input command from part 1 i.e. userString

vowels = ["a", "e", "i", "o", "u"]

x = int()

for i in userString :

    if i in vowels :

        x += 1

print(f"The number of vowels in {userString} is: {x}\n{lineBreak}")

# 3. Check Palindrome: Determine if the given string is a palindrome

if userString == reverseString :

    print(f"Your string is a palindrome! :D\n{lineBreak}")

else :

    print(f"Your string is not a palindrome! >:(\n{lineBreak}")

# 4. String Length Without Spaces: Count the number of characters, excluding spaces

y = int()

for i in userString :

    if i != " " :

        y += 1

print(f"The number of non-space characters in your string is: {y}\n{lineBreak}")

# 5. Uppercase Conversion: Convert a string to uppercase without using .upper() manually for each character

alphabetDict = {
    'a': 'A',
    'b': 'B',
    'c': 'C',
    'd': 'D',
    'e': 'E',
    'f': 'F',
    'g': 'G',
    'h': 'H',
    'i': 'I',
    'j': 'J',
    'k': 'K',
    'l': 'L',
    'm': 'M',
    'n': 'N',
    'o': 'O',
    'p': 'P',
    'q': 'Q',
    'r': 'R',
    's': 'S',
    't': 'T',
    'u': 'U',
    'v': 'V',
    'w': 'W',
    'x': 'X',
    'y': 'Y',
    'z': 'Z'
}

a = alphabetDict.items()
aK = alphabetDict.keys()
aV = alphabetDict.values()

upperString = ""

for i in userString :

    if i in aK :

        upperLetter = alphabetDict.get(i)
        upperString += upperLetter

    else :

        upperString += i

print(f"This is your string in upper case: {upperString}\n{lineBreak}")

# ==================================================
# If Statement
# ==================================================

# 1. Even or Odd: Ask for a number and determine if it's even or odd

evenOdd = int(input("Please enter a number: "))

if evenOdd % 2 == 0 :

    print("Your number is even.")

else :

    print("Your number is odd.")

print(lineBreak)

# 2. Leap Year Check: Check if a given year is a leap year

yearInput = int(input("Please enter a year: "))

if yearInput % 4 == 0 :

    print("This is a leap year.")

else :

    print("This is not a leap year.")

print(lineBreak)

# 3. Grade Calculator: Assign letter grades based on a numeric score (A, B, C...).

gradeLetters = ["A", "B", "C", "D", "F"]
gradeScores = [80, 70, 60, 50, 40]

testScore = int(input("Please enter your final test score: "))

for i in gradeScores :

    if testScore >= i :

        gradeIndex = gradeScores.index(i)
        grade = gradeLetters[gradeIndex]
        #print(grade)
        print(f"Your grade is {grade}")
        break

print(lineBreak)

# 4. Positive, Negative or Zero: Identify if a number is positive, negative, or zero.

pnz = int(input("Please enter a number: "))

if pnz > 0 :

    print("Your number is positive.")

elif pnz < 0 :

    print("Your number is negative.")

else :

    print("Your number is 0.")

print(lineBreak)

# 5. Max of Three: Take three numbers and print the greatest.

numberOne = int(input("Please enter your first number: "))
numberTwo = int(input("Please enter your second number: "))
numberThree = int(input("Please enter your third number: "))

if numberOne > numberTwo :

    if numberOne > numberThree :

        print(f"{numberOne} is the biggest number.")

    elif numberOne == numberThree :

        print(f"{numberOne} and {numberThree} are the two biggest numbers.")

    else :

        print(f"{numberThree} is the biggest number.")

elif numberOne < numberTwo :

    if numberTwo > numberThree :

        print(f"{numberTwo} is the biggest number.")

    elif numberTwo == numberThree :

        print(f"{numberTwo} and {numberThree} are the two biggest numbers.")

    else :

        print(f"{numberThree} is the biggest number.")

else :

    if numberOne > numberThree :

        print(f"{numberOne} and {numberTwo} are the two biggest numbers.")

    elif numberOne == numberThree :

        print(f"All three numbers are the same.")

    else :

        print(f"{numberThree} is the biggest number.")

print(lineBreak)

# ==================================================
# Function
# ==================================================

# 1. Sum of Two Numbers: A function that returns the sum of two numbers

def addition(x, y) :

    totalSum = x + y

    return totalSum

# numberOne, numberTwo = input("Enter 2 numbers: ").split()

# numberOne, numberTwo = [int(numberOne), int(numberTwo)] # this is a bit more efficient but is more reliant on user input, so im hashing it out for now and might come back to it later

numberOne = int(input("Enter your first number: "))
numberTwo = int(input("Enter your second number: "))

#print(numberOne, numberTwo)

totalSum = addition(numberOne, numberTwo)
print(totalSum)
print(lineBreak)

# 2. Factorial: Write a function to return the factorial of a number.

def factorialCalculator() :

    factorialInput = int(input("Please enter a number: "))

    for x in range(1, factorialInput) :

        factorialInput *= x

    return factorialInput

factorialOutput = factorialCalculator()
print(factorialOutput)
print(lineBreak)

# 3. Check Prime: Write a function to check if a number is prime.

def primeChecker() :

    primeInput = int(input("Please enter a number: "))

    checker = 0

    while checker < 2 :

        for x in range(1, primeInput // 2) :

            if primeInput % x == 0 :

                checker += 1
        break

    if checker < 2 :

        return "Prime"
    
    else :

        return "Not prime"

primeOutput = primeChecker()
print(primeOutput)
print(lineBreak)

# 4. Greeting Function: Accept a name and return a personalized greeting.

nameInput = input("Please enter your name: ")

def greetingFunction(name) :

    return f"Hello, {name}!"

greetingMessage = greetingFunction(nameInput)
print(greetingMessage)
print(lineBreak)

# 5. Area of Circle: Function to compute area of a circle from the radius.

radius = int(input("Enter the radius of your circle: "))

def circleArea(radius) :

    return 3.14 * radius ** 2

area = circleArea(radius)
print(area)
print(lineBreak)

# ==================================================
# While Loop
# ==================================================

# 1. Countdown Timer: Countdown from a user-input number to 0.

countdownTimer = int(input("Enter a time to countdown from: "))

while countdownTimer >= 0 :

    print(countdownTimer)
    countdownTimer -= 1

print(lineBreak)

# 2. Sum Until Zero: Keep adding user-entered numbers until 0 is entered.

totalValue = int()
userInput = None

while userInput != 0 :

    userInput = int(input("Pick a number to add to your total: "))
    totalValue += userInput
    print(f"Your total value is: {totalValue}")

# 3. Password Retry: Ask for a password until the correct one is entered.

password = "London"
userPassword = ""

while userPassword != password :

    userPassword = input("Please enter your password: ")

print("Congratulations! You got the password correct.")

# 5. Print Even Numbers: Print even numbers less than 20 using a while loop.

i = 20

while i <= 20 and i > 0 :

    i -= 1

    if i % 2 == 0 :

        print(i)

    else :

        continue