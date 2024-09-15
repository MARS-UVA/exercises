# Installation
1. To install Java on the VM, open terminal and run ```sudo apt install default-jdk```
2. To install Python, run ```sudo apt install python3```

# Compilation and Running
- Python: ```python3 [file_name].py [taskNo] [args]```
     * taskNo - which task you want to run from 1-8
     * args - arguments for the task you are running
          - Task 1: integer number and boolean("true"/"false")
          - Task 2: double number
          - Task 3: integer number
          - Task 4-8: does NOT ake any argument
- Java:
     * In JavaExercises/src, execute ```javac *.java```
     * Execute ```java [ClassName]``` to execute the program (Your class should be Main but you can run the other classes)

# Git Quick Guide
- ```git pull```
- ```git add [file path]```
- ```git commit -m "Commit message..."```
- ```git push```
- Merging branches
  * ```git checkout [branch to merge code into]```
  * ```git merge [branch to merge from]```
- Rollback changes
  * Reverting to previous commit and effectively cancelling out previous commits:
    - ```git revert HEAD```
    - ```git revert HEAD~3```
    - ```git revert [hash to revert back to]```
  * Reset to previous commit moves the HEAD pointer to the commit corrresponding to the hash
    - git reset [hash to reset HEAD at]


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
5. (parsing byte messages) Your dumb robot with a wheel and a single arm is receiving a byte message on its serial port and your job is to decode what it means so you can send it up to the user interface. Here is what the byte message looks like:

   execution flag | motor current values | actuator direction | actuator current value | ultrasound start flag | ultrasound values | ultrasound end flag | led on/off | hash of byte string | null terminator

   Here is what each field of data should look like:
   -  Execution Flag - should be 1, if not then throw an exception saying "Robot commands must not be executed"
   -  Motor Values - a series of 4 motor values will be present and each will be integers
   -  Actuator Direction - 1 indicates that the actuator is going up and 2 indicates that the actuator is going down
   -  Actuator Current Value - a single current value as a double is given
   -  Ultrasound Start Flag - this value will always be "USTR", 4 bytes exactly, and indicates that start of a stream of ultrasound sensors data points
   -  Ultrasound Values - A series of floating point numbers
   -  Ultrasound End Flag - this value will always be "UEND", 4 bytes exactly, whcih indicates that the ultrasound stream has ended.
   -  LED ON/OFF - 1 indicates that LED is off and 0 indiciates that it should be on.
   -  Hash of Byte String - Hash of everything earlier. Use this to verify that the message came across without corruption.
   -  Null Terminator - indicates that end of a packet and will come with the value "TERM".

      Your job is to parse the stream of bytes and put significant values in an array to return. Here is what your array should include:
  
      [Motor Value 1, Motor Value 2, Motor Value 3, Motor Value 4, Actuator Current Value, Ultrasound Values..., LED value]
  
      ** Bonus: Using motor values, decide if robot is going straight or turning and if so, which direction it is turning (right or left). Place that value at the end of the array.

  
6. (matrix problem) For this problem, you will be given an NxM grid where N and M are randomly selected. There are 0s randomly placed in the grid which represent obstacles. Your robot starts in the top-left hand corner of the grid at position (0,0) and is supposed to get to the bottom-right hand corner (N-1, M-1). Your job is to compute the total number of possible paths that the robot can take without hitting the 0s. If none exist, return 0. Otherwvise, return the number of paths.

      May be helpful to write test cases with example grids.

7. (json read and write) For this problem, you will read in a JSON file with your calendar called events.json. Here is what you need to do:
   -  Your holidays are out of order. Using the "date" field, reorder them.
   -  You have events on your calendar with the same title. Consolidate those events into a single event.
        * Events with the same 'title' may have different dates. Use the latest date as your new date.
        * Concatenate the descriptions into a single description for your new event.
8. (read files) Read some ROS logging info in /logs/feedbackLog.txt. In that file, you want to check for 2 conditiojns and report when the condition occurred:
   - Check if motor current is above 4 Amps in which case the motor is overworking.
   - Check if sensor output voltage is above 3 V is which case it is being triggered.
   
   In both cases, append the datetime to an array and return the final array.

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
