######################################################################################################################################
print("------------------------------------------------------------------------------------")
print("\t\t\t\tName Generator")
print("bored of your current name? Let us give you a new one!")

#input name and gender preference

name = input("\nWhat is your current name? ")
gender = input("And would you like a traditionally male (m) or female (f) name? ")
while gender.lower() != 'f' and gender.lower() != 'm':
    print("\nYou didn't enter 'm' or 'f'.")
    gender = input("And would you like a traditionally male (m) or female (f) name? ")
        
#######################################################################################################################################
#find new name

#delaying because reading things in takes ages
import time
time.sleep(1)
print("\nWe are proud to announce that your new name is...")

#reading in spreadsheet
import pandas as pd
letters = pd.read_excel('names.xlsx', sheet_name="letters", index_col=0)
names = pd.read_excel('names.xlsx', sheet_name="names", index_col=0)

#calculating total for letters in name
total = 0
for i in name.upper():
    if i in letters['letter']:
        total += letters.loc[str(i)]['number']

#finding new name according to chosen gender
if gender == 'm':
    newname = names.loc[total]['boy']

elif gender == 'f':
    newname = names.loc[total]['girl']

#printing new name

print(newname, "!")
time.sleep(0.5)
input("\nThanks for using this service, hope to see you again soon! Press the enter key to exit.")
