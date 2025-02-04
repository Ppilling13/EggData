from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Huw6etnxl238",
    database="egg_data_db"
)

cursor = db.cursor()

@app.route('/')
def home():
    # Fetch data from MySQL
    cursor.execute("SELECT * FROM egg_data ORDER BY date_collected DESC")
    egg_data = cursor.fetchall()  # Retrieve all rows

    # Explicitly convert data to a list of dictionaries
    formatted_data = [
        {"ID": row[0], "Eggs": row[1], "Deaths": row[2], "date_collected": row[3]}
        for row in egg_data
    ]

    # print("Formatted Data:", formatted_data)  # Debugging step

    return render_template('index.html', egg_data=formatted_data)

@app.route('/submit', methods=['POST'])
def submit_data():
    Eggs = request.form['Eggs']
    Deaths = request.form['Deaths']
    date_collected = request.form['date_collected']

    # Insert the data into the MySQL database
    query = "INSERT INTO Egg_data (Eggs, Deaths, date_collected) VALUES (%s, %s, %s)"
    cursor.execute(query, (Eggs, Deaths, date_collected))
    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
