import random
import signal
from rich import print

#This program will present you with challenges to convert numbers between bases and perform logical operations.
#This program goes along with the following youtube video.  


#Turn off Keyboard Interrupts
signal.signal(signal.SIGINT, signal.SIG_IGN)

# Helper function to create conversion functions for different number bases.
def make_conversion_function(choose_from, prompt_text, input_conversion):
    def convert_function():
        the_number = random.choice(choose_from)
        try:
            answer = input(eval(prompt_text))
        except (KeyboardInterrupt, EOFError):
            return "EXIT", ""
        except Exception as e:
            return False, ""
        if answer.lower() == input_conversion(the_number).lower():
            return True, ""
        return False, input_conversion(the_number)
    convert_function.operation = prompt_text
    return convert_function

# List of numbers close to base 2 for binary to decimal and vice versa conversion exercises.
close_to_base2 = [128, 64, 32, 16, 130, 131, 132, 133, 65, 66, 67, 68, 33, 34, 35, 36, 127, 63, 31, 15]

# Create conversion functions for binary to decimal (bin2dec1) and decimal to binary (dec2bin1) with close-to-base2 numbers.
bin2dec1 = make_conversion_function(
    close_to_base2,
    'f"What is 0b{the_number:08b} in decimal? (Answer Format: 999): "',
    input_conversion=str
)

dec2bin1 = make_conversion_function(
    close_to_base2,
    'f"What is {the_number} in binary? (Answer Format: 0b11111111): "',
    input_conversion=lambda num: f'0b{num:08b}'
)

# Create conversion functions for binary to decimal (bin2dec2) and decimal to binary (dec2bin2) with numbers from 0 to 255.
bin2dec2 = make_conversion_function(
    range(256),
    'f"What is 0b{the_number:08b} in decimal? (Answer Format: 999): "',
    input_conversion=str
)

dec2bin2 = make_conversion_function(
    range(256),
    'f"What is {the_number} in binary? (Answer Format: 0b11111111): "',
    input_conversion=lambda num: f'0b{num:08b}'
)

# Create conversion functions for decimal to hexadecimal (dec2hex) and hexadecimal to decimal (hex2dec) with numbers from 0 to 255.
dec2hex2 = make_conversion_function(
    range(256),
    'f"What is {the_number} in hexadecimal? (Answer Format: 0xFF): "',
    lambda num: f"0x{num:02x}",
)

hex2dec2 = make_conversion_function(
    range(256),
    'f"What is 0x{the_number:02x} in decimal? (Answer Format: 999): "',
    str
)

# Create easy versions of decimal to hexadecimal (dec2hex) and hexadecimal to decimal (hex2dec) with numbers from 0 to 255.
dec2hex1 = make_conversion_function(
    close_to_base2,
    'f"What is {the_number} in hexadecimal? (Answer Format: 0xFF): "',
    lambda num: f"0x{num:02x}",
)

hex2dec1 = make_conversion_function(
    close_to_base2,
    'f"What is 0x{the_number:02x} in decimal? (Answer Format: 999): "',
    str
)

# Create conversion function for hexadecimal to binary (hex2bin) with numbers from 0 to 255.
hex2bin = make_conversion_function(
    range(256),
    'f"What is 0x{the_number:02x} in binary? (Answer Format: 0b11111111): "',
    lambda num: f"0b{num:08b}"
)

# Create conversion function for binary to hex (bin2hex)) with numbers from 0 to 255.
bin2hex = make_conversion_function(
    range(256),
    'f"What is 0b{the_number:08b} in hexadecimal? (Answer Format: 0xFF): "',
    lambda num: f"0x{num:02x}"
)

# Define logical operation functions for AND, OR, XOR, NAND, NOR, and NXOR.
def logic_operation(op, negate_num2=False):
    def op_function(num1=None, num2=None):
        num1 = num1 or random.randrange(0,256)
        num2 = num2 or random.randrange(0,256)
        negate_text = ""
        if negate_num2 == True:
            negate_text = "NOT"
        try:
            answer = input(f'\nSolve:    {num1:#010b}\n{op+" "+negate_text: >9s} {num2:#010b}\n      ==> ')
        except (KeyboardInterrupt, EOFError):
            return "EXIT",""
        except:
            return False, correct
        if negate_num2 == True:
            num2 = 0b11111111 - num2
        correct = format(eval(f"{num1} {op} {num2}"), '#010b')
        if answer == correct:
            return True, ''
        else:
            return False, correct
    return op_function

and_operation = logic_operation("&")
or_operation = logic_operation("|")
xor_operation = logic_operation("^")
nand_operation = logic_operation("&", True)
nor_operation = logic_operation("|", True)
nxor_operation = logic_operation("^", True)

# Function to present random conversion or logical operation challenges to the user.
def func_choice(funclist, iterations=20, strikes=3, reset=2, finished=False):
    correct = 0
    incorrect = 0
    completed_symbol = "√"
    incompleted_symbol = " "
    strike_symbol = "X"
    if finished:
        print("Back for more practice! Excellent!")
    while correct < iterations:
        print(f"[[white on green]{completed_symbol * correct}[/][black on white]{incompleted_symbol*(iterations-correct)}[/]][[white on red]{strike_symbol*incorrect}[/][black on white]{' ' * (strikes-incorrect)}[/]]", end=" ")
        choice = random.choice(funclist)
        result, ans = choice()
        if result == "EXIT":
            return "EXIT"
        if result:
            correct += 1
            print(f"\n\n[bold green]Correct![/bold green] Total Correct Answers: {correct} of {iterations}")
            print(f"Mistakes before penalty: {strikes - incorrect} remaining.\n")
            #print_score(correct, iterations, incorrect,strikes )
        else:
            incorrect += 1
            #print_score(correct, iterations, incorrect,strikes )
            print(f"\n\n[bold red]Incorrect.[/bold red] The correct answer is {ans}")
            print(f"[bold red]{incorrect}[/bold red] strikes used and [bold green]{strikes - incorrect}[/bold green] remaining.\n\n")
        if incorrect >= strikes:
            print("Sorry. You missed too many. Assessing a penalty.")
            incorrect = 0
            if reset == 0:
                print(f"Starting back over from the beginning. You need to get {iterations} answers correct.\n\n")
                correct = 0
            else:
                print(f"You need some more practice. Increasing required challenges by {reset}!\n\n")
                iterations += reset
    else:
        return True
    return False

# Main menu and user interaction.
print("Welcome! I hope you find these exercises helpful. I know in my career the ability to perform base conversions and logical operations quickly in my head has been very useful.\n")
print("The number of required completed questions and mistakes allowed (strikes) changes for each lab. Your current status is printed in the square brackets as [completed/remaining]:[strikes before penalty]\n")

# Define the menu options and corresponding challenges.
menu_options = {
    "Decimal To Binary (easy)": [[dec2bin1], 5, 2, 2, False],
    "Decimal To Binary (hard)": [[dec2bin2], 10, 2, 4, False],
    "Decimal To Hex (easier)": [[dec2hex1], 5, 2, 2, False],
    "Decimal To Hex (hard)": [[dec2hex2], 5, 2, 4, False],
    "Binary to Decimal (easy)": [[bin2dec1], 5, 2, 2, False],
    "Binary to Decimal (hard)": [[bin2dec2], 10, 2, 4, False],
    "Binary to Hex (easy)": [[bin2hex], 5, 2, 0, False],
    "Hex to Binary (easy)": [[hex2bin], 5, 2, 0, False],
    "Hex to Decimal (easier)": [[hex2dec1], 5, 3, 2, False],
    "Hex to Decimal (hard)": [[hex2dec2], 5, 3, 4, False],
    "Random Conversions (easy)": [[dec2bin1, dec2hex1, bin2dec1, bin2hex, hex2bin, hex2dec1], 20, 5, 3, False],
    "Random Conversions (hard)": [[dec2bin2, dec2hex2, bin2dec2, bin2hex, hex2bin, hex2dec2], 20, 5, 5, False],
    "AND (&) Operations": [[and_operation], 5, 1, 0, False],
    "OR (|) Operations": [[or_operation], 5, 1, 0, False],
    "XOR (^) Operations": [[xor_operation], 5, 1, 0, False],
    "NOT and AND Operations": [[nand_operation], 10, 2, 2, False],
    "NOT and OR Operation": [[nor_operation], 10, 2, 2, False],
    "NOT and XOR Operation": [[nxor_operation], 10, 2, 2, False],
    "Random Logic": [[and_operation, or_operation, xor_operation, nand_operation, nor_operation, nxor_operation], 20, 5, 3, False],
}
completed_symbol = "√"
menu_items = list(menu_options.keys())


while True:
    print("\n--------Menu--------")
    for position, menu_opts in enumerate(menu_options.items()):
        each_item,opts = menu_opts
        print( f"{position: >2}) {each_item: <20} [white on green]{completed_symbol if opts[-1] else ''}[/] ")
    try:
        selection = input(f'\nSelect one of the items above to begin or Q to quit \n==> ')
    except EOFError:
        print("Bye")
        break
    if selection.lower() == "q":
        break
    try:
        if not selection.isnumeric() or int(selection) >= len(menu_items):
            print("Invalid Menu Option. Enter Q to quit.")
            continue
        options = menu_options.get(menu_items[int(selection)], "NOT FOUND")
        if options == "NOT FOUND":
            raise ValueError
    except:
        print("Invalid Menu Option. Enter Q to quit.")

    result = func_choice(*options)
    if result == True and result != "EXIT":
        menu_options[menu_items[int(selection)]][-1] = True
