# Declaring the constants of the tax rate.
STATE_RATE = 0.05
COUNTY_RATE = 0.025
def main():
    # prompt the user to enter the amount of purchase.
    purchase_amount = float(input("Enter the amount of your purchase: $"))
    state_tax, county_tax, _ = calculate_taxes(purchase_amount)
    show_sale(purchase_amount, state_tax, county_tax)

def calculate_taxes(amount):
    state_tax = amount * STATE_RATE
    county_tax = amount * COUNTY_RATE
    total_tax = state_tax + county_tax
    return state_tax, county_tax, total_tax

def show_sale(amount, state_tax, county_tax):
    total_sale = amount + state_tax + county_tax
    print(f"Amount Purchased: ${amount:.2f}")
    print(f"State Tax (@{STATE_RATE:.2%}): ${state_tax:.2f}")
    print(f"County Tax (@{COUNTY_RATE:.2%}): ${county_tax:.2f}")
    print(f"Total Tax: ${state_tax + county_tax:.2f}")  # total tax = state tax + county tax
    print(f"Total Sale: ${total_sale:.2f}")


# invoking the main function.
main()
