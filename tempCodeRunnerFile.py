total = 0
inputs = [] 

while True: # loop condition while = True
    user_input = input("Enter a number (or type 'stop' to end): ") # user enter a either number, 0 reset the total and stop to stop the program
    if user_input.lower() == "stop": # if user enter stop program will stop
        break

    try:
        number = int(user_input) # use in because its whole number
        if number == 0: # first if in try if number equal siya sa zero mag rereset siya in total is zero (0)
            total = 0
            inputs.append(number)
            print(f"{number} is ZERO → Total reset to 0. Running total: {total}") # mag aapend dito if zero nilagay na total is zero in total
        elif number % 2 == 0: # even if user type even numbers
            total += number
            inputs.append(number)
            print(f"{number} is EVEN → Added. Running total: {total}") # and then numbers that user entered will add in total of the numnbers
        else: # else if odd siya mag substract siya ng number sa total numbers bawas if odd numbers add numbers pa add naman and 0 pag ireset ang total
            total -= number
            inputs.append(number)
            print(f"{number} is ODD  → Subtracted. Running total: {total}")

    except ValueError:
        print("Invalid input. Please enter a number or 'stop'.") # invalid input if si user nag entered ng invalid na na type nya sa input will print invalid

print("The Program is ending!")  # program ending pag na type yung stop 
print("Summary of all numbers you entered") # pag na stop na program  will print the total numbers who entered the user

for input in inputs: # dito naman yung after nung program end 
    if input == 0: # i print dito if zero was total reset total
        print(f"{input} → Zero (total was reset)")
    elif input % 2 == 0: # even naman pag even was added  sa total
        print(f"{input} → Even (was added)")
    else: # odd naman pag na print is odd was substract 
        print(f"{input} → Odd (was subtracted)")

print(f"Final Total: {total}") # and finally yung total ng lahat ng na enter ni user  