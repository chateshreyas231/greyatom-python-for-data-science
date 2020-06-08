# --------------
# Code starts here

# Create the lists 
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class= class_1 + class_2
print("class 1 and class 2 in new class",new_class)

# Append the list
new_class.append("Peter Warden")

# Print updated list
print("append new name",new_class)

# Remove the element from the list
new_class.remove("Carla Gentry")

# Print the list
print("new class is",new_class)

# Create the Dictionary
courses={'Math':65,'English':70,'History':80,'French':70,'Science':60}


# Slice the dict and stores  the all subjects marks in variable


# Store the all the subject in one variable `Total`
total=sum(courses.values())

# Print the total
print("total marks of Geoffrey Hinton ",total)

# Insert percentage formula
percentage=total/5

# Print the percentage
print("percentage",percentage)

# Create the Dictionary
mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}

# Given string
max_marks_scored = max(mathematics,key = mathematics.get)
print ("maximum marks scored in mathematics by",max_marks_scored)

# Create variable first_name 
first_name=(max_marks_scored.split()[0])
print("First Name Of the Topper In Maths ",first_name)

# Create variable Last_name and store last two element in the list
last_name=(max_marks_scored.split()[1])
print("Last Name Of the Topper In Maths ",last_name)

# Concatenate the string

# print the full_name
full_name=last_name+' '+first_name
print("Full Name is",full_name)

# print the name in upper case
certificate_name= full_name.upper() 
print("Certificate Name is ",certificate_name)
# Code ends here


