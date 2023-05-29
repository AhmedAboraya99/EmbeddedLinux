import os
import subprocess
import tkinter as tk


# Define the path to the STM32CubeIDE executable
STM32CUBEIDE_PATH = r"C:/ST/STM32CubeIDE_1.4.0\STM32CubeIDE/STM32CubeIDE.exe"

# Define the path to the project directory
PROJECT_PATH = r"E:\Work\Embedded systems\ITI Diploma\ITI_Dev\Linux\01- Python\02- Tasks\Build Proccess Task"

# Define the name of the project
PROJECT_NAME = "STM_ARM_RTO"

# Define the path to the ST-Link Utility executable
STLINK_PATH = r"C:\Program Files (x86)\STMicroelectronics\STM32 ST-LINK Utility\ST-LINK Utility\STM32 ST-LINK Utility.exe"

# Define the name of the HEX file
HEX_NAME = "STM_ARM_RTO.hex"
# Define the name of the Binary file
BINARY_NAME = "STM_ARM_RTO.bin"
binary_path = f"{BINARY_NAME}"


def make_clean():
    # Get the list of files and directories in the current working directory
    files = os.listdir()

    # Remove all files and directories created by the `make` command
    for file in files:
        if file.endswith('.o') or file.endswith('.bin') or file.endswith('.hex') or  file.endswith('.elf') or os.path.isdir(file) and file != '.':
            # The file is a Makefile, object file, or directory (excluding the current directory)
            if os.path.isfile(file):
                # The file is a regular file
                os.remove(file)
            elif os.path.isdir(file):
                # The file is a directory
                os.system(f'rm -rf {file}')  # Recursively remove the directory
# Define the function that will write the config value to the file
def write_config():
    # Get the value from the entry widget
    value0  = entry0.get()
    value1 = entry1.get()
    value2 = entry2.get()
    value3 = entry3.get()
    root.destroy()


 # Open the config file for reading and writing
    with open('MCAL_GPIO_Config.h', 'r') as f:
        # Read the existing content of the file
        content = f.readlines()

    # Modify the configuration values in the content
    for i in range(len(content)):
        if 'LED_Port' in content[i]:
            content[i] = f"#define LED_Port {value0}\n"
        elif 'LED1_Pin' in content[i]:
            content[i] = f'#define LED1_Pin {value1}\n'
        elif 'LED2_Pin' in content[i]:
            content[i] = f'#define LED2_Pin {value2}\n'
        elif 'LED3_Pin' in content[i]:
            content[i] = f'#define LED3_Pin {value3}\n'

    # Write the modified content back to the file
    with open('MCAL_GPIO_Config.h', 'w') as f:
        f.writelines(content)

# Create the main window
root = tk.Tk()

#Name the window
root.title("STM ARM Build")
#Add the label to the window

################################Controlling window geometery#########################################
# controlling window geometry in pixles 
root.geometry('1000x500')

# Add a label and entry widget for the config value
label0 = tk.Label(root, text="LED Port:")
label0.pack()
entry0 = tk.Entry(root)
entry0.pack()

label1 = tk.Label(root, text="LED1 Pin:")
label1.pack()
entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="LED2 Pin:")
label2.pack()
entry2 = tk.Entry(root)
entry2.pack()

label3 = tk.Label(root, text="LED3 Pin:")
label3.pack()
entry3 = tk.Entry(root)
entry3.pack()

# Add a button to write the config value to the file
button = tk.Button(root, text="Start Build", command=write_config)
button.pack()

# Run the main event looproot.mainloop()
root.mainloop()

# Run the "make hex" command
makefile_path = "makefile"
makefile_target = "STM_ARM_RTO"

# Run the make command to build the hex file
make_clean()
make_command = ["make", "-f", makefile_path]
result = subprocess.run(make_command, check=True)

# Set the permission of the binary file to 0777
os.chmod(binary_path, 0o777)

# Check if the command was successful
if result.returncode == 0:
    print("Hex file built successfully!")
else:
    # Print the error message if the command failed
    print("Error building hex file:")
    print(result.stderr)

# Determine the path to the ST-Link CLI tool
STLINK_CLI_PATH = "C:\Program Files (x86)\STMicroelectronics\STM32 ST-LINK Utility\ST-LINK Utility\ST-LINK_CLI.exe"

# Flash the code using the ST-Link Utility tool
subprocess.run([STLINK_CLI_PATH, "-c", "SWD","-P",  f"{BINARY_NAME}", "0x08000000", "-V","-Rst"], check=True)

