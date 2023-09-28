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

## Examples

Here is an example of how to use this program:

### Input

Enter the year: 1999 <br>

### Output
```
   January  February  March  April   May  June  July  August  September  \
0      8.0       5.0    1.0    5.0   2.0   4.0   2.0     4.0        7.0   
1     14.0       7.0    3.0   11.0   5.0   9.0   6.0    25.0       22.0   
2     15.0       8.0   13.0   12.0  19.0  22.0  14.0     NaN        NaN   
3     17.0      13.0   16.0   23.0   NaN   NaN  23.0     NaN        NaN   
4      NaN      20.0    NaN    NaN   NaN   NaN  27.0     NaN        NaN   
5      NaN      26.0    NaN    NaN   NaN   NaN   NaN     NaN        NaN   
6      NaN       NaN    NaN    NaN   NaN   NaN   NaN     NaN        NaN   

   October  November  December  
0      3.0       5.0         7  
1      9.0      16.0         9  
2     23.0      19.0        10  
3     30.0      20.0        21  
4      NaN       NaN        28  
5      NaN       NaN        30  
6      NaN       NaN        31
```
```
Total number of prime birthdays for each Zodiac sign from the year 0000 to the year of interest are:
Capricorn: 12192
Aquarius: 18858
Pisces: 18745
Aries: 18738
Taurus: 19383
Gemini: 19272
Cancer: 19985
Leo: 19451
Virgo: 19436
Libra: 18810
Scorpio: 18617
Sagittarius: 18694
```
The DataFrame shows the prime birthdays for each month in the year `1999`. If a day is prime, it is filled with the day number; otherwise, it is `NaN`.

## Future Work
- Optimize the program to run faster.
- Create an interactive website where users can play around with the variables.
