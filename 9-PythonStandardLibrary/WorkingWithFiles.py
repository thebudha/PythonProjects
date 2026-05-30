from pathlib import Path
from time import ctime
import shutil

path = Path("completePythonMastery/.vscode/ecommerce/__init__.py")
# path.exists() #True
# path.rename("init.txt")
# path.unlink() #Deletes the file
# print(path.stat()) #os.stat_result(st_mode=33206, st_ino=0, st_dev=0, st_nlink=1, st_uid=0, st_gid=0, st_size=0, st_atime=1700000000, st_mtime=1700000000, st_ctime=1700000000)
print(ctime(path.stat().st_birthtime)) #2024-06-14 12:00:00

# print(path.read_text()) #Reads the content of the file as a string
# path.write_text("print('Hello World')") #Writes the string to the file, overwriting existing content
# path.write_bytes(b"Hello World") #Writes bytes to the file, overwriting existing content

source = Path("completePythonMastery/.vscode/ecommerce/__init__.py")
target = Path() / "__init__.py"

shutil.copy(source, target) #Copies the file to the target location
shutil.move(source, target) #Moves the file to the target location
