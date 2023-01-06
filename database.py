#!/usr/bin/env python3
import sqlite3

def create_compliments_table():
    """Creates a table for compliments"""
    database = sqlite3.connect('compliments.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS compliments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comp_text TEXT,
        lang TEXT,
        category TEXT
        );
    ''')
    database.commit()
    database.close()

def select_compliment():
    """Selects random compliment from db"""
    database = sqlite3.connect('compliments.db')
    cursor = database.cursor()
    cursor.execute('''
        SELECT comp_text
          FROM compliments
         ORDER BY RANDOM()
         LIMIT 1;
    ''')
    compliment = cursor.fetchone()
    database.close()
    return compliment[0]

create_compliments_table()
