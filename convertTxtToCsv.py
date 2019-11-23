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
    stripped = (line.strip() for line in inFile)
    lines = (line.split(",") for line in stripped if line)
    with open('log.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('URL', 'TimeStamp'))
        writer.writerows(lines)
