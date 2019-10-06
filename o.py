import os
print(os.getcwd())
os.chdir('./')
print(os.getcwd())
print(os.listdir())
print(type(os.walk('./')))
print(os.environ['home'])