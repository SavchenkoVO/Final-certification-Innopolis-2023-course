import sqlite3, json
from flask import Flask, render_template

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def main_page():
    conn = get_db_connection()
    cur = conn.cursor()
    data = cur.execute('SELECT * FROM results').fetchall()
    conn.close()

    return render_template('main.html', predictions=[ json.loads(row['result']) for row in data])

if __name__ == '__main__':
	app.run(debug=True)