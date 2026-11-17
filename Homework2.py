#2.3
grade = int(input("What was your score: "))
if grade >= 90:
    print("Congratulations")
else:
    print("You'll get it next time")
#2.4
print(27.5 + 2)
print(27.5 - 2)
print(27.5 * 2)
print(27.5 / 2)
print(27.5 // 2)
print(27.5 ** 2)
#2.5
print("radius of the circle is 2")
area = 3.14159*4
circumference = 2*2*3.14159
diameter = 2*2
print(circumference)
print(area)
print(diameter)
#2.6
integer = int(input("Input a number: "))
if integer%2 == 0:
    print("This is an even number")
elif integer%2 != 0:
    print("This is an odd number")
else:
    print("Invalid input")
#2.7
int1 = int(input("Input a number: "))
if int1%4 == 0 and int1%2 == 0:
    print("Your number is a multiple of 2 and 4")
elif int1%2 == 0:
    print("Yout number is a multiple of 2")
elif int1%4 == 0:
    print("Yout number is a multiple of 4")
else:
    print("Your number isn't a multiple of 2 or 4")
#2.8
print("We are going to be printing a table with the value of the squares and cubes of 0 to 5")
print("number\tsquare\tcube")
print("0\t0\t0")
print("1\t1\t1")
print("2\t4\t8")
print("3\t9\t27")
print("4\t16\t64")
print("5\t25\125")
#2.9
ord('B')
ord('C')
ord('D')
ord('0')
ord('$')
#2.10
a = int(input("Enter a number"))
b = int(input("Enter a number"))
c = int(input("Enter a number"))
sum = a+b+c
product = a*b*c
print("Largest number is: ", max(a, b, c))
print("Smallest number is: ", min(a, b, c))
print("Sum is: ", sum)
print("Product is: ", product)
#2.11
number = int(input("Input a 5 digit"))
digit1 = number//10000
number = number%10000
digit2 = number//1000
number = number % 1000
digit3 = number // 100
number = number % 100
digit4 = number // 10
digit5 = number % 10
print (digit1   digit2   digit3  digit4  digit5)
#2.12
print("The orignal amount of money investedwas $1000. We will find out how much you have after 10, 20 and 30 years")
print("The rate is at 7%")
initial = int(1000)
final1 = initial*((1+0.07)**10)
final2 = initial*((1+0.07)**20)
final3 = initial*((1+0.07)**30)
print(f"The total after 10 years was {final1}.\nThe total after 20 years was {final2}. \nThe total after 30 years was {final3}")
#2.13 Size limit checker
print(3000000**20)
#2.14 Heart Rate calculator
age = int(input("How old are you: "))
max_bpm = 220-age
range1 = 0.5*max_bpm
range2 = 0.85*max_bpm
print(f"You are {age} years old. Your max bpm is {max_bpm}. The safe heart range is {range1} bpm - {range2} bpm")
print("These formulas are estimates provided by the AHA; maximum and target heart rates may vary based on the health, fitness and gender of the individual. Always consult a physician or qualified healthcare professional before beginning or modifying an exercise program.")
#2.15 Some rubbish
a = int(input("Input an integer"))
b= int(input("Input an integer"))
c = int(input("Input an integer"))
if a > b and a > c 


    



