# Python 3.5.2 or 3.6.1 or later is required!
import sys

# Program Banner
print('Reverse Copy')
print('Forensics')

# File Name Input
print('Source File Name')
try:
    srcFileName = sys.argv[1]
    print(srcFileName)
except IndexError:
    srcFileName = input()

print('Result File Name')
try:
    rstFileName = sys.argv[2]
    print(rstFileName)
except IndexError:
    rstFileName = input()

# Reading Source File
print('Read Source File...')
try:
    srcf = open(srcFileName, 'rb')
    sfdata = srcf.read()
    srcf.close()
except FileNotFoundError:
    print('Failed!')
    exit()

# Reverse Data
print('Reverse File Data...')
rfdata = sfdata[::-1]

# Writing Result File
print('Write Result File...')
rstf = open(rstFileName, 'wb')
rstf.write(rfdata)
rstf.close()
print('Finished!')
exit()
