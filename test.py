from datetime import datetime, timedelta
import random
import sqlite3
DB_PATH = pantry.db
def insert_fake_ingredients(n=10):
    fake_ingredients = [
        "Onion", "Tomato", "Coriander", "Turmeric", "Chili Powder",
        "Salt", "Sugar", "Garlic", "Ginger", "Cumin Seeds",
        "Garam Masala", "Mustard Seeds", "Curry Leaves", "Green Chili", "Yogurt"
    ]
    units = ["g", "kg", "ml", "L", "pcs", "tbsp", "tsp"]

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    for _ in range(n):
        name = random.choice(fake_ingredients)
        quantity = round(random.uniform(0.5, 5.0), 2)
        unit = random.choice(units)
        expiry = (datetime.now() + timedelta(days=random.randint(5, 30))).strftime('%Y-%m-%d')

        c.execute("INSERT INTO pantry (name, quantity, unit, expiry) VALUES (?, ?, ?, ?)",
                  (name, quantity, unit, expiry))

    conn.commit()
    conn.close()
