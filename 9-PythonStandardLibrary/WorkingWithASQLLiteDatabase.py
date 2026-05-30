import sqlite3
import json
from pathlib import Path

# # Create a SQLite database and a table for movies
# movies = json.loads(Path("completePythonMastery/9-PythonStandardLibrary/movies.json").read_text())

# with sqlite3.connect("db.sqlite3") as conn:
#     command = "INSERT INTO Movies VALUES (?, ?, ?)"
#     for movie in movies:
#         conn.execute(command, tuple(movie.values()))
#     conn.commit()

with sqlite3.connect("db.sqlite3") as conn:
    command = "SELECT * FROM Movies"
    cursor = conn.execute(command)
    for row in cursor:
        print(row)
