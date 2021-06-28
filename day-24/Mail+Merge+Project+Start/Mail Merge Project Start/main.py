#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from turtle import mode, write


with open("Input/Letters/starting_letter.txt") as data:
    content = data.read()
with open("Input/Names/invited_names.txt") as data:
    names = data.readlines()

for i in range(len(names)):
    names[i] = names[i].strip('\n')

for name in names:
    new_content = content.replace("[name]", name)
    with open(f"Output/ReadyToSend/{name}.txt", mode="w") as data:
        data.write(new_content)



#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp