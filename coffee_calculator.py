# Coffee calculator.
# golden ratio = 1:15 (1 gram of coffee per 15 grams of water); try different ratios as needed

print("")
print("Thanks for using Blake's Coffee Calculator.")
gram = int(input("Enter number of coffee grams, then hit enter: "))
ratio = int(input("Enter preferred coffee ratio (i.e. '15' for '1:15', etc.), then hit enter: "))

water_gram = gram * ratio

water_ounces = water_gram * 0.035274

print()
print("You should pour " + str(water_ounces) + str(" ounces of water."))
