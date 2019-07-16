#!/bin/bash
cd /home/pi/tetris/
echo Tetris Bash Script
pwd
python3 webserverV2.py &
python3 MAIN.py

