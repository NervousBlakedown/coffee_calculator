from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        option = request.form.get('option')
        ratio = float(request.form.get('ratio'))
        
        if option == 'coffee':
            coffee_grams = float(request.form.get('coffee_grams'))
            result = f"You should use {calculate_water_from_coffee(coffee_grams, ratio):.2f} ounces of water."
        
        elif option == 'water':
            water_ounces = float(request.form.get('water_ounces'))
            result = f"You will need {calculate_coffee_from_water(water_ounces, ratio):.2f} grams of coffee."

    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
