# This program calculates the total cost of items purchased based on quantity discounts.
# 29 May 2024
# CSC121 m1Lab1– Review
# Ruben Guillen


"""
Pseudocode:
1. Start
2. Define a function to calculate total cost based on the number of items:
    a. Prompt user to enter the number of items they want to purchase.
    b. Determine the cost per item based on the following quantity discounts:
        - If number of items is between 1 and 19, cost per item is $4.75
        - If number of items is between 20 and 49, cost per item is $4.50
        - If number of items is between 50 and 99, cost per item is $4.25
        - If number of items is 100 or more, cost per item is $4.00
    c. Calculate the total cost as number of items multiplied by cost per item.
    d. Return the number of items, cost per item, and total cost.
3. Define a main function to control the program flow:
    a. Enter a loop that does the following until the user decides to stop:
        i. Call the function to calculate total cost and display results.
        ii. Display the cost per item and the total cost.
        iii. Prompt the user to decide if they wish to run the program again.
        iv. If user inputs 'No', thank them and break the loop to end the program.
4. Check if the script is the main program and if so, call the main function to execute.
5. End
"""

def calculate_total_cost():
    # Prompt for the total items wanted to purchase
    n_of_items = int(input("Enter the number of items you want to purchase: "))

    # Determine the cost, depending on the quantity
    if 1 <= n_of_items <= 19:
        cost_per_item = 4.75
    elif 20 <= n_of_items <= 49:
        cost_per_item = 4.50
    elif 50 <= n_of_items <= 99:
        cost_per_item = 4.25
    else:
        cost_per_item = 4.00

    total_cost = cost_per_item * n_of_items
    return n_of_items, cost_per_item, total_cost

# Main function to control the program flow
def run_program():
    while True:
        n_of_items, cost_per_item, total_cost = calculate_total_cost()
        # Display Cost per item and total order cost
        print(f"Cost per item: ${cost_per_item:.2f}")
        print(f"Total cost for {n_of_items} items: ${total_cost:.2f}")
        
        # Ask user if they wish to run the program again, only exits on 'no'
        again = input("Do you wish to run the program again? (Yes/No): ")
        if again.lower() == 'no':
            print("Thank you for using the purchase. Goodbye!")  # A friendly goodbye message.
            break

# Ensures that run_program() is called only when this script is executed directly,
# not when imported as a module into another script.
if __name__ == '__main__':
    run_program()