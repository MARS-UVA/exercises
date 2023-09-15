#!/bin/sh

#Linux commands in the shell script:
var1="Hello World"
echo $var1
echo "What's up! What is your name:"

read name
echo "Hello $name !"

echo "Let's see the computer play the Game of Life"
cd "src/games"
PROG_NAME="life.cpp"


