from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from forms import CafeForm
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    # Form write a new row into csv file when form is submitted
    if form.validate_on_submit():
        # Open the CSV file in append mode with newline=''
        with open('cafe-data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            # Ensures a new row is started
            writer.writerow([])

            new_row = []
            # Retrieving values from form
            for field_name, value in form.data.items():
                new_row.append(value)
            added_new_row = new_row[:-2]

            # Write the new row to the CSV file
            writer.writerow(added_new_row)
        cafes()
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True, port=5004)
