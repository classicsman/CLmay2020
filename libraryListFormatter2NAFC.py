# Python Project CL 2020
# Ricky J. Gleitz - July 2020

import re

import pyperclip

pyperclip.copy("") # clears the clipboard for the else statement in case there are no items to copy

# Hardcoded headers: (add after text manipulation later)
headers = "\n\n\nNew Albany Floyd County Public Library\n\
Title                         Due Back             Renewals Info\n"

# Input copied rawText:
input("Copy the NAFC data from the library's site or rawNAFCfile.txt (and press 'enter'): ")

textNAFC = pyperclip.paste()

numOfItemsNAFC = len(re.findall(r'Due \d\d', textNAFC))
itemsOut = str(numOfItemsNAFC)

# Conditional statement to manipulate text, or if no items out, output a notation
if textNAFC:
    
    makeOneLinedString = textNAFC.replace('\r\n', '')

    deleteToTitle = re.sub(r'(\w{5}\s\w*)?\w*\d\s\d\s\d\s\d\s\d', '\n', makeOneLinedString)

    deleteSubtitleAndDate = re.sub(r'(:.*)?\s\(\d\d\d\d\)', '', deleteToTitle)

    deleteAuthorEtc = re.sub(r'By.*\s\d\d\d\d\d\d\d\d\s\s', '', deleteSubtitleAndDate)

    deleteRenewLoan = re.sub(r'\w\w\w\w\w(\s\w\w\w\w)?$', '', deleteAuthorEtc)

    tabsToSpaces = deleteRenewLoan.replace(r'(.*?)\t', '\s')

    outputNAFC = headers +  tabsToSpaces + "\n\nNAFC items checked out: {}".format(itemsOut)

else:
    outputNAFC = "\n\n\nNew Albany Floyd County Public Library\nNo Items Checked Out"
