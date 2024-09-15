# Installation
1. To install Java on the VM, open terminal and run ```sudo apt install default-jdk```
2. To install Python, run ```sudo apt install python3```
# Python Exercises
1. (refactoring) Mikhail wrote a function called returnStuff a while ago to help with dump autonomy, but now nobody in the club can understand how it works! Help us make this code more understandable. The specificaitons are below.
    * The dump decision depends on two factors: the amount of regolith in the bin (a number), and whether we're in construction mode (a boolean).
    * If there's more than 5 cubic inches in the bin, we will dump. The decision is to either
        * dump immediately (code 2) if we're in construction mode
        * dump later (code 3) if we're not in construction mode
    * If there's 5 cubic inches of regolith or less in the bin, regardless of whether we're in construction mode, we do not dump (code 1).
2. (development, unit testing) Our robot has a thermometer, but it reads in Celsius. Write a function to convert Celsius to Fahrenheit.
    * Formula: T in Fahrenheit = T in Celsius * 1.8 + 32
    * Make sure the answer is an integer (int)
    * Write a test for the boiling point of water (100C = 212F) in Tests.py
    * Write a test for negative values to ensure your code handles those correctly (-10C = 14F).
3. (optimization) I wrote a function to compute skibonacci numbers. They're computed the following way:
    * The 0th, 1st, and 2nd skibonacci numbers are 1.
    * To compute subsequent skibonacci numbers, we skip the previous one, double the second to last one, and add the third to last one. 
    * However, the function is really slow. I'm trying to compute the 100th skibonacci number and it's taking ages. Help me optimize my code.
    * *Bonus: If you like math, see if you can find the sublinear solution*
4. (data wrangling) I have some weather data in resources/weather_long.csv.  This data is in *long format*, meaning it has a few columns to represent a lot of fields. Convert it to wide format, where the columns are City, Month, temperature, humidity, precipitation, wind speed, and air quality index. That way, we can more easily see what was going on in each city in each month. Output your data in a file called weather_wide.csv.
# Java Exercises
1. (test-driven development) Oh no! Someone wrote a whole load of spaghetti code for our MaxFinder class. It looks like it's passing our 1 unit test, but I'm suspicious of it. 
    - Write tests in the Main class until you find an error.
    - Fix the bug. Only 1 line should be changed.
    - Document the max method so people can understand what it does.
    - Fix the code as much as possible to make it clean and consistent, while maintaining the same behavior (refactoring).
2. (development, unit testing) Our robot has a thermometer, but it reads in Celsius. Write a function to convert Celsius to Fahrenheit.
    * Formula: T in Fahrenheit = T in Celsius * 1.8 + 32.
    * Make sure the answer is an integer (int).
    * Write a test for the boiling point of water (100C = 212F). in Main.java.
    * Write a test for negative values to ensure your code handles those correctly (-10C = 14F).