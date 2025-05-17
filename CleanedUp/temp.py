# Ask the user what acronym they want to add
# Then ask the user for the definition
# Open the file
# Write the new acronym and definition to the file

acronym = input('What acronym do you want to add?\n')
definition = input('What is the definition?\n')
with open('input.txt', 'a') as file:
    file.write(acronym + ' - ' + definition + '\n')