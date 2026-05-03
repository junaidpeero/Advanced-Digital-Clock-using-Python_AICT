## Advanced Digital Clock using Python
## Overview

This project is a graphical digital clock application built using Python and the Tkinter library. It displays real-time time, date, and day with a modern dark-themed interface and includes an alarm system with visual effects.

The application demonstrates GUI development, event-driven programming, and real-time system updates.

## Objectives
Develop a real-time digital clock
Design a simple and user-friendly GUI
Implement an alarm system
Apply modern UI styling (dark mode + neon effects)
Understand threading and event-driven programming
## Technologies Used
Programming Language: Python
GUI Library: Tkinter
Modules:
datetime → handles date and time
time → manages delays and updates
threading → runs alarm without freezing UI
## Features
## Real-Time Clock
Displays current time in HH:MM:SS AM/PM format
Updates automatically every second
## Date & Day Display
Shows current date in DD/MM/YYYY format
Displays the day of the week
## Dark Mode Interface
Black background for a modern and eye-friendly design
## Neon Visual Effect
Text color changes dynamically to create a glowing effect
## Alarm System
User can set alarm using input field
When time matches, visual alert is triggered
Runs using threading (does not freeze UI)
## How It Works
## Input
User enters alarm time in format:
HH:MM:SS AM/PM
Process
System continuously updates time every second
Compares current time with alarm time
Output
Displays time, date, and day
Triggers alarm with neon flashing effect
## Code Structure Explanation
Main Components
Main Window
Created using Tkinter
Styled with dark theme
Time Update Function
Uses strftime() to format time
Updates UI every 1 second using after()
Alarm System
set_alarm() → sets alarm time
check_alarm() → compares current time
trigger_alarm() → activates alert
Threading
Ensures alarm runs without stopping main application
Neon Effect
Changes label colors in loop to simulate glow
## How to Run
Make sure Python is installed
Save the file as advanced_digital_clock.py
Run the program:
python advanced_digital_clock.py
## Advantages
Simple and easy to use
Real-time updates
Attractive UI with effects
Good for beginners learning GUI
## Limitations
Alarm requires exact time format
No sound alert
Basic UI design
## Future Enhancements
Add sound alarm
Add snooze option
Improve UI design
Add stopwatch and timer
Add fullscreen mode
Integrate weather updates
## Conclusion

This project successfully demonstrates how to build a real-time GUI application in Python. It provides practical understanding of:

GUI development
Event-driven programming
Multithreading

It serves as a strong foundation for building more advanced applications.

## Author

Name: Muhammad Junaid
Roll Number: BS-IB-107210
