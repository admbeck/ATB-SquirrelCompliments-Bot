#!/usr/bin/env python3
import sqlite3
import csv

database = sqlite3.connect('compliments.db')
cursor = database.cursor()

with open('compliments.csv') as file:
    dr = csv.DictReader(file)
    to_db = [(i['compliment'], i['lang'], i['category']) for i in dr]

cursor.executemany('INSERT INTO compliments (comp_text, lang, category) VALUES (?, ?, ?);', to_db)
database.commit()
database.close()
