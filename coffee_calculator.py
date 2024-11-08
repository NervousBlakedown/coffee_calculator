from flask import Flask, render_template, request, session, send_file, redirect, url_for
import csv
from io import BytesIO, StringIO

app = Flask(__name__)
app.secret_key = 'coffee_secret_key'
OZ_TO_GRAMS = 0.035274 

def calculate_coffee_from_water(water_ounces, ratio):
    """Calculates amount of coffee needed for a given amount of water."""
    water_grams = water_ounces / OZ_TO_GRAMS
    coffee_grams = round(water_grams / ratio, 1)
    return coffee_grams

def calculate_water_from_coffee(coffee_grams, ratio):
    """Calculates amount of water needed for a given amount of coffee."""
    water_grams = coffee_grams * ratio
    water_ounces = round(water_grams * OZ_TO_GRAMS)
    return water_ounces

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if 'calculations' not in session:
        session['calculations'] = []

    if request.method == 'POST':
        option = request.form.get('option')
        ratio = int(float(request.form.get('ratio')))
        formatted_ratio = f"1:{ratio}"
        
        if option == 'coffee':
            coffee_grams = float(request.form.get('coffee_grams'))
            water_needed = calculate_water_from_coffee(coffee_grams, ratio)
            result = f"Pour {water_needed} ounces of water."
            calculation = {"water_oz": round(water_needed), "coffee_g": coffee_grams, "ratio": formatted_ratio}

        elif option == 'water':
            water_ounces = float(request.form.get('water_ounces'))
            coffee_needed = calculate_coffee_from_water(water_ounces, ratio)
            result = f"Grind {coffee_needed} grams of beans."
            calculation = {"water_oz": round(water_ounces), "coffee_g": coffee_needed, "ratio": formatted_ratio}

        # Only add calculation if not already in session
        if calculation not in session['calculations']:
            session['calculations'].append(calculation)
            session.modified = True # mark session as modified to save changes

    return render_template('index.html', result=result)

@app.route('/download_csv')
def download_csv():
    calculations = session.get('calculations', [])
    if not calculations:
        return redirect(url_for('index'))

    # Create CSV in memory with StringIO (text mode)
    csv_data = StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(["water_oz", "coffee_g", "ratio"])

    # Use a set to track unique entries to prevent duplicates
    unique_calculations = set()
    
    for calc in calculations:
        water_oz = round(calc.get("water_oz", 0))  
        coffee_g = round(calc.get("coffee_g", 0), 1) 
        ratio = calc.get("ratio", "")

        # only add row if unique and all fields are filled
        unique_key = (water_oz, coffee_g, ratio)
        if unique_key not in unique_calculations and water_oz and coffee_g and ratio:
            writer.writerow([water_oz, coffee_g, ratio])
            unique_calculations.add(unique_key)

    # Convert CSV text data into bytes
    csv_bytes = BytesIO(csv_data.getvalue().encode('utf-8'))
    csv_data.close()

    # Send CSV as attachment
    return send_file(
        csv_bytes,
        mimetype='text/csv',
        as_attachment=True,
        download_name="coffee_calcs.csv"
    )

if __name__ == "__main__":
    app.run(debug=True)
