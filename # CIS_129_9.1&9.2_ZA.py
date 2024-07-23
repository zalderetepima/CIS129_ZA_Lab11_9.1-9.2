# Zach Alderete
# Lab 11 - Question 9.1
# 7/22/24.
# Program collects numeric grades from the user to write them into a text file. 
# Loop will let user enter grades until they break the loop. 
# Grades are validated to ensure they are in specefied parameters. Assumes grades are between 0-100. Can be adjusted as needed. 

# Open the file in write mode
with open('grades.txt', 'w') as file:
    while True:
        # Prompt user optoins
        grade = input("Enter a grade (or type 'done' to close program): ") 
        # Check is user is done entering grades
        if grade.lower() == 'done':
            break
        try:
            # Try to convert the input to a float to check if it's a valid number
            float_grade = float(grade)
            # Check if the grade is within the valid range
            if 0 <= float_grade <= 100:
                # Format the float to two decimal places and write to the file
                file.write(f"{float_grade:.2f}\n")
            else:
                print("Grade must be between 0 and 100. Please enter a valid grade.")
        except ValueError:
            # If the input is not a valid number, inform the user and continue the loop
            print("Invalid input. Please enter a valid number.")

print("Grades have been written to grades.txt")

# Lab 11 - Question 9.2
# Establish variables to store the total of the grades and the count of the grades
total = 0
count = 0

# Open the file in read mode
with open('grades.txt', 'r') as file:
    # Read each line (grade) from the file
    for line in file:
        # Strip the newline character and convert the line to a float
        grade = float(line.strip())
        # Display the individual grade and format .2f
        print(f"Grade: {grade:.2f}")
        # Add the grade to the total
        total += grade
        # Increment the count of grades
        count += 1

# Calculate the average of the grades
average = total / count if count != 0 else 0

# Display the total, count, and average of the grades
print(f"Total of grades: {total:.2f}")
print(f"Number of grades: {count}")
print(f"Average grade: {average:.2f}")
