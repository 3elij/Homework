# #  A college offers a course that prepares students for the state licensing exam for real
# # estate brokers. Last year, several of the students who completed this course took the
# # licensing examination. The college wants to know how well its students did on the
# # exam. You have been asked to write a program to summarize the results. You have
# # been given a list of these 10 students. Next to each name is written a 1 if the stu
# # dent passed the exam and a 2 if the student failed.
# # Your program should analyze the results of the exam as follows:
# # 1. Input each test result (i.e., a 1 or a 2). Display the message “Enter result”
# # each time the program requests another test result.
# # 2. Count the number of test results of each type.
# # 3. Display a summary of the test results indicating the number of students who
# # passed and the number of students who failed.
# # 4. If more than eight students passed the exam, display “Bonus to instructor 


# counter = 0
# passes = 0
# fail = 0
# total = 0
# result = int(input("Input a '1' if the student passed, and a '2' if the student failed: "))
# while counter < 9:
#     if result == 1:
#         passes+=1
#         counter+=1
#     elif result == 2:
#         fail+=1
#         counter+=1
#     else:
#        result = int(input("Invalid Input. Input 1 for a pass and 2 for a fail: "))
#     result = int(input("Input 1 for a pass and 2 for a fail: "))
    
        
# print(f"{passes} students passed and {fail} students failed")
# if passes >= 8:
#     print("Bonus to the instructor")

# for row in range(2):
#     for column in range(7):
#         print('@',end='')
#     print()

# print('Enter two integers, and I will tell you the relationships they satisfy.')
# number1 = int(input('Enter first integer: '))
# number2 = int(input('Enter second integer: '))
# if number1 == number2:
#     print("They are equal")
# elif number1 > number2:
#     print(f"{number1} is bigger than {number2}")
# elif number1 < number2:
#     print(f"{number2} is bigger than {number1}")

# answer = input("Wht is your problem")
# response = input("Have you had this problem before(yes or no)")
# if response == 'yes':
#     print("Well you have it again")
# elif response == 'no':
#     print("Well you have it now")
# else:
#     print("Invalid input")

# table_length = int(input("How long do you want the table to be: "))
# number = 0
# print("NUMBER\tSQUARE\tCUBE")
# for column in range(0, table_length+1):
#     print(number,number**2,number**3, sep='\t')
#     number+=1

# total = 0
# product = 1

# for count in range(4):
#     number = int(input("Input a number: "))
#     total+=number
#     product*=number
#     if count == 0:
#         min = number
#         max = number
#     if min > number:
#         min = number
#     if max < number:
#         max = number
# print(f"The total is {total}")
# print(f"The average is {total/4}")
# print(f"The product is {product}")
# print(f"The largest number is {max}")
# print(f"The smallest number is {min}")

# num = int(input("Input a 5 digit integer: "))
# holder = 0
# divisor = 10000
# while num != 0:
#     holder = num//divisor
#     num = num%divisor
#     divisor//=10
#     print(f"{holder}", end=' ')

# money = int(input("How much money did you Invest in $: "))
# for counter in range(30):
#     money = money*((1+0.07)**counter)
#     if counter > 0:
#         print(f"In year {counter}, you have ${money:.2f}")

# miles = int(input("How many miles did you drive: "))
# gallons = int(input("How many gallons did you use(-1 to end): "))
# while gallons != -1:
#      g_per_m = gallons/miles
#      print(f"You consumed {g_per_m:.2f} gallons per mile")
#      miles = int(input("How many miles did you drive: "))
#      gallons = int(input("How many gallons did you use(-1 to end): "))

#  A palindrome is a number, word or text phrase that reads the same
# backwards or forwards. For example, each of the following five-digit integers is a palindrome
#: 12321, 55555, 45554 and 11611. Write a script that reads in a five-digit integer
# and determines whether it’s a palindrome. [Hint: Use the // and % operators to separate
# the number into its digits.]

# num = int(input("Input a 5 digit number: " ))
# number_reduced = 0
# last_digit = 0
# penultimate_number_finder = num//10
# second_digit_finder = num%10000
# if (num//10000) == (num%10) and (second_digit_finder//1000) == (penultimate_number_finder%10):
#     print("The number is a palindrome")
# else:
#     print("This number is not a palindrome")

# number = int(input("Input a number: "))
# running_total = 1
# for counter in range(1,number+1):
#     running_total = running_total*counter
# print(f"{number}! = {running_total}")

# num = 4
# denominator = -3
# print("NUMBER\tApproximation")
# print(f"1\t{num}")
# for counter in range(1,10)
#     print(counter,() sep='/t')
#     denominator = (denominator)

# running_total = 1
# upper_limit = int(input("What degree of approximation do you want euler;s to be to: "))
# eulers = 1
# for counter in range(1,upper_limit+1):
#     running_total = running_total*counter
#     eulers = eulers+ (1/running_total)
# print(f"The approximation of Eulers constant to {upper_limit} iterations is {eulers}")

# biggest = 0
# second_biggest = 0
# for counter in range(1,11):
#     number = int(input("Input a number: "))
#     if biggest < number:
#         biggest = number
#     elif second_biggest < number and second_biggest < biggest:
#         second_biggest = number
# print(biggest, second_biggest)


# for counter in range(1,6):
#     for counter1 in range(0,counter):
#         print("*", end='')
#     print()

# for counter in range(1,6):
#     for counter2 in range(6-counter,0,-1):
#         print("*", end='')
#     print()
# for counter in range(1,6):
#     for counter3 in range(0,counter-1):
#         print(" ", end='')
#     for counter4 in range(6-counter,0,-1):
#         print("*", end='')
#     print()

# for counter in range(1,6):
#     for counter5 in range(6-counter,0,-1):
#         print(" ", end='')
#     for counter6 in range(0,counter):
#          print("*", end='')
#     print()

# for counter in range(1,6):
#     for counter1 in range(0,counter):
#         print("*", end='')
#     print(end='\t')
#     for counter2 in range(6-counter,0,-1):
#         print("*", end='')
#     print(end='\t')
#     for counter3 in range(0,counter-1):
#         print(" ", end='')
#     for counter4 in range(6-counter,0,-1):
#         print("*", end='')
#     print(end='\t')
#     for counter5 in range(6-counter,0,-1):
#         print(" ", end='')
#     for counter6 in range(0,counter):
#          print("*", end='')
#     print(end='\t')
#     print()

total = 0
limit = int(input("How many numbers do you want to go up to: "))
for counter in range(1,limit+1):
    for counter1 in range(counter,limit+1):
        total = (counter**2)+(counter1**2)
        for counter2 in range(1,limit+1):
            if total == (counter2**2):
                print(f"{counter},{counter1},{counter2}")





        
















