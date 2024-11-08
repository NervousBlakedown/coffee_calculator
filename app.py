# Coffee calculator.
# Golden ratio = 1:15 to 1:18 (1 gram of coffee per 15–18 grams of water)
import csv
import os

OZ_TO_GRAMS = 0.035274 

# Define the CSV file path
CSV_FILE_PATH = "C:\\Users\\blake\\Documents\\general_reference\\personal_stuff\\coffee_calculations.csv"

# Check if the CSV file exists and create it with headers if it doesn't
def initialize_csv():
    if not os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["water_oz", "coffee_g", "ratio"])

# Save unique results to the CSV file
def save_to_csv(water_ounces, coffee_grams, ratio):
    formatted_ratio = f"1:{int(ratio)}"
    coffee_grams = round(coffee_grams, 1)

    # Load existing data only once
    existing_data = set()
    if os.path.exists(CSV_FILE_PATH):
        with open(CSV_FILE_PATH, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                # Add each existing row as a tuple to the set
                existing_data.add((float(row[0]), float(row[1]), row[2]))

    # Only add new row if it’s not a duplicate
    new_entry = (water_ounces, coffee_grams, formatted_ratio)
    if new_entry not in existing_data:
        with open(CSV_FILE_PATH, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([water_ounces, coffee_grams, formatted_ratio])

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
    initialize_csv()
    print()
    print("Welcome to Blake's Coffee Calculator! Press CTRL + C anytime to quit.")

    while True:
        print()
        choice = input("Do you already know the 'coffee', 'water', or 'exit'? ").strip().lower()

        if choice == 'coffee':
            coffee_grams = get_positive_float("Enter the amount of coffee in grams: ")
            ratio = get_positive_float("Enter preferred coffee ratio ('15' for 1:15, etc.): ")
            if not 15 <= ratio <= 18:
                print("Please note that the recommended ratio is 1:15 to 1:18.")
            water_ounces = calculate_water_from_coffee(coffee_grams, ratio)
            print(f"Use {water_ounces:.1f} ounces of water.")
            save_to_csv(water_ounces, coffee_grams, ratio)


        elif choice == 'water':
            water_ounces = get_positive_float("Enter the amount of water in ounces: ")
            ratio = get_positive_float("Enter your preferred coffee ratio ('15' for 1:15, etc.): ")
            if not 15 <= ratio <= 18:
                print("Please note that the recommended ratio is between 15 and 18.")
            coffee_grams = calculate_coffee_from_water(water_ounces, ratio)
            print(f"Use {coffee_grams:.1f} grams of coffee.")
            save_to_csv(water_ounces, coffee_grams, ratio)
            

        elif choice == 'exit':
            print()
            print(f"Results saved to {CSV_FILE_PATH}.")
            print()
            open_csv = input("Would you like to open the CSV file? (yes/no): ").strip().lower()
            if open_csv == 'yes':
                print()
                print(f"Now opening {CSV_FILE_PATH}...")
                os.startfile(CSV_FILE_PATH)
            else:   
                print("\nThank you for using Blake's Coffee Calculator. Enjoy your coffee!")
            break

        else:
            print("Invalid input. Please enter 'coffee', 'water', or 'exit'.")

if __name__ == "__main__":
    main()
