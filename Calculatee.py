print('Welcome to the bill calculator')
ask_bill = float(input('How much was the bill? $'))
ask_tip = int(input('How much tip percentage would u like to pay? '))
ask_people = int(input('How many people to split the bill? '))
tip_percentage = ask_tip / 100 
bill = ask_bill / 5
tip = tip_percentage * ask_bill / 5
total_bill = tip + bill
total_bill_round = '{:.2f}'.format(total_bill)
print(f'Each person should pay: ${total_bill_round}')
