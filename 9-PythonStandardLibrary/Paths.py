from pathlib import Path

# # Use "r" to create a raw string that ignores escape characters in Windows paths
# Path(r"C:/Program Files/Microsoft")
# #Path object that represents the home directory of the current user in linux
# Path("/usr/local/bin")
# #Path object that represents the current folder
# Path()
# #Combining paths using the "/" operator
# Path() / "ecommerce" / "__init__.py"
# #Returns home directory of the current user
# Path.home()

#Related path to a file in the current folder
path = Path("ecommerce/__init__.py")
path.exists() #True
path.is_file() #True    
path.is_dir() #False
print(path.name) #__init__.py
print(path.stem) #__init__
print(path.suffix) #.py
print(path.parent) #ecommerce
path = path.with_name("file.txt")
print(path) #ecommerce/file.txt
print(path.absolute()) #C:\Repos\PythonProjects\completePythonMastery\ecommerce\file.txt