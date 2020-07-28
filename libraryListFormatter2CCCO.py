# Python Project CL 2020
# Ricky J. Gleitz - July 2020

import re

import pyperclip

pyperclip.copy("") # clears the clipboard for the else statement in case there are no items to copy

# Hardcoded headers: (add after text manipulation later)
headers = "\n\n\nCharlestown Clark County Library\n\
Title                         Due Back             Renewals Info\n"

# Input copied rawText:
input("Copy the CCCO data from the library's site or rawCCCOfile.txt (and press 'enter'): ")

textCCCO = pyperclip.paste()

numOfItemsCCCO = len(re.findall(r'Due \d\d', textCCCO))
itemsOut = str(numOfItemsCCCO)

# conditional statement to manipulate text, or if no items out, return a statement
if textCCCO:
    
    makeOneLinedString = textCCCO.replace('\r\n', '')

    deleteToTitle = re.sub(r'(\w{5}\s\w*)?\w*\d\s\d\s\d\s\d\s\d', '\n', makeOneLinedString)

    deleteSubtitleAndDate = re.sub(r'(:.*)?\s\(\d\d\d\d\)', '', deleteToTitle)

    # ____________

    # deleteAuthorEtc = re.sub(r'By.*\s\d\d\d\d\d\d\d\d\s\s', '', deleteSubtitleAndDate)

    deleteAuthorEtc = re.sub(r'(By\,\.\(\).*)?\d\d\d\d\d\d\d\d\d\d\s\s', '', deleteSubtitleAndDate)

    # >>>>>>  /\  Trying to get author/DLC # out

    # ____________

    deleteRenewLoan = re.sub(r'\w\w\w\w\w(\s\w\w\w\w)?$', '', deleteAuthorEtc)

    tabsToSpaces = deleteRenewLoan.replace(r'(.*?)\t', '\s')

    outputCCCO = headers +  tabsToSpaces + "\n\nCCCO items checked out: {}".format(itemsOut)

else:
    outputCCCO = "\n\n\nCharlestown Clark County Library\nNo Items Checked Out"
