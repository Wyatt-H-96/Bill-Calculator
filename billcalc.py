# Calculator to calculate bill total, amount of people splitting bill and the tip based off percentage

while True:
    bill = input('What is the price of your bill? ')
    try:
        bill_float = float(bill)
        print(bill_float)
        break  # Break out of the loop if the input is valid
    except ValueError:
        print('Make sure you use a decimal and all numbers. Try again!\n')

while True:
    split = input('How many people are splitting the bill? ')
    try:
        split_int = int(split)
        print(split_int)
        break
    except ValueError:
        print('Please enter only numbers and no decimals. Try again!\n')
# Fix below section to input a percent only
while True:
    tip = input('What tip would you like to leave? (0.10, 0.15, 0.20, 0.25 etc..) ')
    try:
        tip_float = float(tip)
        print(tip_float)
        break
    except ValueError:
        print('Please enter a valid number with decimals. Try again!\n')



# Setup calculation below

bill_tip = float(bill) * float(tip) / 100
bill_total = float(bill) + float(bill_tip)
bill_per_person = float(bill_total) / float(split) 

print(f'Your total bill per person is ${bill_per_person:.2f}')

