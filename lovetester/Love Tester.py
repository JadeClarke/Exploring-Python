######################################################################################################################################
print("---------------------------------------------------------------")
print("\t\tThe Wonderful Panto Love Tester")
print("\n")

#setting up names

#input two names
name1 = input("First name: ").lower()
name2 = input("Second name: ").lower()

#makes both names 6 characters long
if len(name1)>6:
    name1 = name1[:6]
else:
    while len(name1)<6:
        for i in name1:
            if len(name1)<6:
                name1 = name1 + i
        if len(name1)==6:
            break

if len(name2)>6:
    name2 = name2[:6]
else:
    while len(name2)<6:
        for i in name2:
            if len(name2)<6:
                name2 = name2 + i
        if len(name2)==6:
            break
        
#######################################################################################################################################

#setting up scores
        
scores = {}

#imports scores data
import csv
with open('scores.csv', 'r') as scoresFile:
    
    #removes BOM characters and adds each entry to scores dictionary
    def remove_bom(line):
        return line[3:] if line.startswith("ï»¿") else line

    reader = csv.reader(remove_bom(line) for line in scoresFile)
    for row in reader:
        scores.update({row[0]:row[1]})
scoresFile.close()

#######################################################################################################################################

#calculate result

total = 0

#adding letter values in both names
for i in name1:
    total += int(scores[str(i)])
for i in name2:
    total += int(scores[str(i)])

#define and add bonus letters
bonus_value = 20
bonus_letters = ["p","a","n","t","o"]

for i in name1:
    if i in bonus_letters:
        total += bonus_value

for i in name2:
    if i in bonus_letters:
        total += bonus_value

#normalise
total = total/2.9

#######################################################################################################################################

#printing results (anything over 100 becomes 100)

#delays printing for dramatic effect
import time

time.sleep(1)
print("\ncalculating...")
t = 0
while t < 2:
    time.sleep(1)
    print("calculating...")
    t += 1

#prints result
time.sleep(1)
if total>100:
    print("\nLove percentage: ",100,"%")
else:
    print("\nLove percentage: ",int(total),"%")

input("\nPress the enter key to exit")
