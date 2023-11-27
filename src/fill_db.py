import pandas as pd
import json
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

output_data = pd.read_csv('./output.csv')

conn = get_db_connection()
cur = conn.cursor()
cur.execute('CREATE TABLE results(result TEXT);')
conn.commit()
conn.close()

for index, row in output_data.iterrows():
    conn = get_db_connection()
    cur = conn.cursor()

    first_10 = json.loads(row['first10'])
    predicted_next_20 = json.loads(row['predicted_next_20'])
    real_next_20 = json.loads(row['real_next_20'])

    db_row = json.dumps({
        'idx': index,
        'first_10': first_10, 
        'predicted_next_20': predicted_next_20,
        'real_next_20': real_next_20,
    })

    cur.execute(f"INSERT INTO results VALUES ('{db_row}')");
    conn.commit();
    conn.close();