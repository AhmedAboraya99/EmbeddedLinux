# Automating Build Process for Lighting LEDs using RTO on STM32F401CC

This project is a Python script that automates the build process for flashing code of lighting LEDs using our own real-time operating system "RTO" on an STM32F401CC board with IMT Kit.
 The script uses the Tkinter GUI library to create a user-friendly interface that simplifies the process of entering the LED port and pins values, and updating the configuration file.
 It also helps make the process more efficient and automated, saving time and reducing the chance of errors.

## Prerequisites

Before running the script, you need to have the following prerequisites:

- [Python 3](https://www.python.org/downloads/) installed on your system.
- {Optional}[STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html) installed on your system.
- [ST-Link Utility](https://www.st.com/en/development-tools/stsw-link004.html) installed on your system.

5. On the GUI, enter the LED port and pins values and click on the "Build and Flash" button.
6. The script will then change the values in the configuration file, build the project using the makefile, and finally flash the code using the st-link cli flash command.

## Credits

This project was developed as part of my studies at ITI. I would like to express my sincere gratitude to my instructors for their guidance and support throughout this project.
