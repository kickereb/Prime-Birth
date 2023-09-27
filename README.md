# Prime Birthdays

## Description
This project generates a list of all prime birthdays that can occur in an input year. A prime birthday is one which, when written as DDMMYYYY format, is a prime number. For example, 30 October 1999 is 30101999.

The prime numbers used in this project are obtained from [The Prime Pages](https://t5k.org/lists/small/millions/), which provides lists of the first 100 Billion Prime Numbers.

## How to Run
1. Clone this repository.
2. Download the prime numbers from The Prime Pages and save them as text files.
3. Replace `'prime1.txt'` and `'prime2.txt'` in the Python script with the paths to your actual files containing the prime numbers (which can be downloaded from [src](https://github.com/kickereb/Prime-Birth/tree/main/src)).
4. Run the Python script in an environment where Python and pandas are installed and have necessary permissions to read your files.

## Features
- Generates a list of all prime birthdays that can occur in an input year.
- Outputs the list in a pandas DataFrame where each column is a month and each row is a day of the month.
- Calculates the total number of prime birthdays for each Zodiac sign from the year 0000 to 9999.

## Future Work
- Optimize the program to run faster.
- Create an interactive website where users can play around with the variables.
