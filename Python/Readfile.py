# READING FROM FILE
employee_file = open("employees.txt", "r")  # opens file read mode
print(employee_file.readable())  # checks file is readable
#print(employee_file.read())  # reads entire file to screen
#print(employee_file.readline())  # can be used multiple times to read next line in file
#print(employee_file.readlines())  # reads each line into a list
print(employee_file.readlines()[1])  # reads into a list and displays item at position 1 in the list
#employee_file.close()  # closes file

for employee in employee_file.readlines():
    print(employee)
employee_file.close()

# WRITING AND APPENDING TO FILE
employee_file = open("employees.txt", "a")  # opens file append mode
employee_file.write(
    "Toby - HR")  # in append mode will append this onto the end of the last line, not after the last line
employee_file.write(
    "\nToby - HR")  # in append mode will add a newline char to the end of the last line, then write a new line

employee_file = open("employees.txt", "w")  # opens file write mode
employee_file.write("Toby - HR")  # in write mode, this will overwrite the file entirely

employee_file.close()