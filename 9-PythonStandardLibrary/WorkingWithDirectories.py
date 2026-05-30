from pathlib import Path

path = Path("ecommerce")
print(path)
# path.exists()
# path.mkdir() 
# path.rmdir()
# path.rename("ecommerce2")

# paths = [p for p in path.iterdir() if p.is_dir()]
# print(paths) #[WindowsPath('ecommerce/__init__.py')]
py_files = [p for p in path.rglob("*.py")]
print(py_files) 