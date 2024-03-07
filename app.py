# Coffee calculator.
# golden ratio = 1:15 (1 gram of coffee per 15 grams of water); try different ratios as needed
# TODO: flask app

def calculate_coffee_from_water(water_ounces, ratio):
    """Calculates coffee from water."""
    water_grams = water_ounces / 0.035274  # Convert ounces to grams
    coffee_grams = water_grams / ratio
    return coffee_grams

def calculate_water_from_coffee(coffee_grams, ratio):
    """Calculates water from coffee."""
    water_grams = coffee_grams * ratio
    water_ounces = water_grams * 0.035274  # Convert grams to ounces
    return water_ounces

def get_positive_float(prompt):
    """Gets a positive float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive number.")

def main():
    """Main script functionality."""
    print("\n") # double-line break
    print("Welcome to Blake's Coffee Calculator!")
    print("This calculator can help you determine either the amount of water you need for your coffee, or the amount of coffee you need for a given amount of water.")

    while True:
        choice = input("\nDo you know the amount of coffee or water? (Enter 'coffee', 'water', or 'exit'): ").lower()

        if choice == 'coffee':
            gram = get_positive_float("Enter the amount of coffee in grams, then hit enter: ")
            ratio = get_positive_float("Enter your preferred coffee ratio (e.g., '15' for '1:15'), then hit enter: ")
            water_ounces = calculate_water_from_coffee(gram, ratio)
            print(f"\nYou should pour {water_ounces:.2f} ounces of water.")
        elif choice == 'water':
            water_ounces = get_positive_float("Enter the amount of water in ounces, then hit enter: ")
            ratio = get_positive_float("Enter your preferred coffee ratio (e.g., '15' for '1:15'), then hit enter: ")
            coffee_grams = calculate_coffee_from_water(water_ounces, ratio)
            print(f"\nYou will need {coffee_grams:.2f} grams of coffee.")
        elif choice == 'exit':
            print("\nThank you for using Blake's Coffee Calculator. Go in peace!")
            break
        else:
            print("\nInvalid input. Please enter 'coffee', 'water', or 'exit'.")

# Run app
if __name__ == "__main__":
    main()

