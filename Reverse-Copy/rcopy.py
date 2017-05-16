# Python 3.5.2 or 3.6.1 or later is required!
import sys

# Program Banner
print('Reverse Copy')
print('Forensics')

# File Name Input
print('Source File Name')
try:
    sourceFileName = sys.argv[1]
    print(sourceFileName)
except IndexError:
    sourceFileName = input()

print('Result File Name')
try:
    resultFileName = sys.argv[2]
    print(resultFileName)
except IndexError:
    resultFileName = input()

# Reading Source File
print('Read Source File...')
try:
    srcf = open(sourceFileName, 'rb')
    sfdata = srcf.read()
    srcf.close()
except FileNotFoundError as err:
    print('Failed!')
    print(err)
    exit()

# Reverse Data
print('Reverse File Data...')
rfdata = sfdata[::-1]

# Writing Result File
print('Write Result File...')
rstf = open(resultFileName, 'wb')
rstf.write(rfdata)
rstf.close()
print('Finished!')
exit()
