This set of Python Scripts are designed to help with transferring data from large excel spreadsheets when people don’t format things correctly (i.e. putting more than one piece of data into a cell). Also. EXCEL IS NOT A DATABASE, SO STOP USING IT AS ONE. The main purpose of this program is for when users treat spreadsheets like databases. Have too much data in a spreadsheet? use regex. Excel? No regex. Please, use databases for this kind of thing.

===Supported File formats===
.xlsx
.xls
============================

Your Excel file must be the same as the file name on line 4 of ToCSV.py

run ToCSV first, select the spreadsheet file that you want to use, and name the output file, then open that output file in a text editor. All you have to do is add spaces where you want commas to be. Then run AddCommas.py

A comma denotes a cell. lines denote rows. 
The data is essentially just a raw spreadsheet
2,4,6,8
1,2,3,4
10,13,0,3 
will open like this is a spreadsheet
--------------
|2|4|6|8
--------------
|1|2|3|4
--------------
|10|13|0|3
--------------

if you did this 

2,4,6,8
1,2,3,4
1,0,1,3,0,3

in the file that comes out after you run ToCSV, the spreadsheet would look like

--------------
|2|4|6|8
--------------
|1|2|3|4
--------------
|1|0|1|3|0|3
--------------

The 10 is separated into 1,0 Which is parsed by the spreadsheet as two separate cells, containing 1 and 0 respectively.
