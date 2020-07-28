**CODE LOUISVILLE PROJECT**

**PYTHON MAY 2020**

R. Gleitz

General information:

The Library List Formatter is designed to take text input that I copy from my library patron's account at each of the following libraries:

Louisville Free Public Library (LFPL)
New Albany Floyd County Public Library (NAFC)
Charlestown Clark County Public Library (CCCO)

then concatenates and formats that raw input into a text file that has taken out unwanted information and more neatly presents it versus what it would look like if I just simply pasted the raw information into a text file.

The desire to do this program comes from having made such text files by hand every few weeks from the raw information, which takes about a half hour or more. This program should only take about five minutes, most of which is accessing the accounts on the various libraries' websites. The data is my actual accountdata, taken on July 26, 2020.


**How to Run the Program:**

Python must be on your computer
Pyperclip needs to be installed:

**pip install pyperclip**

if you have trouble with installing pyperclip, see:
https://pypi.org/project/pyperclip/

**re** and **datetime** are also imported, but that shouldn't be problematic, as they are in the standard library.

For the purposes of demonstration the libraries' information is stored in the following text files:

rawLFPLfile.txt, rawNAFCfile.txt, rawCCCOfile.txt

**1)** After you have the repo on your machine, run the main program, fullLibraryListFormatter.py

**2)** When the first prompt "Copy the LFPL data from the library's site or rawLFPLfile.txt (and press 'enter'): " appears, open the rawLFPLfile.txt file and select everything in it, either by highlighting it, or by pressing "Select All" under the Edit tab in the menu. Then either right click and press Copy, or press Copy under the Edit tab. Then click back in the window with the prompt and simply press 'enter' to load the text. No pasting! If you do, you have to start over.
Then another prompt comes up for the NAFC info, so open the rawNAFCfile.txt file and do the same procedure; likewise for the CCCO library. The option to copy from the websites is not open to anyone but me (and anyone who makes a copy of the repo and has their own accounts).

**Note:** The idea behind pyperclip is that it will take in whatever you have copied in your clipboard. The clipboard gets cleared when the program runs, and after each entry. This helps ensure that the same data won't be submitted twice and be formatted by two different modules. It also allows you to press 'enter' without copying if there are no books checked out at the library prompted. The output for that library will be "No Items Checked Out" in the text.

**3)** Open the output file to see the result. It's in the same directory the program files are in. Its name structure is: LibraryItemsOut{current date}.txt where the {current date} in the file name will be the formatted date for the day you run the program.

If you run the program again on the same day, that file will be overwritten, if you run it again on another day, that day's date will be in the file name and it will be a new file, with the previous one remaining.

**Note:** In real use, I won't have to make separate text files for each library. While running the program, I can simply log in to each site, view my "Items Out" and then copy the info in turn as the prompts appear. It amounts to the same thing as the above instructions, but would save the text file making step, which is just here for demonstrating the program's functionality without accessing the libraries' proprietary systems with my username and password. I would have made code to input the text files directly, but I'm not going to use it in that way.

###Current shortcomings:

I have not yet gotten the formatting right. This is going to take more effort with figuring out the proper string manipulation techniques and regex. I have made a good bit of progress, though. I got the beginning and ending elisions from the items fairly right, but I really need to figure out how to get the interior formatted correctly in some cases, as well as getting the various fields to line up under the headers properly. Getting them lined up is probably going to be my biggest challenge going forward.


