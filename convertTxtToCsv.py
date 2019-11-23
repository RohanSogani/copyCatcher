import csv
import sys

if(len(sys.argv) != 2):
    print("Please enter a txt file to convert")
    sys.exit()
if(sys.argv[1].endswith('.txt') == False):
    print("Text files only")
    sys.exit()
print("Processing")
with open('catcher.txt', 'r') as inFile:
    #Remove leading and trailing whitespaces
    stripped = (line.strip() for line in inFile)
    lines = (line.split("\t") for line in stripped if line)
    with open('log.csv', 'w') as outFile:
        writer = csv.writer(outFile)
        writer.writerow(('URL', 'TimeStamp'))
        writer.writerows(lines)
