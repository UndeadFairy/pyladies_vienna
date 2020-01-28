# Alarm Clock desktop tool
Small time reminder is always needed, right?

Desktop GUI applications can be easily built with some already created frameworks and can be run from any OS later. In the end you should compile your project into executable file for the operating system of your choice. **Here are some suggestions for GUI frameworks to use**:

  - PySimpleGUI - simple and enough for such a project
  - PyQt5 - more robust, may look too complex at the beginning, but may come handy with bigger projects
  - TkInter

So, your alarm clock tool should give audio or any other signal to user when a condition is met. Here the certain time is a condition and since the user don't have specific device, everything should run on personal laptop or desktop.


### Examples of Alarm Tools
- You can find them everywhere :) 

## Technical Details
Main objective of this project is to activate the signal of your choice when certain time of a day comes. 
  - Play signal in certain time
  - Allow user to create, edit and delete alarms
  - Display all set allarms
  - If you want to play a tone or song, use already created libraries for it
  - Application should constatnly look for set alarm times. It should trigger the signal everytime condition is met
  - To check for alarm times, these should be stored in some database with appropriate information


## Extra Challenge
  - Add possibility for reccuring alarms (every wednesday to practice python)
  - Add snooze feature
