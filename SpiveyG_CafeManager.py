
cafe_name = "Lukes Diner"
tax_rate = 0.095  

print(f"Welcome to {cafe_name}!")
print(f"Today's tax rate: {tax_rate * 100:.0f}%")
print("-" * 40)


item_names = []
item_prices = []
item_quantities = []


def view_cart():
    if not item_names:
        print("Your cart is empty.")
    else:
        print("\n--- Your Cart ---")
        for i in range(len(item_names)):
            print(f"{i+1}. {item_names[i]} - ${item_prices[i]:.2f} x {item_quantities[i]}")
        print("-----------------\n")

def checkout():
    if not item_names:
        print("Your cart is empty. Nothing to checkout.")
        return

    subtotal = sum(item_prices[i] * item_quantities[i] for i in range(len(item_names)))
    discount = 0.0

   
    code = input("Enter discount code (or press Enter to skip): ").strip()
    if code.upper() == "STUDENT10":
        discount = subtotal * 0.10
        print("Discount code applied: 10% off!")

    subtotal_after_discount = subtotal - discount
    tax_amount = subtotal_after_discount * tax_rate
    total = subtotal_after_discount + tax_amount

    print("\n--- Checkout Summary ---")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: -${discount:.2f}")
    print(f"Tax: +${tax_amount:.2f}")
    print(f"Final Total: ${total:.2f}")
    print("-------------------------\n")




while True:
    print("Menu Options:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Checkout")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        name = input("Enter item name: ").strip()
        price = float(input("Enter item price: $"))
        quantity = int(input("Enter quantity: "))

        if price > 0 and quantity > 0:  
            item_names.append(name)
            item_prices.append(price)
            item_quantities.append(quantity)
            print(f"Added {quantity} x {name} at ${price:.2f} each.")
        else:
            print("Price and quantity must be positive numbers!")

    elif choice == "2":
        view_cart()

    elif choice == "3":
        view_cart()
        if item_names:
            try:
                remove_index = int(input("Enter the number of the item to remove: ")) - 1
                if 0 <= remove_index < len(item_names):
                    removed = item_names.pop(remove_index)
                    item_prices.pop(remove_index)
                    item_quantities.pop(remove_index)
                    print(f"Removed {removed} from your cart.")
                else:
                    print("Invalid item number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        checkout()

    elif choice == "5":
        print("Thank you for visiting lukes! Goodbye!")
        break

    else:
        print("Invalid option. Please choose 1-5.")
