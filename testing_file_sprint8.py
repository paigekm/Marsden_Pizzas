"""A program to manage customers' pizza orders."""

from validations import get_validated_integer, \
    get_validated_integer_pizzalimits, get_validated_string


def stars():
    """Print a line of * to separate information.

        :return: None

    This also makes the output easy to understand.
    """
    print("*" * 60)


def dotted():
    """Print a line of . to separate information.

        :return: None

    It also makes the output easy to understand.
    """
    print("." * 60)


def single_loop_print(p):
    """Print the list.

        :param p: list
        :return: None

    Print the list in a nice format and only once.
    """
    output = "{:^15} {:^15} {:^15}".\
        format("PRICE", "PIZZAS", "DESCRIPTION")
    print(output)
    stars()
    for i in range(0, len(p)):
        output = "{: ^15} --- {:<15} --- {:<15}".format(p[i][0],
                                                        p[i][1], p[i][2])
        print(output)


def single_loop_print_with_indexes(p):
    """Print the list.

        :param p: list
        :return: None

    Print the list in a nice format and only once.
    """
    output = "{: ^10} {:^15} {:^15} {:^15}".\
        format("INDEX", "PRICE", "PIZZAS", "DESCRIPTION")
    print(output)
    stars()
    for i in range(0, len(p)):
        output = "{}:  {: ^25} --- {:<10} --- {:<10}".format(i, p[i][0],
                                                             p[i][1], p[i][2])
        print(output)


def add_to_order(mo, p):
    """Add pizza to order.

    :param mo: list (customer order list)
    :param p: list (pizza menu list)
    :return: None

    The required list must be two-dimensional,
    and the sub list must be of the form [str, int],
    requests user input for index and quantity,
    adds new pizza and quantity to the list,
    prints confirmation.
    """
    dotted()
    # only allows the user to choose a pizza index number that is on the menu
    pizza_choice_index = get_validated_integer("Enter pizza "
                                               "index number:", 0, len(p)-1)
    chosen_pizza = p[pizza_choice_index][1]
    # get the total number of pizzas
    total = total_pizzas_ordered(mo)
    print("You currently have {} pizzas in your order.".format(total))
    # only allows the user to order up to 5 pizzas of one type
    quantity = get_validated_integer_pizzalimits("How many {} "
                                                 "pizzas would you like?".
                                                 format(chosen_pizza), 1, 5)
    if total + quantity > 50:
        print("You can only order 50 pizzas in total. "
              "You can only order {} more pizzas.".format(50-total))
        return None
    dotted()
    temp_list = [chosen_pizza, quantity, p[pizza_choice_index][0]]
    mo.append(temp_list)


def total_pizzas_ordered(mo):
    """Return the total number of pizzas the user has ordered.

    :param mo: None
    :return: integer
    """
    total_sum = 0
    for i in range(0, len(mo)):
        total_sum += mo[i][1]
    return total_sum


def price_of_order(mo, delivery_charge):
    """Return the total price and number of pizzas ordered in a receipt format.

    :param mo: None
    :return: None
    """
    print("Here is your order so far:")
    dotted()
    total_price = 0
    #
    for i in range(0, len(mo)):
        sub_total = mo[i][1] * mo[i][2]
        order = "{: ^15} x {:<10} @ {: ^5.2f}      ${:<15.2f}".format(mo[i][0],
                                                                      mo[i][1],
                                                                      mo[i][2],
                                                                      sub_total
                                                                      )
        print(order)
        total_price = total_price + sub_total + delivery_charge
    dotted()
    order = "{: ^15}   {:<10}   {: ^5}      ${:<15.2f}". \
        format("", "", "Total", total_price)
    order_gst = "{: ^15}   {:<10}   {: ^5}      ${:<15.2f}". \
        format("", "", "GST", total_price*(3/23))
    order_delivery = "{: ^15}   {:<10}   {: ^5}      ${:<15.2f}". \
        format("", "", "Extra", delivery_charge)
    print(order_delivery)
    dotted()
    print(order)
    print(order_gst)
    dotted()
    return None


def update(mo, delivery_charge):
    """Give the user the option to change their order.

    Delete a pizza or return to the main menu.

    :param mo: None
    :return: None
    """
    # print current order so far
    total_pizzas_ordered(mo)
    # prints total cost and GST
    price_of_order(mo, delivery_charge)
    # sub menu options
    change_options = [("C", "Change amount"), ("D", "Delete pizza from order"),
                      ("E", "Exit back to main menu")]

    # requests index number from the pizza order list
    message = "Please enter the index number (far left column) " \
              "of the pizza you would like to update:"
    indextochange_choice = get_validated_integer(message,
                                                 0, len(mo) - 1)

    print("The pizza you have chosen to change is {"
          "}".format(mo[indextochange_choice][0]))
    dotted()
    # print the sub menu
    for i in range(0, len(change_options)):
        print("{:3} : {}".format(change_options[i][0], change_options[i][1]))
    # request option letter
    change_choice = get_validated_string(""
                                         "What would you "
                                         "like to do?"
                                         "", 0, 1).upper()

    if change_choice == "C":
        # requests integer of new number of pizzas
        message = "Please enter the new amount of {} pizzas you would lik" \
                  "e:".format(mo[indextochange_choice][0])
        new_amount_pizzas = get_validated_integer_pizzalimits(message, 0, 5)
        # confirms the user wants to,
        # then appends the number of pizzas in the order or does not append it
        message = "Are you sure you want to change your order to have {} {} " \
                  "pizzas Please enter Y/N:" \
                  "".format(new_amount_pizzas, mo[indextochange_choice][0])
        yes_or_no_change = get_validated_string(message, 0, 1).upper()

        if yes_or_no_change == "Y":
            mo[indextochange_choice][1] = new_amount_pizzas
        elif yes_or_no_change == "N":
            print("Your order still has your original request for {} {} "
                  "pizzas"
                  "".format(mo[indextochange_choice][1],
                            mo[indextochange_choice][0]))
            dotted()
            return None
        else:
            print("Your entry was invalid.")
            dotted()
            return None

    elif change_choice == "D":
        # request confirmation of delete
        yes_or_no_delete = get_validated_string(("Are you sure you want "
                                                 "to delete all {} pizzas"
                                                 " from the order? "
                                                 "Please enter Y/N:"
                                                 "").format
                                                (mo[indextochange_choice][0]),
                                                0, 1).upper()
        if yes_or_no_delete == "Y":
            print("{} pizzas are being deleted..."
                  "".format(mo[indextochange_choice][0]))
            # remove row from the list
            mo.pop(indextochange_choice)
            dotted()
        elif yes_or_no_delete == "N":
            print("{} pizzas have NOT been deleted..."
                  "".format(mo[indextochange_choice][0]))
            dotted()
            return None
        else:
            print("Your entry was invalid.")
            dotted()
            return None

    elif change_choice == "E":
        print("Exiting...")
        dotted()
        return None

    else:
        return None


def customer_details():
    """Get customer details

    :param: None
    :return: None
    """
    # submenu asking for pizza pickup or delivery
    deliverypickup_options = [("P", "Pickup"), ("D", "Delivery")]
    message = "Please enter the customer name:"
    message_phone = "Please enter your phone number:"
    # asks for user to enter their name
    name = get_validated_string(message, 0, 15)
    phone = get_validated_string(message_phone, 0, 30)
    # prints their name and number
    dotted()
    print("Order name: {}".format(name))
    print("Number: {}".format(phone))
    dotted()
    for i in range(0, len(deliverypickup_options)):
        print("{:3} : {}".format(deliverypickup_options[i][0], deliverypickup_options[i][1]))
    # asks user to choose whether they would like to do pickup or delivery
    deliverypickup_choice = get_validated_string(""
                                         "What would you "
                                         "like to do?"
                                         "", 0, 1).upper()

    if deliverypickup_choice == "P":
        dotted()
        print("Pickup for {} at Karori Branch".format(name))
        dotted()
        # returns information about the pickup details
        return name, phone, deliverypickup_choice
    elif deliverypickup_choice == "D":
        message_address = "Please enter 1st address line:"
        message_suburb = "Please enter 2nd address line:"
        # asks for user to enter their address
        address = get_validated_string(message_address, 0, 50)
        suburb = get_validated_string(message_suburb, 0, 50)
        dotted()
        print("Delivery for {} to {}".format(name, address))
        dotted()
        dotted()
        # returns information about the pickup details
        return name, phone, deliverypickup_choice, address, suburb
    else:
        return None


def quit_or_menu():
    """Choose to either quit or view menu.

    :param: None
    :return: None
    """
    price_of_regular = 18.5
    price_of_gourmet = price_of_regular + 7

    # list of pizzas on the menu
    pizzas = [
        (price_of_regular, "USA", "A tasty meat lovers pizza"),
        (price_of_regular, "Australia", "Pineapple, shrimp and BBQ sauce"),
        (price_of_gourmet, "Russia",
         "Mockba four fish pizza with sardines, tuna, mackerel and salmon"),
        (price_of_gourmet, "India", "Pickled ginger and paneer")
    ]

    pizzas_full = [
        (price_of_regular, "USA", "A tasty meat lovers pizza"),
        (price_of_regular, "Australia", "Pineapple, shrimp and BBQ sauce"),
        (price_of_regular, "NZ", "Steak and Kumara"),
        (price_of_regular, "France", "Flambee - bacon, onion, cream"),
        (price_of_regular, "Italy", "Margharita"),
        (price_of_regular, "UK", "Pepperoni"),
        (price_of_regular, "Germany", "Flammkuchen - "
                                      "bacon and caramelized onions"),
        (price_of_gourmet, "Russia",
         "Mockba four fish pizza with sardines, tuna, mackerel and salmon"),
        (price_of_gourmet, "India", "Pickled ginger and paneer"),
        (price_of_gourmet, "Japan", "Eel, squid, mayojaga"),
        (price_of_gourmet, "Brazil", "Green peas"),
        (price_of_gourmet, "Pakistan", "Curry")
    ]

    option_menu = [
        ("V", "View pizza menu"),
        ("A", "Add pizza to your order"),
        ("U", "Update"),
        ("R", "Review order so far"),
        ("D", "Confirm customer Details"),
        ("F", "Finish order"),
        ("C", "Cancel order"),
        ("Q", "Quit")
    ]

    confirm_quit = [
        ("Y", "Continue quit"),
        ("N", "Go back to menu page")
    ]

    confirm_cancel = [
        ("Y", "Continue to cancel order"),
        ("N", "Go back to menu page")
    ]

    customerdetails_data = None
    delivery_charge = 0

    # starts the ordering process
    start_order = True
    # when the first pizza is ordered
    first_pizza_in_the_order = True
    run = True
    while run is True:
        # informs the user a completely new order is being made
        if start_order is True:
            dotted()
            print("A new order is starting now")
            dotted()
            # this list is a list of the customer's ordered pizzas
            # this list is empty when a new order is
            # started and is then appended
            my_order = []
            # once the order has been started,
            # it is not a completely new order anymore
            start_order = False
        # runs the main option menu
        for i in range(0, len(option_menu)):
            print("{:3} : {}".format(option_menu[i][0], option_menu[i][1]))
        option_choice = get_validated_string("What would you like "
                                             "to do? -> ", 0, 1).upper()
        dotted()
        if option_choice == "V":
            # prints the food menu
            single_loop_print(pizzas_full)
            dotted()
        elif option_choice == "A":
            # allows the user to add a pizza type to the order
            single_loop_print_with_indexes(pizzas_full)
            # this message only prints when the order is
            # initially empty and the first pizza is added
            # this is not printed every time
            # the user orders a different pizza type in their order
            if first_pizza_in_the_order is True:
                dotted()
                print("Start to fill out order")
                # this is false once the first pizza is ordered
                first_pizza_in_the_order = False
            add_to_order(my_order, pizzas_full)

        elif option_choice == "R":
            if len(my_order) == 0:
                print("You have no pizzas in your order yet!")
                dotted()
            # allows the user to review their order so far
            else:
                total_pizzas_ordered(my_order)
                price_of_order(my_order, delivery_charge)

        elif option_choice == "D":
            customerdetails_data = customer_details()
            if customerdetails_data[2] == "D":
                delivery_charge = 3
                dotted()

        elif option_choice == "F":
            if customerdetails_data:
                print(customerdetails_data[0])
                print(customerdetails_data[1])
                if customerdetails_data[2] == "D":
                    print(customerdetails_data[3])
                    dotted()
                price_of_order(my_order, delivery_charge)
                print("Thank you for coming to our pizza shop!")
                dotted()
                start_order = True
            else:
                print("Please enter your customer details first.")
                dotted()
                for i in range(0, len(option_menu)):
                    print("{:3} : {}".format(option_menu[i][0], option_menu[i][1]))
                option_choice = get_validated_string("What would you like "
                                                     "to do? -> ", 0, 1).upper()


        elif option_choice == "U":
            if len(my_order) == 0:
                print("You have no pizzas to update. "
                      "Please add pizzas to your order first.")
                dotted()
            else:
                # calls update function to either
                # change the number of pizzas or delete one
                update(my_order, delivery_charge)

        elif option_choice == "C":
            # ends the ordering process
            if start_order is False:
                # user can cancel their whole order
                # but is asked to confirm first
                for i in range(0, len(confirm_cancel)):
                    print("{:3} : {}".format(confirm_cancel[i][0],
                                             confirm_cancel[i][1]))
                ask_cancel_confirmation = get_validated_string("Are you sure "
                                                               "you "
                                                               "want to "
                                                               "cancel "
                                                               "your order?"
                                                               "", 0, 1
                                                               ).upper()
                dotted()
                if ask_cancel_confirmation == "Y":
                    start_order = True
                elif ask_cancel_confirmation == "N":
                    run = True
                else:
                    print("You have requested an invalid choice.")
                    dotted()

        elif option_choice == "Q":
            # user can quit the whole program but is asked to confirm first
            for i in range(0, len(confirm_quit)):
                print("{:3} : {}".format(confirm_quit[i][0],
                                         confirm_quit[i][1]))
            ask_quit_confirmation = get_validated_string(""
                                                         "Are you sure you "
                                                         "want to quit?"
                                                         "", 0, 1).upper()
            dotted()
            if ask_quit_confirmation == "Y":
                print("Thank you for visiting Marsden Pizzas. "
                      "Hope to see you again!")
                dotted()
                run = False
            elif ask_quit_confirmation == "N":
                run = True
            else:
                print("You have requested an invalid choice.")
                dotted()
        else:
            print("You have requested an invalid choice.")
            dotted()


quit_or_menu()
