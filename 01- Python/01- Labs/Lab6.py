
#define Instructions function
def Display_Instructions():
	while True:
		print("==========Enter Method number to get Info========\n")
		print("================= 1- index()=====================\n")
		print("================= 2- split() ====================\n")
		print("================= 3- strip() ====================\n")
		print("============== Exit(): Press Esc=================\n")
		choice1 =  input()

		if choice1 in Method_Info_Dic:
			print(f" you have choosed {choice1} \n {Method_Info_Dic[choice1]}")
			if choice1 == "1":
				
				print("\n my_list = [10, 20, 30, 40, 50]\n\
				try:\n #Find the index of the element 30\n \
				index = my_list.index(30)\n \
				print(index) # outputs: 2\n")
			elif choice1 == "2":
				print("\n my_string = ""Hello, world!\n"\
				"# Split the string into a list of substrings based on the comma separator\n"
				"\n my_list = my_string.split(",")"
				"\n print(my_list)  # outputs: ['Hello', ' world!']")
			elif choice1 == "3":
				print("\n my_string = "  "Hello, world!  \n"\
					"# Remove leading and trailing whitespace from the stringn\n"\
					"new_string = my_string.strip()\n"\
					"print(new_string)  # outputs: 'Hello, world!'\n")

	
	
Method_Info_Dic = {
"1": "index(): Searches the string for a specified value and returns the position of where it was found",
"2": "Split() : Splits the string at the specified separator, and returns a list",
"3": "Strip(): Returns a trimmed version of the strings",
}
#exec function
Display_Instructions()

