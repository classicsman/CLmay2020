from datetime import datetime

# Bringing the library items together in one place
from libraryListFormatter2LFPL import outputLFPL, numOfItemsLFPL
from libraryListFormatter2NAFC import outputNAFC, numOfItemsNAFC
from libraryListFormatter2CCCO import outputCCCO, numOfItemsCCCO

# This serves a dual purpose - for the filename and the countdown
now = datetime.now()

# Date format for file name
formattedDate = now.strftime('%Y-%m-%d')

# Countdown til we get out of this awful year
newYear = datetime.strptime('Jan 1 2021  00:00', '%b %d %Y %H:%M')

countdown = int((newYear-now).total_seconds())

days = countdown // 86400
hours = (countdown - days * 86400) // 3600
minutes = (countdown - days * 86400 - hours * 3600) // 60
seconds = countdown - days * 86400 - hours * 3600 - minutes * 60
betterTimes = 'Only {} days, {} hours, {} minutes, and {} seconds left until we get a (HOPEFULLY) \
better year in 2021!\n\n'.format(days, hours, minutes, seconds)

# Totals all the items out
totalItems = numOfItemsLFPL + numOfItemsNAFC + numOfItemsCCCO

# Concatenates countdown and reformatted text files
outputFile = open(f'library_books_out_{formattedDate}.txt', "w")
outputFile.writelines(betterTimes + outputLFPL + outputNAFC + outputCCCO + \
                      str("\n\n\nTotal number of items checked out: {}".format(totalItems)))
outputFile.close()

