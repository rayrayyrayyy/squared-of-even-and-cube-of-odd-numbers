# Ray Allessandra D. Pacis | BSCPE 1-5
# Write a method in python that will create two separate text files after reading the source text file named integers.txt that contains 20 integers. 
# The first output file will be named double.txt containing the square of all even integers found in integers.txt.
# The second file will be named triple.txt containing the cube of all odd numbers found in the integers.txt.

# import modules for design
import pyfiglet
from termcolor import colored, cprint
import time
from colorama import Fore, Back, Style

print_grey = lambda x: cprint(x, 'grey')
print_yellow = lambda x: cprint(x, 'yellow')

# intro
hi_welcome = pyfiglet.figlet_format("Welcome User!", font = "doom", width = 150, justify = "center")
print(Fore.YELLOW + hi_welcome)
print(Style.RESET_ALL)
print(Fore.BLUE + "="*150)
instruction = "INSTRUCTION: Please enter 20 random integers and if it's even I will find its squared and if it's odd I'll cube it.☺"
instruction_center = instruction.center(150)
print(instruction_center)
print(Fore.BLUE + "="*150)
print(Style.RESET_ALL)

# open file integers.txt(write)
with open("integers.txt", 'w') as input_file:

    # create loop
    i = 0
    while (i < 20):
        # ask user for numbers
        user_numbers = input("\t\tPlease write a number: ")
        # put the numbers to integers.txt
        input_file.write((user_numbers) + '\n')
        i += 1

# open files integers.txt(read), double.txt(write), and triple.txt(write)
with open("integers.txt", 'r') as integers_file, open("double.txt", 'w') as even_squared, open("triple.txt", 'w') as odd_cube:
    # read integers.txt by line
    for line in integers_file:
        user_num = int(line)
            
        # if extracted number is even
        if user_num % 2 == 0:
            # extracted number will be squared
            squared_number = user_num ** 2
            # write squared number to double.txt
            even_squared.write(str(squared_number) + '\n')

        # else if the extracted number is odd
        if user_num % 2 == 1:
            # extracted number will be cubed
            cubed_number = user_num ** 3
            # write cubed number to triple.txt
            odd_cube.write(str(cubed_number) + '\n')

# outro
print('\n' + Fore.YELLOW + Style.BRIGHT + "-"*150)
done = pyfiglet.figlet_format("Thank you!", font = 'doom', width = 150, justify = 'center')
print_yellow(done)
note = "See text files for results"
print_grey(Fore.YELLOW + '-'*62 + note + '-'*62 + '\n') 

# end of program
