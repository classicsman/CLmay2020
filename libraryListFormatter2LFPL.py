# Python Project CL 2020
# Ricky J. Gleitz - July 2020

import re

import pyperclip

pyperclip.copy("") # clears the clipboard for the else statement in case there are no items to copy

# Hardcoded headers: (add after text manipulation later)
headers = "\nLouisville Free Public Library\n\
Title                                     Due           Renewals Left\n\n"

# Input copied rawText:
input("Copy the LFPL data from the library's site or rawLFPLfile.txt (and press 'enter'): ")

textLFPL = pyperclip.paste()

numOfItemsLFPL = len(re.findall(r'Item details', textLFPL))
itemsOut = str(numOfItemsLFPL)

# Conditional statement to manipulate text, or if no items out, output a notation
if textLFPL:
    
    makeOneLinedString = textLFPL.replace('\r\n', ',')

    deleteToTitleFirstItem = re.sub(r'^.*?\s\d\d\d\d\t', '', makeOneLinedString)

    deleteToTitleRemainingItems = re.sub(r',(.*?)\s\d\d\d\d\t', '\n', deleteToTitleFirstItem)

    deleteSubtitleAndBranch = re.sub(r'(\s:.*)?\t\w*(\s\w*)?\t', '   ', deleteToTitleRemainingItems)

    tabsToSpaces = deleteSubtitleAndBranch.replace(r'(.*?)\t', '\s')

    outputLFPL = headers + tabsToSpaces + "\n\nLFPL items checked out: {}".format(itemsOut)

else:
    outputLFPL = "\n\n\nLouisville Free Public Library\nNo Items Checked Out"
