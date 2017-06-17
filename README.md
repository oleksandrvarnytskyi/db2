# db2
1. Write a function that takes as a parameters number1(int), number2(int) and number3. (e.g. handle_numbers(number1, number2, number3))
Function need to return the count of integers that are divisible by number3 in range [number1, number2]
Example:
number1 = 1
number2 = 10
number3 = 2

Result: 
5, because 2, 4, 6, 8, 10 are divisible by 2


2. Write a function that takes sentense as a parameter (e.g. handle_string(value)) and count number of letters and digits.
Example:
value = "Hello world! 123!"

Result:
Letters -  10
Digits -  3


3. Write a function that takes list of tuples (e.g. handle_list_of_tuples(list)) and sort it based on the next rules:
name / age / height / weight
Example:
list = [
    ("Tom", "19", "167", "54"), 
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75") 
    ("John", "27", "190", "87"), 
    ("Jony", "24", "191", "98"), 
    ]

Result:
[
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("Tom", "19", "167", "54"),
]

