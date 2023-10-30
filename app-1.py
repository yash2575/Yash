from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create an SQLite database
conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question1 TEXT NOT NULL,
        question2 TEXT NOT NULL,
        question3 TEXT NOT NULL,
        question4 TEXT NOT NULL,
        question5 TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

@app.route('/')
def feedback_form():
    return render_template('feedback_form.html')

if __name__ == '__main__':
    app.run(debug=True)