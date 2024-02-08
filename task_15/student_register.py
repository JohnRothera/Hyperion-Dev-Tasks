# Using a function to avoid invalid user input,
# ask user for number of students needed for register.
def get_valid_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

student_id_count = get_valid_int_input("How many student IDs would you like on the register? ")

# Set a varibale to add student ID information to.
student_id_list = "Student ID numbers: \n \n"

# Loop through, adding the ID number for each entry per loop. 
for i in range(student_id_count):
    student_id = input("Please enter the students ID number: ")
    if i < student_id_count:
        student_id_list += f"{student_id}...................\n"
    
# Write the information to the file.    
with open('reg_form.txt','w') as f:
    f.write(student_id_list)   
