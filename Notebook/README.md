FOCPP – Lab Worksheets (Weeks 1–8)

This folder contains all the practical worksheets done regularly from week1-8.

Week 1 – Basics

This focuses on basic Python program execution, printing output, arithmetic expressions, operator precedence, and awareness of common errors. It is to understand how a Python program runs, display output using `print()`, evaluate arithmetic expressions, and observe how operator precedence affects results.

This worksheet does not require any user input.  
All values used in the program are hardcoded within the source code.

The program produces the following output when executed:

Hello World
Python is running
65
15
50
3.0303030303030303
3
100
1
20
30


Week 2 – Variables and Data Types
Focus
Variables, numbers, strings, Booleans, type conversion.
Purpose
Store, manipulate, and display data.
Input Validation
Ensure numeric values are converted using int() or float().
Strings should be handled as-is.
Tasks
task1_numbers_strings.py
Description: Work with numbers and strings
Example Input:
Enter a number: 5
Enter a word: Hello

Example Output:
Number squared: 25
Word repeated twice: HelloHello

task2_type_conversion.py
Description: Convert types and perform calculations
Example Input:
Enter a number: 7

Example Output:
Number as string: '7'
Number plus 10: 17


Week 3 – Conditionals
Focus
if, elif, else statements, Boolean logic, ternary expressions.
Purpose
Control the flow of programs based on conditions.
Input Validation
Ensure numeric input is properly converted.
Handle unexpected text input gracefully (optional).
Tasks
task1_if_else.py
Description: Basic decision-making
Example Input:
Enter your age: 18

Example Output:
You are an adult.

task2_ternary.py
Description: Use concise conditional expressions
Example Input:
Enter a number: 7

Example Output:
The number is odd


Week 4 – Loops
Focus
for loops, while loops, break, continue.
Purpose
Repeat tasks efficiently and automate processes.
Input Validation
Ensure loop counts are numeric.
Handle empty or invalid input.
Tasks
task1_for_loop.py
Description: Loop over a range
Example Output:
1
2
3
4
5

task2_while_loop.py
Description: Repeat while a condition is True
Example Input:
Enter number to count down from: 3

Example Output:
3
2
1
0

 Week 5 – Functions
Focus
Defining functions, parameters, return values, scope.
Purpose
Write reusable code and improve organization.
Input Validation
Ensure numeric input is converted correctly.
Check for valid function arguments.
Tasks
task1_rectangle_area.py
Description: Calculate area of a rectangle
Example Input:
Width: 5
Height: 3

Example Output:
Area of rectangle: 15

task2_circle_area.py
Description: Calculate area of a circle
Example Input:
Radius: 4

Example Output:
Area of circle: 50.27

 Week 6 – Lists and Tuples
Focus
Lists and tuples: storing multiple values, accessing elements.
Purpose
Manage collections of data efficiently.
Input Validation
Ensure numeric input is converted if needed.
Handle empty lists/tuples.
Tasks
task1_list_operations.py
Description: Perform operations on lists
Example Output:
Original list: [1, 2, 3]
After append: [1, 2, 3, 4]

task2_tuple_access.py
Description: Access elements in a tuple
Example Output:
Tuple: (10, 20, 30)
Second element: 20


Week 7 – Sets and Dictionaries
Focus
Set operations, dictionaries (key-value pairs).
Purpose
Store unique values and map keys to values.

Input Validation
Ensure unique inputs for sets.
Ensure valid dictionary keys exist before access.
Tasks
task1_sets.py
Description: Perform set operations
Example Output:
Set A: {1, 2, 3}
Set B: {3, 4}
Union: {1, 2, 3, 4}
Intersection: {3}

task2_dictionaries.py
Description: Work with dictionaries
Example Output:
Student ages: {'Alice': 23, 'Bob': 25}
Alice's age: 23


Week 8 – Input/Output and File Handling
Focus
Display output with formatting (f-strings, str.format())
Read/write text files
Append data, random file access, with statement
Purpose
Learn to interact with users and files, format outputs, and handle exceptions.
Input Validation
Ensure numeric inputs are converted.
Check files exist before reading.
Handle invalid lines gracefully.
Tasks
task1_rectangle_area_fstring.py
Description: Format rectangle area using f-strings
Example Output:
The area of a rectangle with width 104.32 and height 15.654 is 1634.961

task2_rectangle_area_fstring_precision.py
Description: Limit area to 3 decimal places
Example Output:
The area of a rectangle is 1634.961

task3_name_age_format.py
Description: Column width, alignment, fill character
Example Output:
$$$$$$$$$$Donald$$$$$$$$$$ - $$$$$$$75.00$$$$$$$

task4_alignment_fill.py
Description: Advanced alignment formatting

task5_circle_area_format.py
Description: Use str.format() to display area
Example Output:
A circle with radius 52 has an area of 8494.8665353068

task6_format_equivalent.py
Description: Convert f-string to str.format()

task7_read_entire_file.py
Description: Read entire contents of info.txt

task8_read_line_by_line.py
Description: Read lines individually

task9_read_for_loop.py
Description: Iterate file with for loop

task10_append_file.py
Description: Append text to file

task11_with_statement.py
Description: Use with to auto-close file
