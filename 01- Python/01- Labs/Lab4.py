#receive input from cmd

	
s1, s2, s3 = input("Please Enter Three Sensor Numbers\n").split(" ",3)
s1 = int(s1)
s2 = int(s2)
s3 = int(s3)

sensor_read_List = [s1, s2, s3]

sensor_read_Tuple = s1, s2, s3

sensor_read_Dic ={
"s1": s1,
"s2": s2,
"s3": s3
}

print("List Sensor values:\n")
print(sensor_read_List)
	
print("Tuple Sensor values:\n")
print(sensor_read_Tuple)
	
print("Dic Sensor Values:\n")

print(sensor_read_Dic)