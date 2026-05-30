# JSON stands for JavaScript Object Notation. 
# It is a lightweight data-interchange format that is easy for humans to read and write, 
# and easy for machines to parse and generate. 
# In Python, we can work with JSON data using the built-in `json` module.
import json
from pathlib import Path

# #Creates a json file
# movies = [
#     { "id": 1, "title": "Terminator", "year": 1989 },
#     { "id": 2, "title": "Kindergarten Cop", "year": 1993 },
# ]

# data = json.dumps(movies) #Converts the Python object to a JSON string
# Path("movies.json").write_text(data) #Writes the JSON string to a file

#Reads the json file
data = Path("movies.json").read_text() #Reads the content of the file as a string
movies = json.loads(data) #Converts the JSON string to a Python object
print(movies[0]["title"])