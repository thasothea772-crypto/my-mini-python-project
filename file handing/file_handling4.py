#File - Handling ===========================================

with open('text.txt', 'a') as file: #a is append that means it will add the text to the file.
    file.write("I love the learning Python Programming\n")
with open('text.txt', 'r') as file: #r is read that means it will read the text from the file.
    print(file.read())
