import csv
#opens the first comma seperated value file
f = open('spread.csv', 'r')
#reads in the csv file
name = f.read()
#prints it out, 'cause testing
print name
#replace space with comma
numlist = (name.replace(' ',',')) #replace space with commas
#more verification
print numlist
#opens the file that the edited version of the first file is written to
newfile = open('FinalSpreadsheet.csv' , 'w+')
#writes to the new file
newfile.write(numlist)
#close the file
newfile.close()


