# Program Banner
print('Reverse Copy')
print('Forensics')

# File Name Input
print('Source File Name')
srcFileName = input()
print('Result File Name')
rstFileName = input()

# Reading Source File
print('Read Source File...')
srcf = open(srcFileName, 'rb')
sfdata = srcf.read()
srcf.close()

# Reverse Data
print('Reverse File Data...')
rfdata = sfdata[::-1]

# Writing Result File
print('Write Result File...')
rstf = open(rstFileName, 'wb')
rstf.write(rfdata)
rstf.close()
print('Finished!')
