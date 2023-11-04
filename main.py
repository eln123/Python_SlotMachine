

# 1) we need to get the user's deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        # check if amount is a number before you get out of while loop
        if amount.isdigit():
            # is digit is a string function to check if you can convert to int
            amount = int(amount)
            # now we have to check if amount > 0
            if amount > 0:
                # if amount is number and > 0, we break
                break
            else:
                print("Amount must be greater than 0.")
            
        else:
            print("Please enter a number")

    return amount

# 2) we need to get number of lines they are betting on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

# 3)
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
# 3) we need to get bet per line
def get_bet():
    while True:
        amount = input("What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount

# 4)
import random



#4)
ROWS = 3
COLS = 3

#4)
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#4)
def get_slot_machine_spin(rows, cols, symbols):
    # we need to pick 3 symbols to go in each column
    # so we will pick out of list of possible values, and remove them from the list each time we pick

    all_symbols = []
    # we are going to do a for loop that adds each symbol to the all_symbols list whatever the key is amount of times
    for symbol, symbol_count in symbols.items():
        print(symbol, symbol_count)
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    # columns is the slot machine
    # we are going to return 3 columns, with 3 symbols in each column
    columns = []
    # for each column we need to generate ROWS values
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        # : is the slice operator
        # if you don't put this, and you just do current_symbols = all_symbols, that is a "reference" not a "copy"
        # if you change a reference, it will then change current_symbols, and we don't want that
        # we do this for each for loop because we want to reset current_symbols for each column
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

# 5)when we print out each column, so the user can see what they spin,
# we are printing it out in this numerical order: 
# 1, 2, 3
# 4, 5, 6,
# 7, 8, 9
# to do this,we need to do "transposing"
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                # column == columns[i]
                print(columns[i][row], end=" | ")
            else: 
                # we are at the end, so don't print the pipe operator after
                print(columns[i][row], end="")
        print()
        # an empty print statement brings us down to the next line

# 6) Multipliers
symbol_count = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
# the multiplier applies to your bet if that letter is 3 times in a row

#6) now, we have to check if the slot machine spun 3 of the same letter in a row
# also, if the user bet on 1 line, or just 2 lines, that means they bet on the top and middle lines, they cannot choose which of the 3 they are betting on
# if they bet on all 3 lines, then all 3 lines are their bet
def check_winnings(columns, lines, bet, symbol_multipliers):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        # in this for loop, we have to check if every symbol in the row is the same
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_multipliers[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

#7)
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is ${balance}.")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${bet * lines}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_count)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")
main()