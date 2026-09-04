<h1> Decimal, Binary, Octal & Hexadecimal Convert + Calculator</h1>


<h2>Description</h2>
USER INPUT INSTRUCTIONS


This program allows you to either convert numbers
between bases or perform calculations in a chosen base.


When the program starts, type one of the following:


    1  → Convert a number between bases
    2  → Perform a calculation in a chosen base
    3  → Quit the program


     

 <br />


OPTION 1: NUMBER CONVERSION


If you choose 1, you will enter THREE inputs:


1. Starting base  (type exactly one)
       binary
       octal
       decimal
       hexadecimal


2. The number in that base
   Example valid inputs:
       decimal     → 255,
       binary      → 101101,
       octal       → 127,
       hexadecimal → AF3


4. The base you want to convert to
   (same four options as above)


Example Input Sequence:
    1,
    decimal,
    255,
    hexadecimal.




After this, a bar graph will appear showing how long the number is in
binary, octal, decimal, and hex.


Expected Output:
    Converted Value: FF
Will save result in a file which stores all previous tasks
    Ex: CONVERSION: 255 (decimal) -> FF (hexadecimal)


<br />



OPTION 2: PERFORM CALCULATION


If you choose 2, you will enter FOUR inputs:


1. Base of the calculation (choose one)
       binary
       octal
       decimal
       hexadecimal


2. First number (must match the base)


3. Operation (choose one)
       +
       -
       *
       /


4. Second number (same base as the first)


Example Input Sequence:
    2,
    hexadecimal,
    A,
    +,
    5.


*Note there is no graph for this one


Expected Output:
    Result: F
Will save result in a file which stores all previous tasks
    Ex: CALCULATION: A + 5 in base hexadecimal = F


<br />

OPTION 3: QUIT PROGRAM


Type:
    3
to exit the program.

<br />


<h2>Tools & Technologies</h2>

- <b>Python</b> 
- <b>Visual Studio Code</b>
- <b>Matplotlib</b>

<br />

<h2>Key Concepts</h2>

- <b>File I/O for saving results</b> 
- <b>Data visualization with Matplotlib</b>
- <b>Modular function-based program structure</b>
- <b>Input validation and error handling</b>
</p>
