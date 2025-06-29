file = open("output.txt", "w")
file.write("This is some sample content written to the file. \n moving to the next line")
file.close()
print("Content written to file.")

file1=open("output.txt", "r")
content = file1.read()
print(f"File content: '{content}'")