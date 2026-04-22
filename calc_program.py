# a simple calculator program - interactive user
# program will ask user for input and stores it in a variable called calc_data 
# program only checks for one operator 
# while the calc is true- keep running - in this case until user types 'quit'
while True:
    calc_data = input("Welcome, enter a calc with spaces (or type 'quit'): ")
    # requires spaces because split() will be used which seperates input based on spaces

    if calc_data == "quit":
        break # this will stop the loop

   # split input into list
   # split bascially breaks input using spaces
    items = calc_data.split()

    if "+" in items:
        operator = "+"
    elif "-" in items:
        operator = "-"
    elif "*" in items:
        operator = "*"
    elif "/" in items:
        operator = "/"
    elif "%" in items:
        operator = "%"
    else:
        print("invalid operation")
        continue

    result = float(items[0])

    # go through each item in list and look for operator
    # i is the position tracker
    i = 0
    # start at beginning of the list and goes through until the end
    # len means keep going until length of list is finished - returns how many items in the list
    while i < len(items):
        if items[i] == operator:
            number = float(items[i + 1])
        # if we find operator, take number after it and use it, now the math will be done
            if operator == "+":
               result = result + number
            elif operator == "-":
               result = result - number
            elif operator == "*":
               result = result * number
            elif operator == "/":
               result = result / number
            elif operator == "%":
               result = result % number

        i = i + 1 # move to next position in the list so lop continues if it wasnt here, the loop would stay in same place
         # print final result from calculations
         # result from the entire program - not indented 
    print("Result:", result)


