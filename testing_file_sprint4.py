"""A program to manage customers' pizza orders."""

from validations import get_validated_integer, \
    get_validated_integer_pizzalimits, get_validated_string
import math


def stars():
    """Print a line of * to separate information and make
    the output easy to understand."""
    print("*" * 60)


def dotted():
    """Print a line of . to separate information and make the
    output easy to understand."""
    print("." * 60)


def single_loop_print(p):
    """Print the list.
        :param L: list
        :return: None
    Print the list in a nice format and only once.
    """
    output = "{: ^10} {:^15} {:^15} {:^15}".format("INDEX", "PRICE", "PIZZAS", "DESCRIPTION")
    print(output)
    stars()
    for i in range(0, len(p)):
        output = "{}:  {: ^25} --- {:<10} --- {:<10}".format(i, p[i][0], p[i][1], p[i][2])
        print(output)


def add_to_order(mo,p):
    """Add pizza to order.

        :param L: list
        :return: None

        The required list must be two-dimensional,
        and the sub list must be of the form [str, int],
        requests user input for index and quantity,
        adds new pizza and quantity to the list,
        prints confirmation.
        """
    dotted()
    pizza_choice_index = get_validated_integer("Enter pizza index number:", 0, len(p)-1)
    chosen_pizza = p[pizza_choice_index][1]
    ## get the total number of pizzas
    total = total_pizzas_ordered(mo)
    print("You currently have {} pizzas in your order.".format(total))
    quantity = get_validated_integer_pizzalimits("How many {} pizzas would you like?".format(chosen_pizza), 1, 5)
    if total + quantity > 50:
        print("You can only order 50 pizzas in total. You can only order {} more pizzas.".format(50-total))
        return None
    dotted()
    temp_list = [chosen_pizza, quantity, p[pizza_choice_index][0]]
    mo.append(temp_list)


def review_order(mo):
    print("Here is your order so far:")
    dotted()


def total_pizzas_ordered(mo):
    total_sum = 0
    for i in range(0, len(mo)):
        total_sum += mo[i][1]
    return total_sum


def price_of_order(mo):
    total_price = 0
    for i in range(0, len(mo)):
        order = "{: ^15} x {:<10} @ {: ^5} ech ".format(mo[i][0], mo[i][1], mo[i][2])
        print(order)
        sub_total= mo[i][1] * mo[i][2]
        print("= {: ^10}".format(sub_total))
        total_price = total_price + sub_total
    dotted()
    print("Your order is ${} in total".format(total_price))
    dotted()
    return None


def quit_or_menu():
    """Choose to either quit or view menu.
        :param: None
        :return: None
        """
    # this list is a list of the customer's ordered pizzas
    my_order = []
    my_order_temp = [
        ["Russia", 5, 25.5],
        ["Botswana", 3, 18.5],
        ["Afghanistan", 2, 25.5],
    ]

    price_of_regular = 18.5
    price_of_gourmet = price_of_regular + 7

    pizzas = [
        (price_of_regular, "USA", "A tasty meat lovers pizza"),
        (price_of_regular, "Australia", "Pineapple, shrimp and BBQ sauce"),
        (price_of_gourmet, "Russia", "Mockba four fish pizza with sardines, tuna, mackerel and salmon"),
        (price_of_gourmet, "India", "Pickled ginger and paneer")
    ]

    option_menu = [
        ("V", "View pizza menu"),
        ("A", "Add pizza to your order"),
        ("R", "Review order so far"),
        ("Q", "Quit"),
        ("T", "This is a test")
    ]

    confirm_quit = [
        ("Y", "Continue quit"),
        ("N", "Go back to menu page")
    ]

    start = True
    run = True
    while run == True:
        for i in range(0, len(option_menu)):
            print("{:3} : {}".format(option_menu[i][0], option_menu[i][1]))
        option_choice = get_validated_string("What would you like to do? -> ", 0, 1).upper()
        dotted()
        if option_choice == "V":
            single_loop_print(pizzas)
            dotted()
        elif option_choice == "A":
            single_loop_print(pizzas)
            if start == True:
                dotted()
                print("Start to fill out order")
                start = False
            add_to_order(my_order, pizzas)
        elif option_choice == "R":
            review_order(my_order)
            total_pizzas_ordered(my_order)
            price_of_order(my_order)
        elif option_choice == "Q":
            for i in range(0, len(confirm_quit)):
                print("{:3} : {}".format(confirm_quit[i][0], confirm_quit[i][1]))
            ask_quit_confirmation = get_validated_string("Are you sure you want to quit?", 0, 1).upper()
            dotted()
            if ask_quit_confirmation == "Y":
                print("Thank you for visiting Marsden Pizzas. Hope to see you again!")
                dotted()
                run = False
            elif ask_quit_confirmation == "N":
                run = True
            else:
                print("You have requested an invalid choice.")
                dotted()
        elif option_choice == "T":
            print("Hey")
        else:
            print("You have requested an invalid choice.")
            dotted()


quit_or_menu()