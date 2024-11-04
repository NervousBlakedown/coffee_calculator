# Coffee calculator.
# Golden ratio = 1:15 to 1:18 (1 gram of coffee per 15–18 grams of water)
OZ_TO_GRAMS = 0.035274  # Conversion factor from ounces to grams

def calculate_coffee_from_water(water_ounces, ratio):
    """Calculates the amount of coffee needed for a given amount of water."""
    water_grams = water_ounces / OZ_TO_GRAMS
    coffee_grams = water_grams / ratio
    return coffee_grams

def calculate_water_from_coffee(coffee_grams, ratio):
    """Calculates the amount of water needed for a given amount of coffee."""
    water_grams = coffee_grams * ratio
    water_ounces = water_grams * OZ_TO_GRAMS
    return water_ounces

def get_positive_float(prompt):
    """Prompts the user for a positive float input."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print()
    print("\nWelcome to Blake's Coffee Calculator!")
    print("Determine the amount of coffee or water you need based on the coffee-to-water ratio.\n")

    while True:
        choice = input("Do you know the amount of coffee or water? (Enter 'coffee', 'water', or 'exit'): ").strip().lower()

        if choice == 'coffee':
            coffee_grams = get_positive_float("Enter the amount of coffee in grams: ")
            ratio = get_positive_float("Enter your preferred coffee ratio (15 to 18): ")
            if not 15 <= ratio <= 18:
                print("Please note that the recommended ratio is between 15 and 18.")
            water_ounces = calculate_water_from_coffee(coffee_grams, ratio)
            print(f"\nYou should use {water_ounces:.2f} ounces of water.")

        elif choice == 'water':
            water_ounces = get_positive_float("Enter the amount of water in ounces: ")
            ratio = get_positive_float("Enter your preferred coffee ratio (15 to 18): ")
            if not 15 <= ratio <= 18:
                print("Please note that the recommended ratio is between 15 and 18.")
            coffee_grams = calculate_coffee_from_water(water_ounces, ratio)
            print(f"\nYou will need {coffee_grams:.2f} grams of coffee.")

        elif choice == 'exit':
            print("\nThank you for using Blake's Coffee Calculator. Enjoy your coffee!")
            break

        else:
            print("Invalid input. Please enter 'coffee', 'water', or 'exit'.")

if __name__ == "__main__":
    main()
