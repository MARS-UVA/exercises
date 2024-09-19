## Important Linux Commands
### Basic Filesystem commands
1) **pwd** - present working directory
    - Usage: pwd
    - Shows you the current directory path from root to your current working directory
1) cd - changing directory
   - Usage: cd [path to destination directory]
   - Paths include
     - ../ to go to a directory 1 level higher or ../[other directories from upper level directory]
     - ~/ to go to root directory or ~/[other directories from root directory]
2) mv - moving file from one source directory to a destination directory
     - Usage for renaming files: mv [source file name] [new name for file]
     - Usage for moving files: mv [file name to move] [path of directory to move to]
3) ls - listing files and directories within present working directory
4) rmdir - remove a, note, *empty* directory
5) rm - remove a file
     - If you want to remove a non-empty folder, use rm -rf [directory to remove]. The -rf flag means 'recursive force'.
4) grep - pattern matching using regular expressions
     - Usage: grep [regex to search for] [path to file you wish to search]
     - Regular Expression examples:
       - "literal value"
       - "^literal value" - empty string at start of line should be the only things in front of the literal
       - "literal$" - end of line character should be the only thing after the literal you are searching for
       - "..literal" - search for all words with 'literal' at the end
       - "h[e|l]lo" - search for words that must start with an 'h', must have either an 'e' or 'l' after, and must end with an 'l' and 'o'
       - "([A-Za-z0-9 ]*)" - search for strings with A-Z, a-z, or 0-9, in repetition, and the string must start and end with an open and close parenthesis respectively
5) tail and head - provide first or last n number of results from a file or another command
6) | - the pipe operator specifies to use an output from a previous command for the next command
7) ps - lists out all presently running processes
8) top - a command for Linux equivalent of task manager to view current processes and usage stats
8) kill - to terminate processes using a process ID or PID
       - Usage: kill [signal] [pid]
9) killall - to kill all processes
10) sed - stream editor command used to edit files and piped streams as input
11) chmod - change permissions to a file (can only be executed as a privileged or sudoer)
12) ifconifg - to display network information such as current IP address amd subnet (specifically subnet mask)
13) traceroute - to provide a list of hops between your source IP to a destination IP

### Shell Scripting
All of the above Linux commands and more can be run in a unified file called an .sh or shell file. The shell file allows you to automate Linux processes with ease.
We will give a quick demo of shell scripting.

### Cron Jobs
Linux allows you to run chronological jobs at specific intervals.
If you have a command you want to run or shell script at specified time periods, use *crontab -e* to launch an editor for your new cronjob.
Add '* * * * * [linux command to run]' to your crontab.
The 5 asterisks specify certain parameters for the frequency of your cronjob runs:
1) What minute of every hour from 0-59
2) What hour of every day from 0-23
3) What day of every month from 0-31
4) What month of every year from 1-12
5) Which weekday of every week from 0-6

*tail -f /var/log/syslog* to list as of currently executed cronjobs.

### Practice Tasks:
