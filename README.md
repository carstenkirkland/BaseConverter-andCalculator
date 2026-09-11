# Decimal, Binary, Octal & Hexadecimal Converter + Calculator

[Code File](https://github.com/carstenkirkland/BaseConverter-andCalculator/blob/main/code.py)  
[Example Result File](https://github.com/carstenkirkland/BaseConverter-andCalculator/blob/main/results.txt)

## Description

This Python program allows users to convert numbers between binary, octal, decimal, and hexadecimal or perform arithmetic calculations in a selected number system.

I developed this project during my freshman year as a way to apply what I was learning in Python while also becoming more familiar with binary and hexadecimal number systems used in electrical and computer engineering.

The program includes number-base conversion, arithmetic operations, input validation, error handling, file-based result storage, and data visualization using Matplotlib.

---

## How to Use the Program

When the program starts, select one of the following options:

1. Convert a number between bases
2. Perform a calculation in a chosen base
3. Quit the program

### Option 1: Number Conversion

If you choose **1**, enter:

1. Starting base:
   - Binary
   - Octal
   - Decimal
   - Hexadecimal
2. The number in that base
3. The base you want to convert to

Example input:

- Option: 1
- Starting base: Decimal
- Number: 255
- Output base: Hexadecimal

Expected output:

**Converted Value: FF**

The program also generates a bar graph comparing the length of the number in binary, octal, decimal, and hexadecimal.

The conversion is saved to a results file containing previous program outputs.

Example:

**CONVERSION: 255 (decimal) -> FF (hexadecimal)**

---

### Option 2: Perform Calculation

If you choose **2**, enter:

1. Base of the calculation:
   - Binary
   - Octal
   - Decimal
   - Hexadecimal
2. First number
3. Operation:
   - `+`
   - `-`
   - `*`
   - `/`
4. Second number

Example input:

- Option: 2
- Base: Hexadecimal
- First number: A
- Operation: +
- Second number: 5

Expected output:

**Result: F**

The calculation is also saved to the results file.

Example:

**CALCULATION: A + 5 in base hexadecimal = F**

> **Note:** The graph is only generated for number conversions, not calculations.

---

### Option 3: Quit

Enter **3** to exit the program.

---

## Program Features

- Converts between binary, octal, decimal, and hexadecimal
- Performs arithmetic operations in multiple number systems
- Saves previous conversions and calculations to a file
- Generates a bar graph using Matplotlib
- Checks for invalid base inputs
- Prevents division by zero
- Uses separate functions to organize program logic

---

## Reflection

This project was the culmination of what I learned in my introductory Python course and was one of my first opportunities to independently design a program around a topic that interested me.

At the time, I had not yet started my core electrical engineering coursework, but I knew that binary and hexadecimal number systems would become important later in my degree. I used the project as an opportunity to develop both my programming skills and my familiarity with these number systems.

One of the most valuable parts of the project was learning how to break a larger problem into smaller functions for conversion, calculation, visualization, and file handling. Separating each task made the program easier to build, test, and debug.

During development, I encountered several issues involving incorrect inputs, numbers that did not match the selected base, missing prompts, and division by zero. I addressed these problems by adding input validation, error messages, and additional testing.

This project also strengthened my understanding of Python functions, loops, file I/O, data visualization, input validation, and debugging. I especially enjoyed the troubleshooting process of identifying why the program was producing an error or unexpected result and determining how to correct it.

---

## Tools & Technologies

- **Python**
- **Visual Studio Code**
- **Matplotlib**

## Key Concepts

- **Number-base conversion**
- **File I/O for saving results**
- **Data visualization with Matplotlib**
- **Modular function-based program structure**
- **Input validation and error handling**
- **Testing and debugging**
